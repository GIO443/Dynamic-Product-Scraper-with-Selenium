import os
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up headless browser
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Create the ChromeDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Load the local HTML file
mock_path = os.path.abspath("mock_store/mock_store.html")
driver.get(f"file://{mock_path}")
time.sleep(1)  # allow JS to render products

# Find and extract product data
products = driver.find_elements(By.CLASS_NAME, "product")
results = []

for product in products:
    try:
        title = product.find_element(By.CLASS_NAME, "item-title").text
        price = product.find_element(By.CLASS_NAME, "price").text
        shipping = product.find_element(By.CLASS_NAME, "shipping").text
        link = product.find_element(By.CLASS_NAME, "item-title").get_attribute("href")
        results.append([title, price, shipping, link])
    except Exception as e:
        print("Skipping product due to error:", e)

# Save results to CSV
with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Shipping", "Link"])
    writer.writerows(results)

driver.quit()
print(f"Scraped {len(results)} products successfully.")
