from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml
import subprocess
import requests

with open("locators.yaml") as f:
    locators = yaml.safe_load(f)

with open("testdata.yaml") as f2:
    user_set = yaml.safe_load(f2)


class TestSearchLocators:
    ids = dict()
    for i in locators['xpath'].keys():
        ids[i] = (By.XPATH, locators['xpath'][i])
    for i in locators['css'].keys():
        ids[i] = (By.CSS_SELECTOR, locators['css'][i])


class Operations(BasePage):
    def enter_login(self, word):
        logging.debug(f"Send {word} to element {TestSearchLocators.ids['LOCATOR_LOGIN_FIELD']}")
        login_field = self.find_element(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'])
        if login_field:
            login_field.clear()
            login_field.send_keys(word)
        else:
            logging.error('Field Login not found')


    def enter_pass(self, word):
        logging.debug(f"Send {word} to element {TestSearchLocators.ids['LOCATOR_PASS_FIELD']}")
        password_field = self.find_element(TestSearchLocators.ids['LOCATOR_PASS_FIELD'])
        if password_field:
            password_field.clear()
            password_field.send_keys(word)
        else:
            logging.error('Field Password not found')


    def click_login_button(self):
        logging.debug("Click login button")
        btn = self.find_element(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'])
        if btn:
            btn.click()
        else:
            logging.error('Button Login not found')


    def click_about_button(self):
        logging.debug("Click about link")
        btn = self.find_element(TestSearchLocators.ids['LOCATOR_ABOUT'])
        if btn:
            btn.click()
        else:
            logging.error('Error click about link')


    def get_font(self):
        about_page_field = self.find_element(TestSearchLocators.ids['LOCATOR_ABOUT_PAGE'], time=3)
        if about_page_field:
            font = about_page_field.value_of_css_property('font-size')
            logging.debug(f"We find '{font}' in error field {TestSearchLocators.ids['LOCATOR_ABOUT_PAGE']}")
            return font
        else:
            logging.error('Error header about page not found')
            return None


    def get_profile(self, token):
        response = requests.get(f"{user_set['users']}/{user_set['id']}", headers={'X-Auth-Token': token})
        return response.json()['userName']


    def get_nikto(self, cmd, answer):
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        out = result.stdout
        if answer in out:
            return True
        else:
            logging.error('Error. site dont return code')
            return False

    
    