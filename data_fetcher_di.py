from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fetch_di_value():
    # Define the WebDriver service and options
    service = Service()  # Add the path to your ChromeDriver if needed
    options = webdriver.ChromeOptions()

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=options)

    # Define the URL to navigate to
    url = 'https://www.infomoney.com.br/ferramentas/juros-futuros-di/'
    driver.get(url)

    try:
        # Wait for the table element to be present on the page
        table_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="contratos_di_futuro"]/tbody/tr[1]/td[3]'))
        )
        # Extract the text from the table cell
        value = table_element.text
        driver.quit()
        return float(value.replace(",", "."))
        
    except Exception as e:
        driver.quit()
        raise e