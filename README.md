# usdbrl-future-math - Financial Analysis Tool

usdbrl-future-math is an automated tool for financial market analysis. It collects real-time data, performs calculations for key metrics like overRate, fairPrice, and others, and displays them through an interactive dashboard.

---

## **Key Features**
- Fetches real-time data for:
  - USDX (U.S. Dollar Index)
  - USDBRL (USD to Brazilian Real exchange rate)
  - Brazilian mini-dollar futures
  - DI (Interbank Deposit rates)
- Automates periodic data updates using a Python scheduler.
- Calculates essential financial metrics:
  - **OverRate**: Measures contract volatility.
  - **FairPrice**: Theoretical price based on market trends.
  - **Opening, MaxOpening, MinOpening**: Price levels for better market insights.
- Displays results on a user-friendly Streamlit dashboard.
- Modular backend built with Flask, allowing API integrations.

---

## **Tech Stack**
1. **Python**:
   - Libraries: `streamlit`, `flask`, `sqlite3`, `schedule`, `pandas`, `yfinance`, `selenium`
2. **Database**:
   - SQLite for storing calculated metrics.
3. **Deployment**:
   - Streamlit for the dashboard.
   - Flask for backend APIs.
   - Scheduler for periodic data updates.

---

## **Installation**

### 1. Clone the Repository
```bash
git clone https://github.com/Renan-T/usdbrl-future-math.git
cd usdbrl-future-math

1. Install Dependencies

pip install -r requirements.txt

2. Set Up the Database

python models.py

3. Run Flask Backend

python app.py

4. Run the Scheduler

python scheduler.py

5. Run Streamlit Dashboard

streamlit run streamlit_app.py
