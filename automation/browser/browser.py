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


class BrowserSingleton:
    _instance = None

    def __new__(cls, driver, judge):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._driver = driver
            cls._instance._judge = judge
        return cls._instance

    @property
    def driver(self):
        return self._driver

    @property
    def judge(self):
        return self._judge

    def go(self, url):
        self._driver.get(url)

    def html(self):
        self._driver.execute_script("return document.documentElement.outerHTML;")
        return self._driver.page_source

    def close(self):
        self._driver.close()

    def _webelement_from_semantic(self, semantic):
        try:
            if semantic.xpath is not None:
                return self._driver.find_element(By.XPATH, semantic.xpath)
        except NoSuchElementException as e:
            pass

        try:
            unique_id = ""
            if semantic.id is not None:
                unique_id += f"#{semantic.id}"
            if semantic.name is not None:
                unique_id += f"[name={semantic.name}]"
            if semantic.classes is not None:
                for cls in semantic.classes:
                    unique_id += f".{cls}"
            return self._driver.find_element(By.CSS_SELECTOR, unique_id)
        except NoSuchElementException as e:
            pass

        raise ElementRetrievalException(f"could not find {semantic.tag}")

    def _scroll_check(self, webelement):
        self._driver.execute_script("arguments[0].scrollIntoView();", webelement)

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
