from selenium import webdriver
import pytest

def setup():
    driver = webdriver.Chrome(options = webdriver.ChromeOptions())
    return driver

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# @pytest.fixture(scope="class")
# def setup(request):
#     # Initialize ChromeOptions
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")  # Optional: Start browser maximized
#     # Replace with the path to your ChromeDriver
#     service_obj = Service("C:/path/to/chromedriver.exe")  # Update the path

#     # Initialize the WebDriver
#     driver = webdriver.Chrome(service=service_obj, options=chrome_options)
#     request.cls.driver = driver  # Pass the driver instance to the test class

#     yield driver  # Return the driver instance to the test
#     driver.quit()  # Quit the browser after the test execution
