from selenium import webdriver

class WebDriverSetup:
    @staticmethod
    def get_driver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver