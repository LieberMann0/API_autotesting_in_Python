from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestLocators:
    x_selector1 = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")

    x_selector2 = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")

    x_selector3 = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")

    btn_selector = (By.CSS_SELECTOR, "button")

    hello_user = (By.XPATH, """/*[@id="app"]/main/nav/ul/li[3]/a""")


class Operations(BasePage, TestLocators):

    def enter_login(self):
        logging.info('Enter login ')
        input1 = self.find_element(self.x_selector1)
        input1.send_keys("test")


    def enter_pass(self):
        logging.info('Enter password ')
        input2 = self.find_element(self.x_selector2)
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
    