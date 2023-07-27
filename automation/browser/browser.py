from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    InvalidElementStateException,
)
from html_parser.context_maker.semantics.base_semantic import Semantic
from exceptions.ElementRetrievalException import ElementRetrievalException
from html_parser.context_maker.semantics.base_page import Page


def refresh(func):
    def update_page(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        BrowserSingleton._page = Page(BrowserSingleton().html())
        return result

    return update_page


class BrowserSingleton:
    _instance = None
    _page = None

    def __new__(cls, driver=None):
        if not cls._instance:
            assert driver is not None
            cls._instance = super(BrowserSingleton, cls).__new__(cls)
            cls._instance._driver = driver
        return cls._instance

    @property
    def driver(self):
        return self._driver

    @refresh
    def go(self, url):
        self._driver.get(url)

    def html(self):
        self._driver.execute_script("return document.documentElement.outerHTML;")
        return self._driver.page_source

    def page(self):
        return BrowserSingleton._page

    def url(self):
        return self._driver.current_url
    
    def close(self):
        self._driver.close()

    def _webelement_from_semantic(self, semantic):
        try:
            if semantic.id is not None:
                return self._driver.find_element(By.ID, semantic.id)
        except NoSuchElementException:
            pass

        try:
            if semantic.name is not None:
                return self._driver.find_element(By.NAME, semantic.name)
        except NoSuchElementException:
            pass

        try:
            if semantic.classes is not None:
                for cls in semantic.classes:
                    return self._driver.find_element(By.CLASS_NAME, cls)
        except NoSuchElementException:
            pass

        try:
            if semantic.xpath is not None:
                return self._driver.find_element(By.XPATH, semantic.xpath)
        except NoSuchElementException:
            pass

        raise ElementRetrievalException(f"Could not find {semantic.tag}")

    @refresh
    def _scroll_check(self, webelement):
        self._driver.execute_script("arguments[0].scrollIntoView();", webelement)

    def refresh_page(self):
        html = self.html()
        BrowserSingleton._page = Page(html)

    @refresh
    def click(self, semantic):
        assert isinstance(semantic, Semantic)
        elem = self._webelement_from_semantic(semantic)
        self._scroll_check(elem)
        try:
            elem.click()
        except ElementNotInteractableException as e:
            pass
        except StaleElementReferenceException as e:
            pass
        except ElementClickInterceptedException as e:
            pass

    @refresh
    def type(self, semantic, content):
        assert isinstance(semantic, Semantic)
        elem = self._webelement_from_semantic(semantic)
        self._scroll_check(elem)
        try:
            elem.send_keys(content)
        except ElementNotInteractableException as e:
            pass
        except InvalidElementStateException as e:
            pass
        except StaleElementReferenceException as e:
            pass
