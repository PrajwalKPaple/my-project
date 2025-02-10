from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    button_hello_ID="nav-link-accountList-nav-line-1"
    textbox_username_xpath="//input[@id='ap_email_login']"
    button_continue_xpath="//input[@type='submit']"
    textbox_password_ID="ap_password"
    button_login_ID="signInSubmit"
    dropdown_All_xpath = "//a[@id='nav-hamburger-menu']"
    button_logout_xpath = "//ul[@class='hmenu hmenu-visible']//a[@class='hmenu-item'][normalize-space()='Sign Out']"

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
        self.driver.find_element(By.ID, self.textbox_password_ID).clear()
        self.driver.find_element(By.ID, self.textbox_password_ID).send_keys(Password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_login_ID).click()

    def clickAlldropdown(self):
        self.driver.find_element(By.XPATH, self.dropdown_All_xpath).click()

    def clickSignout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath)

    # def clickLogout(self):
    #     self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

