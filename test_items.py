import pytest
import time
 
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_have_button(browser):
    browser.get(link)
    #time.sleep(30)
    button = browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(button) == 1, f"Button not found!"
    
    
   


