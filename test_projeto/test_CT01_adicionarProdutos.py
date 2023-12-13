import conftest
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_CT01_adicionar(self):
        browser = conftest.browser
        #faz loguin no site
        browser.find_element(By.ID, 'user-name' ).send_keys('standard_user')
        browser.find_element(By.ID, 'password').send_keys('secret_sauce')
        browser.find_element('xpath', '//*[@id="login-button"]').click()

        #clica no produto
        browser.find_element('xpath', '//*[@id="item_0_title_link"]/div').click()
        #adiciona ao carrinho
        browser.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        #clica no carrinho
        browser.find_element('xpath', '//*[@id="shopping_cart_container"]/a').click()
        #volta para produtos
        browser.find_element('xpath', '//*[@id="continue-shopping"]').click()
        #clica no produto
        browser.find_element('xpath', '//*[@id="item_4_title_link"]/div').click()
        #adiciona ao carrinho
        browser.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        #clica no carrinho
        browser.find_element('xpath', '//*[@id="shopping_cart_container"]/a').click()

        #verifica se os dois produtos estão no carrinho
        assert browser.find_element('xpath', '//*[@id="item_0_title_link"]/div').is_displayed()
        assert browser.find_element('xpath', '//*[@id="item_4_title_link"]/div').is_displayed()