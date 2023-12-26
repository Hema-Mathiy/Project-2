from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from time import sleep
from Locators.locators import orangehrm_xpaths


class Test_PIM_1:

    def __init__(self, driver):
        self.driver = driver
    # Create a method called ResetPassword to Create a new password clicking forgot password button 
    def ResetPassword(self):
        try:
            # Clicking forgot password button
            self.driver.find_element(By.XPATH, orangehrm_xpaths().forgot_password).click()
            # Enter new username to reset the password
            username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, orangehrm_xpaths().reset_username_input)))
            username_input.send_keys("Admin")
            sleep(3)
            # Find the password input box and entering the password
            reset_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, orangehrm_xpaths().reset_password_button)))
            reset_button.click()
            sleep(3)
            # Printing the Message
            success_mgs= self.driver.find_element(by=By.XPATH, value=orangehrm_xpaths().reset_password_successful).text
            sleep(3)
            print(success_mgs)
        except NoSuchElementException as selenium_error:
            # Handling the error exception
            print(f"Unable to locate the element :{selenium_error}")
