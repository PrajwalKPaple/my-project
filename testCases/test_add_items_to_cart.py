import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from .conftest import setup
import time
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import LogGen
from pageObjects.CartPage import CartPage




# // this is my code
class Test_002_Cart:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_add_Shoe_to_cart(self):
        self.logger.info("********************* TEST 005 STARTED **************************")
        self.driver = setup()
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.cp=CartPage(self.driver)
        self.lp.clickHello()
        self.lp.setUsername(self.username)
        self.lp.clickContinue()
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.cp.clicksearchinput()
        self.cp.clicksearchbutton()
        self.cp.clickaddtocart()
        time.sleep(5)
        self.cp.clickconfirmationaddtocart()
        alert = self.driver.switch_to.alert
        alert_message = alert.text
        print(alert_message)
        if alert_message == "Item Added":
            self.logger.info("********************* TEST PASSED ************************")
            assert True
        else:
            self.logger.info("********************* TEST FAILED ************************")
            assert False

    def test_add_Bottle_to_cart(self):
        self.logger.info("********************* TEST 006 STARTED **************************")
        self.driver = setup()
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.cp=CartPage(self.driver)
        self.lp.clickHello()
        self.lp.setUsername(self.username)
        self.lp.clickContinue()
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.cp.clicksearchinput1()
        self.cp.clicksearchbutton()
        self.cp.clickaddtocart()
        time.sleep(5)
        self.cp.clickconfirmationaddtocart()
        alert = self.driver.switch_to.alert
        alert_message = alert.text
        print(alert_message)
        if alert_message == "Item Added":
            self.logger.info("********************* TEST PASSED ************************")
            assert True
        else:
            self.logger.info("********************* TEST FAILED ************************")
            assert False





