from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import time
from Locators.locators import orangehrm_xpaths
class Test_PIM_3:

    def __init__(self, driver):
        self.driver = driver
    # Create a method called main_menu to to validate the options are clickable
    def main_menu (self):
        try:
             # Click on the "Admin" tab
            adminbutton = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, orangehrm_xpaths().admin_tab)))
            adminbutton.click()
            # Lists of menu options to be clicked
            menu_options = ['Admin', 'PIM,', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Claim', 'Buzz']

            print(len(menu_options))

            for menu_option in menu_options:
                xpath = f"//span[text()='{menu_option}']"
                try:
                    # Find and click on the menu option
                    element = self.driver.find_element(By.XPATH, xpath)
                    element.click()
                    # Adding if function to click the cancel button in maintance tab
                    if xpath == "//span[text()='Maintenance']":
                        cancel = self.driver.find_element(By.XPATH, orangehrm_xpaths().cancel_button)
                        cancel.click()

                    print(menu_option)
                    time.sleep(2)
                except NoSuchElementException:
                    print(f"Element not found for menu option: {menu_option}")
        except (NoSuchElementException, StaleElementReferenceException) as selenium_error:
            print(selenium_error)