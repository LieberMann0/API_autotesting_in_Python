import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

    def find_element(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                          message=f"Can't find element by locator{locator}")
        except:
            logging.exception('Element not found')
            return None

    def get_element_property(self, locator, property):
        try:
            element = self.find_element(locator)
            return (element.value_of_css_property(property))
        except:
            logging.exception('Element property not found')
            return None

    def go_to_site(self):
        try:
            return self.driver.get(self.base_url)
        except:
            logging.exception('Page not found')
            return None
            