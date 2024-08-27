import time

from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TempMailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://temp-mail.io/en"

    def open(self):
        self.driver.get(self.url)

    def get_email_address(self):
        time.sleep(4)
        email_element = self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        return email_element.get_attribute("title")

    def get_verification_code(self):
        self.driver.refresh()
        verification_email = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'אימות מייל')]")))
        verification_email.click()
        verification_code_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//div[@style='direction: rtl; font-size: 36px; font-weight: 300; line-height: 100%; text-align: center;']"))
        )
        return verification_code_element.text
