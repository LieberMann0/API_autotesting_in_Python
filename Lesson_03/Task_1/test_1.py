import yaml
from time import sleep
from BaseApp import BasePage
from testpage import Operations

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata["username"]
passwd = testdata['password']

def test_step1(expected_result_1, browser):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_login()
    page.enter_pass()
    page.click_login_button()    
    assert page.get_error_text() == expected_result_1


# def test_step2(x_selector1, x_selector2, x_selector3, btn_selector, expected_result_2, hello_user, browser):

#     site = BasePage(browser)
     
#     input1 = site.find_element(x_selector1)
#     input1.clear()
#     input1.send_keys(testdata['login'])
     
#     input2 = site.find_element(x_selector2)
#     input2.clear()   
#     input2.send_keys(testdata['passwd'])
    
#     btn = site.find_element(btn_selector)
#     btn.click()    
    
#     sleep(3)
#     element = site.find_element(x_selector3)
#     assert element.text == expected_result_2
