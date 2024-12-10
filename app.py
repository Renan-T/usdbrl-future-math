from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_all_data():
    conn = sqlite3.connect('financial_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT timestamp, di, dolfut, dvdi, usdbrl, usdx, over_rate, fair_price, openingPrice, max_open, min_open
        FROM financial_data
        ORDER BY timestamp DESC
    ''')
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    data = get_all_data()
    headers = [
        "Timestamp", "DI", "Dollar Future", "DVDI", "USDBRL", "USDX", 
        "OverRate", "FairPrice", "OpeningPrice", "MaxOpening", "MinOpening"
    ]
    return render_template('index.html', headers=headers, data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
