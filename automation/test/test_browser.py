from automation.browser.browser import BrowserSingleton
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class TestBrowser(unittest.TestCase):
    def test_build_successful(self):
        try:
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            browser = BrowserSingleton(driver)
            browser.go("https://github.com/")
            browser.html()
        except Exception as e:
            print(e)
            driver.close()
            raise Exception
        finally:
            driver.close()


unittest.main()
