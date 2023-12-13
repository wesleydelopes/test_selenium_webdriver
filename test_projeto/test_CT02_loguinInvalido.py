from selenium.webdriver.common.by import By
import time
import conftest
import pytest


@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_CT02_loguininvalido(self):
        #faz loguin no site
        browser = conftest.browser
        browser.find_element(By.ID, 'user-name' ).send_keys('000')
        browser.find_element(By.ID, 'password').send_keys('000')
        browser.find_element(By.ID, 'login-button').click()
        assert (browser.find_element(By.ID, 'login-button')).is_displayed()



