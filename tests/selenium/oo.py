from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

class RegisterPage(BasePage):
    def open(self):
        self.driver.get("http://localhost:5173/register?redirect=/")

    def register_user(self, username, email, password, confirm_password):
        self.wait.until(EC.presence_of_element_located((By.ID, "name"))).send_keys(username)
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "confirmPassword").send_keys(confirm_password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)  # wait for redirect after registration

class LoginPage(BasePage):
    def open(self):
        self.driver.get("http://localhost:5173/login")

    def login_user(self, email, password):
        self.wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        # wait until redirected (React routing)
        self.wait.until(EC.url_contains("/"))

class LogoutPage(BasePage):
    def logout_user(self):
        try:
            logout_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Logout']")))
            logout_btn.click()
            time.sleep(1)
        except TimeoutException:
            print("Logout button not found, continuing...")

class CreateMoviePage(BasePage):
    def open(self):
        self.driver.get("http://localhost:5173/admin/movies/create")

    def create_movie(self, name, year, detail, cast, rating):
        self.wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(name)
        self.driver.find_element(By.NAME, "year").send_keys(str(year))
        self.driver.find_element(By.NAME, "detail").send_keys(detail)
        self.driver.find_element(By.NAME, "cast").send_keys(", ".join(cast))
        self.driver.find_element(By.NAME, "rating").send_keys(str(rating))
        self.driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()  # Create Movie button
        time.sleep(2)  # wait for success toast or redirect

# === Script Execution ===
driver = webdriver.Chrome()  # or path to chromedriver
driver.maximize_window()

try:
    # Register
    register = RegisterPage(driver)
    register.open()
    register.register_user("Shraddha Z", "shraddha@test.com", "123456", "123456")

    # Logout
    logout = LogoutPage(driver)
    logout.logout_user()

    # Login
    login = LoginPage(driver)
    login.open()
    login.login_user("shraddha@test.com", "123456")

    # Create Movie
    movie = CreateMoviePage(driver)
    movie.open()
    movie.create_movie(
        name="Avengers Endgame",
        year=2019,
        detail="Superheroes save the world",
        cast=["Robert Downey Jr.", "Chris Evans", "Scarlett Johansson"],
        rating=9.5
    )

finally:
    time.sleep(3)
    driver.quit()
