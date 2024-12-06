import sqlite3

def create_database():
    conn = sqlite3.connect('financial_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS financial_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            di REAL,
            dolfut REAL,
            dvdi INTEGER,
            usdbrl REAL,
            usdx REAL,
            over_rate REAL,
            fair_price REAL,
            openingPrice REAL,
            max_open REAL,
            min_open REAL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
