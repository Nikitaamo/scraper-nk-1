from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import logging

# Configure logging
logging.basicConfig(filename='main.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Setup ChromeDriver
service = Service('/path/to/chromedriver')  # Update the path to where you have downloaded chromedriver
driver = webdriver.Chrome(service=service)

# Navigate to the website with filters applied
driver.get('https://www.cvbankas.lt/?padalinys%5B%5D=76&keyw=data+science')

# Wait for page to load (adjust the time as necessary)
time.sleep(5)

# Find all job listing elements
job_listings = driver.find_elements(By.CSS_SELECTOR, 'div.list_cell')

# Loop through listings and collect data
for job in job_listings:
    # Navigate to job detail page
    job.click()
    time.sleep(3)  # Wait for the detail page to load

    # Scrape data from job detail page
    job_title = driver.find_element(By.CSS_SELECTOR, 'h1').text
    location_and_company = driver.find_element(By.CSS_SELECTOR, 'div#jobad_location').text
    views = driver.find_element(By.CSS_SELECTOR, 'div.jobad_stat strong').text

    # Log the scraped data
    logging.info(f'Job Title: {job_title}, Location and Company: {location_and_company}, Views: {views}')

    # Navigate back to the listings page
    driver.back()
    time.sleep(3)

# Close the browser when done
driver.quit()
