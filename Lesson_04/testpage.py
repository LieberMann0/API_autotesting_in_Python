from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)

    for i in locators['xpath'].keys():
        ids[i] = (By.XPATH, locators['xpath'][i])

    for i in locators['css'].keys():
        ids[i] = (By.CSS_SELECTOR, locators['css'][i])


class Operations(BasePage, TestLocators):
    with open('testdata.yaml') as f:
        info = yaml.safe_load(f)

    def enter_bad_login(self):
        logging.debug('Enter login ')
        input1 = self.find_element(self.ids['x_selector1'])
        if input1:
            input1.send_keys(self.info['bad_login'])
        else:
            logging.error('The login field was not found')

    def enter_bad_pass(self):
        logging.debug('Enter password ')
        input2 = self.find_element(self.ids['x_selector2'])
        if input2:
            input2.send_keys(self.info['bad_login'])
        else:
            logging.error('The password field was not found')

    def enter_good_login(self):
        logging.debug('Enter login ')
        input1 = self.find_element(self.ids['x_selector1'])
        if input1:
            input1.send_keys(self.info['username'])
        else:
            logging.error('The login field was not found')

    def enter_good_pass(self):
        logging.debug('Enter password ')
        input2 = self.find_element(self.ids['x_selector2'])
        if input2:
            input2.send_keys(self.info['password'])
        else:
            logging.error('The password field was not found')

    def click_login_button(self):
        logging.debug('Click login button ')
        btn = self.find_element(self.ids['btn_selector'])
        if btn:
            btn.click()
        else:
            logging.error('Button not found')

    def get_error_text(self):
        err_label = self.find_element(self.ids['x_selector3'])
        if err_label:
            text = err_label.text
            logging.debug(f'Error {text} while loging')
            return text
        else:
            logging.error('The element with the error was not found')
            return None

    def get_hello_user(self):
        hello = self.find_element(self.ids['x_selector4'])
        if hello:
            text = hello.text
            logging.info(text)
            return text
        else:
            logging.error('The user has not logged in')
            return None

    def click_contact_button(self):
        logging.debug('Click contact button ')
        cont_btn = self.find_element(self.ids['contact_btn'])
        if cont_btn:
            cont_btn.click()
        else:
            logging.error('The contact button was not found')

    def enter_name(self):
        logging.debug('Enter name ')
        name_field = self.find_element(self.ids['name_field'])
        if name_field:
            name_field.send_keys(self.info['name'])
        else:
            logging.error('The field for entering the name was not found')

    def enter_email(self):
        logging.debug('Enter email ')
        email_field = self.find_element(self.ids['email_field'])
        if email_field:
            email_field.send_keys(self.info['email'])
        else:
            logging.error('The field for entering the email was not found')

    def enter_content(self):
        logging.debug('Enter content ')
        content_field = self.find_element(self.ids['content_field'])
        if content_field:
            content_field.send_keys(self.info['content'])
        else:
            logging.error('The content input field was not found')

    def click_contact_us_button(self):
        logging.debug('Click contact us button ')
        cont_us_btn = self.find_element(self.ids['contact_us_btn'])
        if cont_us_btn:
            cont_us_btn.click()
        else:
            logging.error('The contact us button was not found')

    def switch_alert(self):
        logging.info("Switch alert")
        text = self.alert()
        logging.info(text)
        return text
