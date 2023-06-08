import logging
import time
from testpage import Operations

def test_step1(expected_result_1, browser):
    logging.info('Test1 Starting')
    site = Operations(browser)
    site.go_to_site()    
    site.enter_login('test')
    site.enter_pass('test')
    site.click_login_button()    
    assert site.get_error_text() == expected_result_1


def test_step2(browser, check_enter):
    logging.info("Test2 Starting")
    testpage = Operations(browser)
    testpage.go_to_site()
    testpage.enter_login("10061")
    testpage.enter_pass("7fe3d16a83")
    testpage.click_login_button()
    assert testpage.check_enter_user() == check_enter


def test_step3(browser, form_title):
    logging.info("Test3 Starting")
    testpage = Operations(browser)
    testpage.button_contact()
    time.sleep(3)
    assert testpage.check_open_form() == form_title


def test_step4(browser, alert_text):
    logging.info("Test4 Starting")
    testpage = Operations(browser)
    testpage.button_contact()
    testpage.input_form_name("Your name")
    testpage.input_form_email("test@email.ru")
    testpage.input_form_content("Enter your content")
    testpage.contact_us_btn()
    time.sleep(3)
    assert testpage.check_alert_text() == alert_text
