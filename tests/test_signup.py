import time
import unittest
from helpers.webdriver_setup import WebDriverSetup
from pages.yad2_page import Yad2Page
from pages.temp_mail_page import TempMailPage


class Yad2SignupTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverSetup.get_driver()
        cls.yad2_page = Yad2Page(cls.driver)
        cls.temp_mail_page = TempMailPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signup(self):
        # Open Yad2 Signup Page
        self.yad2_page.open()
        self.yad2_page.click_login_button()

        # Save the original window handle
        original_window = self.driver.current_window_handle

        # Open Temp-Mail in a new tab
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.temp_mail_page.open()
        time.sleep(3)

        # Get email address from Temp-Mail
        email_address = self.temp_mail_page.get_email_address()
        print("Email Address:", email_address)

        # Switch back to the original Yad2 tab
        self.driver.switch_to.window(original_window)

        # Fill the signup form
        self.yad2_page.click_signup_link()
        self.yad2_page.fill_signup_form(email_address, "Aa123456")

        # Go back to the Temp-Mail tab to get the verification code
        self.driver.switch_to.window(self.driver.window_handles[-1])
        verification_code = self.temp_mail_page.get_verification_code()
        print("Verification Code:", verification_code)
        time.sleep(3)
        # Switch back to the Yad2 tab and enter the verification code
        self.driver.switch_to.window(original_window)
        self.yad2_page.enter_verification_code(verification_code)
        time.sleep(3)
        # Complete the profile
        self.yad2_page.complete_profile("Eilon", "Cohen", "0505620321")
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
