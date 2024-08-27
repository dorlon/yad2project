import unittest
from helpers.webdriver_setup import WebDriverSetup
from pages.yad2_page import Yad2Page
import time


class Yad2AdPublishTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverSetup.get_driver()
        cls.yad2_page = Yad2Page(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_ad_publish(self):
        self.yad2_page.open()
        time.sleep(4)
        self.yad2_page.click_login_button()

        # Login
        self.yad2_page.login("dorbit050@gmail.com", "Aa123456")

        # Handle the optional pop-up
        self.yad2_page.good_to_see_you_again("בפעם אחרת")

        # Click "פרסום מודעה"
        self.yad2_page.click_publish_ad()

        # Select category "יד שניה"
        self.yad2_page.select_category("יד שניה")

        # Select "פרטי" option
        self.yad2_page.select_private_option()

        # Enter product name
        self.yad2_page.enter_product_name("אייפון 10")

        # Upload image
        self.yad2_page.upload_image("C:\\Users\\dorbi\\Downloads\\אייפון 10.JPG")

        # Select device type "סמארטפון"
        self.yad2_page.select_device_type("סמארטפון")

        # Select product condition "חדש באריזה"
        self.yad2_page.select_product_condition("חדש באריזה")

        # Enter price
        self.yad2_page.enter_price("555")

        # Continue to the next page
        self.yad2_page.submit()

        # Enter location details
        #self.yad2_page.enter_location("חיפה", "נווה גנים", "5")

        # Agree to terms and continue
        self.yad2_page.agree_to_terms_and_continue()

        self.yad2_page.select_package_type()
        #time.sleep(3)

        self.yad2_page.select_continue_free_ad()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()