import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.yad2_page import Yad2Page
from helpers.webdriver_setup import WebDriverSetup

class Yad2SignupTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverSetup.get_driver()
        cls.yad2_page = Yad2Page(cls.driver)
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signup(self):
        # Open Yad2 Signup Page
        self.yad2_page.open()
        time.sleep(3)
        self.yad2_page.click_login_button()

        # Fill out the login form and submit
        self.yad2_page.login("nojijaef9t@qejjyl.com", "Aa123456")

        # Click "בפעם אחרת" if it appears
        self.yad2_page.good_to_see_you_again("בפעם אחרת")

        # Click profile menu button איזור אישי -> עדכון פרטים
        self.yad2_page.personal_list_header(
            "//a[@data-testid='enterPersonal-option']",
            "//a[@class='menu-item_link__E2lLZ' and @href='https://www.yad2.co.il/personal/profile']"
        )

        # Update profile fields
        self.yad2_page.update_profile_fields(
            first_name="BBB",
            last_name="AAA",
            phone_number="050-1234567",
            birthday="02-03-1965",
            city="חיפה",
            street="asdf",
            house_number="5"
        )

        # Submit and verify profile update
        self.yad2_page.submitProfile("הפרופיל עודכן בהצלחה")

if __name__ == "__main__":
    unittest.main()