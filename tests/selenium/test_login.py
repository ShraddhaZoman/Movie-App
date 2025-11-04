from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the Login page
    driver.get("http://localhost:5173/login")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Wait until the email input is visible
    email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
    password_input = driver.find_element(By.ID, "password")
    submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]")

    # ✅ Enter login credentials (use a user already registered)
    email_input.send_keys("admin@gmail.com")
    password_input.send_keys("admin")

    # Click Sign In
    submit_btn.click()

    # Wait a few seconds for redirect after login
    time.sleep(3)

    # Validate if login succeeded (you can adjust based on your redirect)
    if driver.current_url != "http://localhost:5173/login":
        print("✅ Login Test Passed!")
    else:
        print("❌ Login Test Failed: Stayed on login page")

except Exception as e:
    print("❌ Login Test Failed:", e)

finally:
    driver.quit()

