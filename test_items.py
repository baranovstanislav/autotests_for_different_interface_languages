import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/' 
def test_check_button(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert len(button), "Such button doesn't exist"