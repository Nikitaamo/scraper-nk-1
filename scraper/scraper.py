from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# Configure logging
logging.basicConfig(filename='main.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Setup ChromeDriver
service = Service('/usr/local/bin/chromedriver')  # Make sure this path is correct
driver = webdriver.Chrome(service=service)


# Navigate to the website with filters applied
driver.get('https://www.cvbankas.lt/?padalinys%5B%5D=76&keyw=data+science')

# Use an explicit wait to make sure the page and elements are loaded
wait = WebDriverWait(driver, 10)

# Get the total number of job listings to iterate through
total_listings = len(driver.find_elements(By.CSS_SELECTOR, 'div.list_cell'))

# Iterate through each job listing by index
for index in range(total_listings):
    # Wait for the job listings to appear and then find them again to avoid stale references
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.list_cell')))
    job_listings = driver.find_elements(By.CSS_SELECTOR, 'div.list_cell')

    # Click the job listing
    try:
        # Use an explicit wait to wait for the specific job listing to be clickable
        wait.until(EC.element_to_be_clickable(job_listings[index]))
        job_listings[index].click()
    except Exception as e:
        # If normal click doesn't work, use JavaScript to click
        driver.execute_script("arguments[0].click();", job_listings[index])
        logging.info(f"Clicked job listing via JavaScript due to exception: {e}")

    # Wait for the job detail page to load and scrape data
    # ... (scrape the data as before) ...

    # Navigate back to the listings page
    driver.back()

    # Wait for the listings page to load before continuing to the next listing
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.list_cell')))

# Close the browser when done
driver.quit()
