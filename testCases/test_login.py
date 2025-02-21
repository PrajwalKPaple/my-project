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


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homepageTitle(self):
        self.logger.info("********************* TEST 001 STARTED ************************")
        self.driver = setup()
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in":
            assert True
            self.driver.close()
            self.logger.info("********************* HOMEPAGE TITLE TEST PASSED ************************")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.info("********************* HOMEPAGE TITLE TEST FAILED ************************")
            assert False


    def test_login(self):
        self.logger.info("********************* TEST 002 STARTED **************************")
        self.driver = setup()
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.lp.clickHello()
        self.lp.setUsername(self.username)
        self.lp.clickContinue()
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in":
            assert True
            self.driver.close()
            self.logger.info("********************* LOGIN TEST PASSED ************************")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.info("********************* HOMEPAGE TITLE TEST FAILED ************************")
            assert False

    def test_logout(self):
        self.logger.info("********************* TEST 003 STARTED  ************************")
        self.driver = setup()
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.lp.clickHello()
        self.lp.setUsername(self.username)
        self.lp.clickContinue()
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickAlldropdown()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.lp.clickSignout()
        act_title = self.lp.capturelogoutpagetitle().text
        self.driver.quit()
        if act_title =="Sign in or create account":
            self.logger.info("********************* LOGOUT TEST PASSED ************************")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_logout.png")
            self.logger.info("********************* LOGOUT TEST FAILED ************************")
            assert False


