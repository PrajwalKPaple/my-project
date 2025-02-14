from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    button_hello_ID="nav-link-accountList"
    textbox_username_xpath="//input[@id='ap_email']"
    button_continue_xpath="//input[@id='continue']"
    textbox_password_xpath="//*[@id='ap_password']"
    button_login_xpath="//*[@id='signInSubmit']"
    dropdown_All_xpath = "//i[@class='hm-icon nav-sprite']"
    button_logout_xpath = "//a[contains(text(),'Sign Out')]"
    serach_box_xpath = "//input[@id='twotabsearchtextbox']"
    search_button_xpath = "//input[@id='nav-search-submit-button']"

    def __init__(self,driver):
        self.driver= driver

    def clickHello(self):
        self.driver.find_element(By.ID, self.button_hello_ID).click()

    def  setUsername(self,username):
        # self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.button_continue_xpath).click()

    def setPassword(self,Password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(Password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickAlldropdown(self):
        self.driver.find_element(By.XPATH, self.dropdown_All_xpath).click()

    def clickSignout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath)
    def clickSearchBox(self):
        self.driver.find_element(By.XPATH, self.serach_box_xpath)
    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath)


    # def clickLogout(self):
    #     self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

