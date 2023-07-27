from selenium import webdriver
from automation.browser.browser import BrowserSingleton
from automation.driver.driver import Driver
from automation.judge.judge import Judge

driver = webdriver.Firefox()
browser = BrowserSingleton(driver=driver)
judge = Judge("create an account on github with email bobross123@gmail.com and password fsbfsaifbsauibBBB1111")
entry_point = "https://github.com/"

driver = Driver(browser=browser, judge=judge, entry_point=entry_point)
driver.start()
