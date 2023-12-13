import pytest
from selenium import webdriver


browser: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup
    global browser
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(12)
    browser.get('https://www.saucedemo.com/') 

    # run test
    yield

    # teardown
    browser.quit()