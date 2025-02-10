import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from .conftest import setup
import time


class Test_001_Login:
    baseUrl = "https://www.amazon.in/"
    username = "9019428682"
    password = "qwertyuiop!@#"

    def test_homepageTitle(self):
        self.driver = setup()
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            assert False


    def test_login(self):
        self.driver = setup()
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.lp.clickHello()
        time.sleep(5)
        self.lp.setUsername(self.username)
        time.sleep(5)
        self.lp.clickContinue()
        time.sleep(5)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title

        if act_title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            self.driver.close()
            assert False

    def test_logout(self):
        self.driver = setup()
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.lp.clickHello()
        time.sleep(3)
        self.lp.setUsername(self.username)
        time.sleep(5)
        self.lp.clickContinue()
        time.sleep(5)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(8)
        self.lp.clickAlldropdown()
        time.sleep(3)
        self.lp.clickSignout()
        time.sleep(3)
        act_title = self.driver.find_element(By.XPATH,"//h1[@class='a-size-medium-plus a-spacing-small']").text
        self.driver.quit()
        if act_title =="Sign in or create account":
            assert True
        else:
            assert False


