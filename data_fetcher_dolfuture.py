from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

def get_current_contract():
    # Month letters for futures contracts
    month_letters = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z']

    # Get current year and month
    now = datetime.now()
    current_month = now.month
    current_year = now.year

    # Move to the next month
    next_month = current_month + 1
    
    # Handle year rollover
    if next_month > 12:
        next_month = 1
        current_year += 1

    # Determine the contract month letter
    month_letters = month_letters[next_month - 1] #Zero-based index

    #Build the contract code
    current_contract = f"DOL{month_letters}{current_year}"

    return current_contract

def fetch_dolfuture_value():
    contract = get_current_contract()
    
    # Instance the WebDriver
    service = Service()

    # Define the preferenced browser - Chrome option
    options = webdriver.ChromeOptions()

    # Start the instance with the browser
    driver = webdriver.Chrome(service=service, options=options)

    url = f'https://br.tradingview.com/symbols/BMFBOVESPA-DOL1!/?contract={contract}'
    driver.get(url)

    # Wait for the element to be present on the page
    time.sleep(5) 

     # Locate and fetch the value
    try:
        element = driver.find_element(By.XPATH, '//*[@id="js-category-content"]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]/span')
        value = element.text

        # Format the value to ensure it's a valid float
        formatted_value = value.replace(".", "").replace(",", ".")
        print(f"Value for {contract}: {float(formatted_value)}")
    except Exception as e:
        print(f"Error fetching data for {contract}: {e}")
    finally:
        # Close the browser
        driver.quit()

    return float(formatted_value)

