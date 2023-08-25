from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''to open the URL'''
driver = webdriver.Chrome()
'''to maximize the URL'''
driver.maximize_window()                 
driver.get("https://www.amazon.in/")
print("application title is",driver.title)
print("application url is",driver.current_url)


'''click for sign in'''
driver.find_element(By.ID,"nav-link-accountList-nav-line-1").click()
time.sleep(2)   # time.sleep can be use for pause the action for the given time(in second)


"""for existing user"""
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("8976******")   # you can add the email id also
driver.find_element(By.XPATH,"//span[@id='continue']")
time.sleep(2)


"""for new user"""
driver.find_element(By.ID,"createAccountSubmit").click()    #click on -create your amazon account
time.sleep(2)
# start filling the form here
driver.find_element(By.CSS_SELECTOR, "[placeholder='First and last name']").send_keys("your name") 
driver.find_element(By.CLASS_NAME,"a-dropdown-prompt")
driver.find_element(By.XPATH,"//input[@type='tel']").send_keys("8976******")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("****@gmail.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("**password**")
driver.find_element(By.XPATH,"//input[@type='submit']").click()     # your account is successfuully created
time.sleep(2)


'''click for set the location'''
driver.find_element(By.ID,"nav-global-location-popover-link").click()
driver.find_element(By.ID,"GLUXZipUpdateInput").send_keys("56****")    # enter 6 digit pincode
driver.find_element(By.XPATH,"//span[text()='Apply']").click()     # your location is updated



'''for search something'''
driver.find_element(By.XPATH,"//input[@type='text']").click()


'''for go to the order or return page'''
driver.find_element(By.ID,"nav-orders").click()