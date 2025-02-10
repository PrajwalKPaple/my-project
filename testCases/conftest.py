from selenium import webdriver
import pytest

def setup():
    driver = webdriver.Edge(options = webdriver.EdgeOptions())
    return driver
