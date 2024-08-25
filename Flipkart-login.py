from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
import time

# Load the webpage

driver.get('https://www.flipkart.com')

#Click on the Login Button
driver.find_element(By.XPATH,"//div[@class='H6-NpN _3N4_BX']").click()

driver.find_element(By.XPATH,"//input[@class='r4vIwl BV+Dqf']").click()
driver.find_element(By.XPATH,"//input[@class='r4vIwl BV+Dqf']").send_keys('your mobile number')

#click on request OTP...
driver.find_element(By.XPATH,"//button[@class='QqFHMw twnTnD _7Pd1Fp']").click()

