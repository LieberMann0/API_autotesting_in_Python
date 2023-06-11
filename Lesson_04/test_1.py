import yaml
import time
from BaseApp import BasePage
from testpage import Operations

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata["username"]
passwd = testdata["password"]


def test_step1(err_401, browser):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_bad_login()
    page.enter_bad_pass()
    page.click_login_button()
    assert page.get_error_text() == err_401


def test_step2(hello_user, browser, alert_text):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_good_login()
    page.enter_good_pass()
    page.click_login_button()
    # SendMail()
    assert page.get_hello_user() == hello_user
    page.click_contact_button()
    time.sleep(3)
    page.enter_name()
    page.enter_email()
    page.enter_content()
    time.sleep(3)
    page.click_contact_us_button()
    time.sleep(3)
    assert page.alert() == alert_text
    