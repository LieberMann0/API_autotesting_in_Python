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
    

    site.close()
      