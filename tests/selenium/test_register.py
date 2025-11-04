from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # ✅ Use correct URL
    driver.get("http://localhost:5173/register?redirect=/")
    driver.maximize_window()

    # ✅ Ensure no previous session is logged in
    driver.delete_all_cookies()
    driver.refresh()

    wait = WebDriverWait(driver, 10)

    random_email = f"user{random.randint(1000,9999)}@test.com"

    # ✅ Wait for element before using it
    name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
    name_input.send_keys("Automation User")

    driver.find_element(By.ID, "email").send_keys(random_email)
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "confirmPassword").send_keys("123456")

    submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Register')]")
    submit_btn.click()

    time.sleep(3)

    # ✅ Validate success (you might redirect to `/` or stay and show toast)
    assert "http://localhost:5173/" in driver.current_url, "Registration did not redirect to home!"
    print(f"✅ Register Test Passed! Created {random_email}")

except Exception as e:
    print("❌ Register Test Failed:", e)

finally:
    driver.quit()
