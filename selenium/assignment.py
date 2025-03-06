from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login")

driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input").clear()
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input").send_keys("admin@yourstore.com")


driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/div/input").clear()
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/div/input").send_keys("admin")


driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()


act_output = driver.find_element(By.XPATH,"/html/body/div[1]/div/p").text
expected_output = 'Verifying you are human. This may take a few seconds.'


# time.sleep(6)

# driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div//iframe").click()

print(act_output)
print(expected_output)

if act_output == expected_output:
    print("Test case passed")
else:
    print("test case failed.")

time.sleep(60)
driver.close()