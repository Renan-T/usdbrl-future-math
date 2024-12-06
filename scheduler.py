import schedule
import time
import pytz
from datetime import datetime
import holidays
from data_fetcher_di import fetch_di_value
from data_fetcher_dolfuture import fetch_dolfuture_value
from data_fetcher_dvdi import working_days_to_maturity
from data_fetcher_usdbrl import fetch_usdbrl_value
from data_fetcher_usdx import fetch_usdx_value
from math_operations import *
import sqlite3


def is_working_day():
    br_timezone = pytz.timezone("America/Sao_Paulo")
    today = datetime.now(br_timezone).date()
    br_holidays = holidays.Brazil(state='SP')
    return today.weekday() < 5 and today not in br_holidays

def fetch_all_data():
    DI = fetch_di_value()
    DOLFUT = fetch_dolfuture_value()

    start_date = datetime.now()

    DVDI = working_days_to_maturity(start_date)

    USDBRL = fetch_usdbrl_value() * 1000
    USDX = fetch_usdx_value()

    return DI, DOLFUT, DVDI, USDBRL, USDX

def run_math_operations():
    DI, DOLFUT, DVDI, USDBRL, USDX = fetch_all_data()
    
    overRate = over_rate(DVDI, DI)
    fairPrice = round(fair_price(overRate, USDBRL), 2)
    openingPrice = round(opening(DOLFUT, USDX), 2)
    maxOpen = round(max_opening(openingPrice, overRate, DELTA), 2)
    minOpen = round(min_opening(maxOpen, DELTA), 2)

    # Save to the database
    conn = sqlite3.connect('financial_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO financial_data (
            di, dolfut, dvdi, usdbrl, usdx, over_rate, fair_price, openingPrice, max_open, min_open
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (DI, DOLFUT, DVDI, USDBRL, USDX, overRate, fairPrice, openingPrice, maxOpen, minOpen))
    conn.commit()
    conn.close()

def schedule_jobs():
    if is_working_day():
        schedule.every().day.at("9:50").do(run_math_operations)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    schedule_jobs()
    run_schedule()
