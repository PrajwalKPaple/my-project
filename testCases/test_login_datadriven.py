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
from utilities import XLutils


class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".//testData/Test Credientials.xlsx"

    logger = LogGen.loggen()

    def test_login(self):
        self.driver = setup()
        self.logger.info("****************************** TEST 004 STARTED********************************")
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver,)
        self.lp.clickHello()
        self.rows = XLutils.getRowCount(self.path,"Sheet1")
        print("Number of rows in the excel:",self.rows)

        list_status=[]

        for r in range(2, self.rows+1):
            self.user = XLutils.readData(self.path,"Sheet1",r,1)
            self.password = XLutils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLutils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUsername(self.user)
            self.lp.clickContinue()
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            act_title = self.driver.title
            exp_title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"

            if act_title== exp_title:
                if self.exp == "PASS":
                    self.lp.clickSignout()
                    list_status.append("PASS")
                elif self.exp == "FAIL":
                    self.lp.clickSignout()
                    list_status.append("FAIL")

            elif act_title != exp_title:
                if self.exp == "PASS":
                    self.lp.clickSignout()
                    list_status.append("FAIL")
                elif self.exp == "FAIL":
                    self.lp.clickSignout()
                    list_status.append("PASS")

        if "FAIL" not in list_status:
            print("Test Passed")
            self.logger.info("****************************** TEST PASSED********************************")
            assert True
        else:
            self.driver.close()
            self.logger.info("****************************** TEST FAILED********************************")
            assert False











