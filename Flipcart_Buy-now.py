# In this we will write test cases for Flipcart Login Page

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
import time

driver.get('https://www.flipkart.com/') #opening Flipcart

#now add implicitly wait for 2 seconds
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//input[@class='Pke_EE']").click()  #click on the search bar
driver.find_element(By.XPATH, "//input[@class='Pke_EE']").send_keys('mobile') #Serach for the 'mobile'
    
#add 10sec implicit wait
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//div[@class='_3idirA']").click() #it will click on the first search suggestion element

#click on the product 
print(driver.window_handles)      
driver.find_element(By.XPATH, "//div[(text()='Apple iPhone 15 (Blue, 128 GB)')]").click() # click on the Apple iPhone 15 (Blue, 128 GB)
driver.implicitly_wait(5)

print(driver.window_handles) 
driver.switch_to.window(driver.window_handles[1])  # driver will switch to the new window

time.sleep(2)

driver.find_element(By.XPATH,"//li[@class='col col-6-12 flex']").click()
print("clicked on buy now")

# Wait for 2 seconds
time.sleep(2)

# get the current title of new window
print(driver.title)
# expected title of new window should be "Apple iPhone 15 (Blue, 128 GB) | Flipkart"
driver.quit()

print("All test cases passed!!!!!")
