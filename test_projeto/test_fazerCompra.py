import conftest
import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures("setup_teardown")
class TestFazerCompra:
    def test_fazerCompra(self):


        #faz loguin no site
        browser = conftest.browser
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

        #inicia compra de dois produtos
        browser.find_element('xpath', '//*[@id="checkout"]').click()
        #primeiro nome
        browser.find_element('xpath', '//*[@id="first-name"]').send_keys('wesley')
        #segundo nome
        browser.find_element('xpath', '//*[@id="last-name"]').send_keys('lopes')
        #cep
        browser.find_element('xpath', '//*[@id="postal-code"]').send_keys('00000000')
        #avança
        browser.find_element('xpath', '//*[@id="continue"]').click()
        #avança
        browser.find_element('xpath', '//*[@id="finish"]').click()

        assert (browser.find_element('xpath', '//*[@id="header_container"]/div[2]/span')).is_displayed()


