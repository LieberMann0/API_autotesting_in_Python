from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestLocators:
    x_selector1 = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    x_selector2 = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    x_selector3 = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    btn_selector = (By.CSS_SELECTOR, "button")
    hello_user = (By.XPATH, """/*[@id="app"]/main/nav/ul/li[3]/a""")
    contact_btn = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    title_form = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    form_name_input = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    form_email_input = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    form_content_input = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    btn_contact_us = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")

class Operations(BasePage, TestLocators):

    def enter_login(self):
        logging.info('Enter login ')
        input1 = self.find_element(self.x_selector1)
        input1.clear()
        input1.send_keys("test")


    def enter_pass(self):
        logging.info('Enter password ')
        input2 = self.find_element(self.x_selector2)
        input2.clear()
        input2.send_keys("test")


    def click_login_button(self):
        logging.info('Click button ')
        btn = self.find_element(self.btn_selector)
        btn.click()


    def get_error_text(self):        
        err_label = self.find_element(self.x_selector3)
        error_text = err_label.text
        logging.info(f'Error {error_text} ')
        return error_text


    def check_enter_user(self):
        open_page = self.find_element(self.hello_user)
        name_user = open_page.text
        return name_user


    def button_contact(self):
        self.find_element(self.contact_btn).click()


    def check_open_form(self):
        open_form = self.find_element(self.title_form)
        form_text = open_form.text
        return form_text


    def input_form_name(self, text):
        input_login = self.find_element(self.form_name_input)
        input_login.send_keys(text)


    def input_form_email(self, text):
        input_login = self.find_element(self.form_email_input)
        input_login.send_keys(text)


    def input_form_content(self, text):
        input_login = self.find_element(self.form_content_input)
        input_login.send_keys(text)

    
    def contact_us_btn(self):
        self.find_element(self.btn_contact_us).click()


    def check_alert_text(self):
        try:
            alert_text = self.driver.switch_to.alert.text
            return alert_text
        except:
            return None
