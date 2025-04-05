from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)

driver.get("https://www.thenexusof.ai")

active_users = driver.find_element(By.XPATH ,value = '//*[@id="__next"]/main/div/div/div[2]/div/textarea')
active_users.send_keys("anime waifu", Keys.ENTER)
sign_in = driver.find_element(By.XPATH , value ='//*[@id="__next"]/main/div/div[2]/div/div/button')
sign_in.click()

time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])

email = driver.find_element(By.XPATH , value = '//*[@id="__next"]/main/div/div/div[2]/div[1]/div[1]/input')
email.send_keys("muhammadhussain.mh512@gmail.com")
password = driver.find_element(By.XPATH , value = '//*[@id="__next"]/main/div/div/div[2]/div[1]/input')
password.send_keys("123321")
login = driver.find_element(By.XPATH, value= '//*[@id="__next"]/main/div/div/div[2]/div[2]/button[2]')
login.click()