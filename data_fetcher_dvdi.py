import pandas as pd
import holidays
from datetime import datetime, timedelta

def get_di_maturity():

    # Get the current date
    now = datetime.now()

    # Move to the next month
    first_day_of_next_month = (now.replace(day=1) + timedelta(days=32)).replace(day=1)

    # Get holidays for Sao Paulo, Brazil
    br_holidays = holidays.Brazil(years=[first_day_of_next_month.year], state='SP')

    # Find the first business day of the next month
    while first_day_of_next_month.weekday() >= 5 or first_day_of_next_month in br_holidays:
        first_day_of_next_month += timedelta(days=1)

    return first_day_of_next_month


def working_days_to_maturity(start_date=None):

    if start_date is None:
        start_date = datetime.now()

    # Get the DI maturity date
    end_date = get_di_maturity()

    # Get holidays for São Paulo, Brazil
    br_holidays = holidays.Brazil(years=[start_date.year, end_date.year], state='SP')

    # Convert holidays to a list of dates
    br_holiday_dates = list(br_holidays.keys())

    # Get all business days between start_date and end_date
    business_days = pd.date_range(start=start_date, end=end_date, freq='B')
    working_days = [day for day in business_days if day not in br_holiday_dates]
    

    return len(working_days)