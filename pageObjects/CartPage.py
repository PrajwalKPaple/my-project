from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import chrome
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:
    search_box_ID = "twotabsearchtextbox"
    add_to_cart_shoe_ID = "a-autoid-1-announce"
    confirmation_add_to_cart_xpath= "//button[contains(text(), 'Add to cart')]"
    search_button_ID = "nav-search-submit-button"



    def __init__(self, driver):
        self.driver = driver

    def clicksearchinput(self):
        self.driver.find_element(By.ID, self.search_box_ID).send_keys("SHOE")

    def clicksearchbutton(self):
        self.driver.find_element(By.ID, self.search_button_ID).click()

    def clickaddtocart(self):
        self.driver.find_element(By.ID, self.add_to_cart_shoe_ID).click()

    def clickconfirmationaddtocart(self):
        self.driver.find_element(By.XPATH, self.confirmation_add_to_cart_xpath).click()


    def clickconfirmation(self):
        self.driver.find_element(By.XPATH, self.confirmation_add_to_cart_xpath).click()

    def clicksearchinput1(self):
        self.driver.find_element(By.ID, self.search_box_ID).send_keys("BOTTLE")