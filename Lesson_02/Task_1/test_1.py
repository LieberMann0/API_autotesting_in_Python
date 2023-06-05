import yaml
from module import Site

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

    site.close()
    