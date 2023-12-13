from selenium.webdriver.common.by import By
import time
import conftest 
import pytest

@pytest.mark.usefixtures("setup_teardown")
class TesteLoguin:    
    def test_loguin(self):
        browser = conftest.browser
        browser.find_element(By.ID, 'user-name' ).send_keys('standard_user')
        browser.find_element(By.ID, 'password').send_keys('secret_sauce')
        browser.find_element('xpath', '//*[@id="login-button"]').click()

        assert (browser.find_element('xpath', '//*[@id="header_container"]/div[2]/span')).is_displayed()






