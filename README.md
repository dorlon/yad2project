# Yad2 Testing Automation - Created by Dor Biton
This repository contains automated tests for the Yad2 website, using Selenium 
WebDriver with Python's unittest framework. The project is structured using the 
Page Object Model (POM) to promote maintainability and reusability of code.


## Project Structure
`helpers/webdriver_setup.py`: Contains the WebDriverSetup class, which initializes and configures the WebDriver.

`pages/base_page.py`: Defines the BasePage class, 
which serves as the parent class for all page objects, 
providing common functionality such as waiting for elements.

`pages/temp_mail_page.py`: Implements the TempMailPage class to interact with Temp-Mail service 
for generating temporary email addresses and fetching verification codes.

`pages/yad2_page.py`: Contains the `Yad2Page` class, 
which provides methods to interact with various elements on the Yad2 website, 
such as login, profile update, and ad publishing functionalities.

`tests/test_ad_publish.py`: Automates the process of publishing an ad on the Yad2 platform, 
including login, category selection, and ad details submission.

`tests/test_editProfile.py`: Automates the process of logging in, 
navigating to the profile section, and updating user details on the Yad2 platform.

`tests/test_signup.py`: Automates the user signup process on Yad2, 
including fetching a temporary email, receiving a verification code, and completing the profile setup.


## Getting Started
### Prerequisites
1. Python 3.x
2. Selenium WebDriver
3. ChromeDriver (or any other browser driver you plan to use)

### Installation
1. Clone the repository:
`git clone https://github.com/dorlon/yad2project.git`                                                          
`cd yad2-automation`

2. Download and install the ChromeDriver:
   Make sure the `chromedriver` is in your PATH or place it in the project directory.


## Running the Tests
1. Navigate to the test directory:
   `cd yad2tests/tests`
2. Run a specific test file:
   `python test_ad_publish.py`


### Good Luck :)
