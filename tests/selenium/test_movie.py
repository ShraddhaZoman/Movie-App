from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# --- Setup Chrome ---
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

try:
    # --- Go to login page ---
    driver.get("http://localhost:5173/login")
    time.sleep(2)

    # --- Login first (admin user) ---
    driver.find_element(By.ID, "email").send_keys("admin@gmail.com")  # Replace with admin email
    driver.find_element(By.ID, "password").send_keys("admin")   # Replace with admin password
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)

    # --- Go to Create Movie page ---
    driver.get("http://localhost:5173/admin/movies/create")
    time.sleep(2)

    # --- Fill form ---
    driver.find_element(By.NAME, "name").send_keys("Test Movie")
    driver.find_element(By.NAME, "year").send_keys("2025")
    driver.find_element(By.NAME, "detail").send_keys("This is a test movie description.")
    driver.find_element(By.NAME, "cast").send_keys("Actor 1, Actor 2")

    # --- Select genre ---
    genre_select = Select(driver.find_element(By.NAME, "genre"))
    genre_select.select_by_index(1)  # selects second genre in list

    # --- Upload image ---
    driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys("C:\\Users\\shrad\\OneDrive\\Pictures\\beautiful-flowers-lotus.webp")  # Update path

    # --- Click Create Movie ---
    driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()

    time.sleep(5)  # wait for submission & toast

    print("✅ Create Movie Test Completed Successfully")

except Exception as e:
    print("❌ Create Movie Test Failed:", e)

finally:
    driver.quit()
