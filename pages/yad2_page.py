import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class Yad2Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.yad2.co.il"

    def open(self):
        self.driver.get(self.url)
        time.sleep(3)

    def click_login_button(self):
        # Wait for the button to be clickable and click it
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='להתחברות']"))
        )
        login_button.click()

    def login(self, email, password):
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

    def good_to_see_you_again(self, option):
        try:
            button_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//button[text()='{option}']"))
            )
            button_element.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def personal_list_header(self, option, select_list):
        profile_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='תפריט פרופיל']"))
        )
        profile_button.click()

        personal_area_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, option))
        )
        personal_area_link.click()

        update_details_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, select_list))
        )
        update_details_link.click()

    def update_profile_fields(self, first_name, last_name, phone_number, birthday, city, street, house_number):
        # Wait for profile fields to be visible
        first_name_field = self.wait.until(EC.visibility_of_element_located((By.ID, "firstName")))
        last_name_field = self.wait.until(EC.visibility_of_element_located((By.ID, "lastName")))
        phone_number_field = self.wait.until(EC.visibility_of_element_located((By.ID, "phone")))
        birthday_field = self.wait.until(EC.visibility_of_element_located((By.ID, "birthday")))
        city_field = self.wait.until(EC.visibility_of_element_located((By.ID, "city.value")))
        street_field = self.wait.until(EC.visibility_of_element_located((By.ID, "street.value")))
        house_number_field = self.wait.until(EC.visibility_of_element_located((By.ID, "house.value")))

        # Update fields
        first_name_field.send_keys(Keys.BACKSPACE)
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field.send_keys(Keys.BACKSPACE)
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        phone_number_field.send_keys(Keys.BACKSPACE)
        phone_number_field.clear()
        phone_number_field.send_keys(phone_number)

        birthday_field.send_keys(Keys.BACKSPACE)
        birthday_field.clear()
        birthday_field.send_keys(birthday)

        city_field.send_keys(Keys.BACKSPACE)
        city_field.click()
        city_field.send_keys(city)
        self.select_dropdown_option(city)

        street_field.click()
        street_field.send_keys(street)
        self.select_dropdown_option(street)

        house_number_field.click()
        house_number_field.send_keys(house_number)
        self.select_dropdown_option(house_number)

    def select_dropdown_option(self, text):
        option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//li[contains(@class, 'container_row__aV0c6') and contains(., '{text}')]")
        ))
        option.click()

    def submit(self):
        time.sleep(5)
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

    def submitProfile(self, expected_toast_message):
        time.sleep(5)
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

        toast_message = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='snackbar_text__1bvrO']"))
        )
        assert expected_toast_message in toast_message.text, "Profile update message does not match expected value"

    def click_publish_ad(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'publish-ad_button__J2sIB')]"))
        ).click()

    def select_category(self, option):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[@class='title' and text()='{option}']")
        )).click()

    def select_private_option(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='פרטי']")
        )).click()

    def enter_product_name(self, product_name):
        input_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//div[@data-testid='text-field-wrapper-title']//input[@data-testid='text-field-title']"))
        )
        input_field.send_keys(product_name)
        print(f"Product name '{product_name}' entered successfully!")

    def upload_image(self, file_path):
        file_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.upload-image-entry_uploadInput__U17qo"))
        )
        file_input.send_keys(file_path)
        print("Image uploaded successfully!")

    def select_device_type(self, device_type):
        self.driver.execute_script("window.scrollBy(0, 900);")
        input_field = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='text-field-Device Type']"))
        )
        input_field.click()
        device_option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@class='container_item__c7jvh' and .//span[text()='{device_type}']]")
            )
        )
        device_option.click()
        print(f"Device type '{device_type}' selected successfully!")

    def select_product_condition(self, condition):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//button[span[text()='{condition}']]"))
        )
        button.click()
        print(f"Product condition '{condition}' selected successfully!")

    def enter_price(self, price):
        # Locate the price input field by its data-testid attribute
        price_input = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='text-field-price']"))
        )
        # Enter the price into the input field
        price_input.clear()  # Clear the field before entering a new value
        price_input.send_keys(price)
        print(f"Price '{price}' entered successfully!")

    def enter_location(self, city, street, home_number):
        # Enter city
        city_input_field = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='text-field-cityId']"))
        )
        city_input_field.send_keys(city)
        city_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//li[contains(., '{city}')]"))
        )
        city_option.click()
        print(f"City '{city}' selected successfully!")

        # Enter street
        street_input_field = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='text-field-streetId']"))
        )
        street_input_field.send_keys(street)
        street_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//li[contains(., '{street}')]"))
        )
        street_option.click()
        print(f"Street '{street}' selected successfully!")

        # Enter home number
        home_number_field = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='text-field-homeNumber']"))
        )
        if home_number_field.is_enabled():
            home_number_field.send_keys(home_number)
            home_number_option = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//li[contains(., '{home_number}')]"))
            )
            home_number_option.click()
            print(f"Home number '{home_number}' entered successfully!")
        else:
            print("Home number field is disabled!")

    def agree_to_terms_and_continue(self):
        time.sleep(5)
        eula_checkbox = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='eula']"))
        )
        eula_checkbox.click()
        print("Agreed to terms and conditions.")
        self.submit()

    def select_package_type(self):
        # Wait for the button to be clickable and click it
        button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='select-package-type-1']"))
        )
        button.click()
        print("Button 'בחירה במסלול' clicked successfully!")

    def select_continue_free_ad(self):
        # Wait for the button to be clickable and click it
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='המשך פרסום בחינם']"))
        )
        button.click()
        print("Button 'המשך פרסום בחינם' clicked successfully!")

    def click_signup_link(self):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.common-link[data-testid='register']"))
        ).click()

    def fill_signup_form(self, email, password):
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "re-entered-password").send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    def enter_verification_code(self, code):
        self.driver.find_element(By.ID, "code").send_keys(code)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    def complete_profile(self, first_name, last_name, phone):
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)
        self.driver.find_element(By.ID, "phoneNumber").send_keys(phone)
        checkbox = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @aria-label='checkbox']")))
        checkbox.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()