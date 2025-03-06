from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()

# Open the website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait until username input field is visible
wait = WebDriverWait(driver, 10)

# Locate username and password fields and enter credentials
username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username.send_keys("Admin")

password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys("admin123")

# Locate and click login button
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
button.click()

# Wait until the dashboard header is visible
act_title_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
act_title = act_title_element.text  # Extract actual text

expected_title = "Dashboard"

# Print actual and expected titles
print(f"Actual Title: {act_title}")
print(f"Expected Title: {expected_title}")


if(act_title == expected_title):
    print("Login test passed")
else:
    print("Login test failed")

# Pause for review before quitting
time.sleep(5)
driver.quit()


