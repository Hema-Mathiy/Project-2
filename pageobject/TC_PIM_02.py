from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from Locators.locators import orangehrm_xpaths
import time


class Test_PIM_2:

    def __init__(self, driver):
        self.driver = driver
    # Create a method called admin_header_validation to validate the options are clickable
    def admin_header_validation (self):
        try:
            # Click on the "Admin" tab
            adminbutton = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, orangehrm_xpaths().admin_tab  )))
            adminbutton.click()
            # admin_header_options = self.driver.find_elements(By.XPATH, orangehrm_xpaths().admin_header_options)
            #  # Create a loop to click all "li" elements in the header of admin tab 
            # for header_options in admin_header_options:
            #     header_options.click()
            time.sleep(5)
            header_options = WebDriverWait(self.driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, orangehrm_xpaths().admin_header_options))
)
            print(len(header_options))
            
            for header_option in header_options:
                if header_option:
                    print(header_option.text)
                    
                    header_option.click()
                    time.sleep(3)

        except (NoSuchElementException, StaleElementReferenceException) as selenium_error:
            print(selenium_error)