from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

#preparing browser option to prevent notifications
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})


var_driver = webdriver.Chrome(options=option)
var_driver.set_window_size(1280, 650)
var_driver.get('https://www.facebook.com')
#Before login
var_emailBox = var_driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
var_passwordBox = var_driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
var_loginButton = var_driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
var_emailBox.send_keys('sguha1988.life@gmail.com')
var_passwordBox.send_keys('agniicygel')
var_loginButton.click()

#after log in
var_seeMoreLinkXPath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div[1]/div/div[1]'
WebDriverWait(var_driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, var_seeMoreLinkXPath)))
var_seeMoreLink = var_driver.find_element_by_xpath(var_seeMoreLinkXPath)
var_seeMoreLink.click()

var_eventsLink = var_driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[3]/div/a/div[1]')
var_eventsLink.click()

var_birthDaysLinkXPath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div[2]/div[3]/a'
#WebDriverWait(var_driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, var_birthDaysLinkXPath)))
var_birthDaysLink = var_driver.find_element_by_xpath(var_birthDaysLinkXPath)
var_birthDaysLink.click()