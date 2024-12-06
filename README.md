# USD/BRL Future Math

**USD/BRL Future Math** is a Python-based financial analysis tool designed to automate data fetching, processing, and visualization of key financial metrics. It calculates OverRate, FairPrice, Opening, MaxOpening, and MinOpening using real-time and historical data, making it an essential tool for financial analysis.

---

## Key Features

- **Data Fetching**:
  - Real-time data from reliable sources for:
    - USDX (U.S. Dollar Index)
    - USDBRL (USD to Brazilian Real exchange rate)
    - Brazilian mini-dollar futures
    - DI (Interbank Deposit rates)
  - Accurate handling of business days and holidays for maturity calculations.

- **Mathematical Calculations**:
  - Calculates:
    - OverRate: Measures volatility.
    - FairPrice: Theoretical price based on trends.
    - Opening, MaxOpening, and MinOpening: Useful price levels.

- **Interactive Dashboard**:
  - Built using **Streamlit**, providing a user-friendly interface to display metrics.

- **Modular Backend**:
  - Flask-based backend for API interactions.
  - Scheduled tasks for periodic updates.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- SQLite (for local database storage)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Renan-T/usdbrl-future-math.git
   cd usdbrl-future-math



2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set Up the Database** 
   ```bash
   Initialize the database:
   python init_db.py

4. **Run the Flask Backend** 
   ```bash
   Start the Flask server:
   python app.py

5. **Run the Scheduler** 
   ```bash
   Start the scheduler for periodic updates:
   python scheduler.py

6. **Run the Streamlit Dashboard** 
   ```bash
   Start the Streamlit interface:
   streamlit run streamlit_app.py

**Usage**
   ```bash
   Open the Streamlit dashboard in your browser (default: http://localhost:8501).
   View the latest metrics fetched and calculated from financial data.
   Data updates automatically via the scheduler.
   ```

**Project Structure**
   ```bash
   usdbrl-future-math/
   ├── app.py               # Flask backend
   ├── scheduler.py         # Periodic data fetching and calculations
   ├── streamlit_app.py     # Streamlit dashboard
   ├── data_fetcher_di.py   # Fetch DI data
   ├── data_fetcher_dolfuture.py  # Fetch mini-dollar futures
   ├── data_fetcher_dvdi.py  # Calculate working days to maturity
   ├── data_fetcher_usdbrl.py  # Fetch USD/BRL exchange rate
   ├── data_fetcher_usdx.py  # Fetch USDX data
   ├── math_operations.py   # Perform financial calculations
   ├── financial_data.db    # SQLite database
   ├── requirements.txt     # Python dependencies
   └── README.md            # Project documentation
   ```

