import yaml
from module import Site
from time import sleep

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, result):
     
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
     
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    
    btn = site.find_element("css", btn_selector)
    btn.click()
    
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == result

    
def test_step2(x_selector1, x_selector2, btn_selector, hello_user):
     
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata['login'])
     
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()   
    input2.send_keys(testdata['passwd'])
    
    btn = site.find_element("css", btn_selector)
    btn.click()    
    
    sleep(3)
    element = site.find_element("xpath", hello_user)
    assert element.text == f"Hello, {testdata['login']}"


def test_step3(btn_create_post, x_selector4, x_selector5, x_selector6, btn_save_post, x_selector7, check_new_post):
    
    sleep(testdata["sleep_time"])
    
    button_create = site.find_element("xpath", btn_create_post)
    button_create.click()

    sleep(testdata["sleep_time"])

    input_title = site.find_element("xpath", x_selector4)
    input_title.send_keys(testdata["title_post"])

    input_des = site.find_element("xpath", x_selector5)
    input_des.send_keys(testdata["descr_post"])

    input_content = site.find_element("xpath", x_selector6)
    input_content.send_keys(testdata["content_post"])

    sleep(testdata["sleep_time"])

    btn_save = site.find_element("xpath", btn_save_post)
    btn_save.click()

    sleep(testdata["sleep_time"])

    check_title = site.find_element("xpath", x_selector7)
    assert check_title.text == check_new_post    


    site.close()
      