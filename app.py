from flask import Flask, render_template
import sqlite3


app = Flask(__name__)

def get_latest_data():
    conn = sqlite3.connect('financial_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT timestamp, di, dolfut, dvdi, usdbrl, usdx, over_rate, fair_price, openingPrice, max_open, min_open
        FROM financial_data
        ORDER BY timestamp DESC
        LIMIT 1
    ''')
    data = cursor.fetchone()
    conn.close()
    return data

@app.route('/')
def index():
    data = get_latest_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)