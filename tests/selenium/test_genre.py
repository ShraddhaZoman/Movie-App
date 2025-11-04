from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# --- Setup Chrome ---
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

try:
    # --- Login first (admin) ---
    driver.get("http://localhost:5173/login")
    time.sleep(2)
    driver.find_element(By.ID, "email").send_keys("admin@gmail.com")  # Replace with admin email
    driver.find_element(By.ID, "password").send_keys("admin")   # Replace with admin password
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)

    # --- Go to Genre Management page ---
    driver.get("http://localhost:5173/admin/movies/genre")
    time.sleep(2)

    # --- CREATE Genre ---
    driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("Test Genre")
    driver.find_element(By.CSS_SELECTOR, "form button[type='submit']").click()
    time.sleep(2)
    print("✅ Genre creation attempted")

    # --- UPDATE Genre ---
    genre_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Test Genre')]")
    genre_button.click()
    time.sleep(1)

    # Clear input and type new name
    modal_input = driver.find_element(By.CSS_SELECTOR, ".modal input[type='text']")
    modal_input.clear()
    modal_input.send_keys("Updated Test Genre")
    driver.find_element(By.CSS_SELECTOR, ".modal button[type='submit']").click()
    time.sleep(2)
    print("✅ Genre update attempted")

    # --- DELETE Genre ---
    driver.find_element(By.CSS_SELECTOR, ".modal button[text()='Delete']").click()
    time.sleep(2)
    print("✅ Genre deletion attempted")

except Exception as e:
    print("❌ Genre Test Failed:", e)

finally:
    driver.quit()
