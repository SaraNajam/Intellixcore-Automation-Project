import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver (using WebDriverManager to manage driver installation)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the sign-up page
driver.get("https://app.intellixcore.ai/auth/login")

try:
    wait = WebDriverWait(driver, 10)
    
    # Locate and fill in the email
    email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"].MuiInputBase-input')))
    email.send_keys('sara.najam@iqeqdigital.com')
    
    # Locate and fill in the password
    password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"].MuiInputBase-inputAdornedEnd')))
    password.send_keys('Sara@1234')
    
    # Locate and click the sign-in button
    sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.MuiButton-containedPrimary')))
    sign_in_button.click()

    # Check if the current URL matches the expected URL after login
    expected_url = "https://app.intellixcore.ai/dashboard"
    WebDriverWait(driver, 50).until(EC.url_to_be(expected_url))
    print("Login successful. Redirected to the dashboard.")

except TimeoutException:
    print("Login failed or URL did not match the expected URL after login.")

finally:
    # Close the WebDriver after some time or conditions
    driver.quit()
