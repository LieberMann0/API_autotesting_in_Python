import yaml
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
    page.enter_login('test')
    page.enter_pass('test')
    page.click_login_button()    
    assert page.get_error_text() == expected_result_1
