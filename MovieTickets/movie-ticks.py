from selenium import webdriver
from decouple import config

import time

# cmd+shift+c

driver = webdriver.Chrome("/usr/bin/chromedriver")
# driver.get(config('THEATRE_SITE'))
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
# button = driver.find_element_by_xpath("/html/....")
# button.click()
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()