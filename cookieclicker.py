from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = chrome_options)

driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID , value='cookie')
money = driver.find_element(By.ID , value = 'money')
money = money.text
store = driver.find_element(By.XPATH, value = '//*[@id="buyCursor"]/b')
# print([i.text for i in store])
print(store.text)
# i =0
# while i<1000:

#     cookie.click()