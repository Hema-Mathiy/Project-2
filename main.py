from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageobject.TC_PIM_01 import Test_PIM_1
from pageobject.TC_PIM_02 import Test_PIM_2
from pageobject.TC_PIM_03 import Test_PIM_3
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import orangehrm_xpaths

# Define the URL and Dashboard URL
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

# Initialize the ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)

test1= Test_PIM_1(driver)
test1.ResetPassword()

try:
    driver.get(url)
    driver.implicitly_wait(10)
    # Find the usernam & password elements and Perform Login 
    username = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, orangehrm_xpaths().username_input_box)))
    username.send_keys("Admin")
    password = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, orangehrm_xpaths().password_input_box)))
    password.send_keys("admin123")
    driver.find_element(by=By.XPATH, value=orangehrm_xpaths().login_submit).click()
    driver.implicitly_wait(10)
    # Check if the current URL matches the dashboard URL
    if dashboard_url in driver.current_url:
        print("SUCCESS : Login success with username ")
 
        # Create instances of Test_PIM_1, Test_PIM_2, and Test_PIM_3 classes and call their methods
        test2= Test_PIM_2(driver)
        test2.admin_header_validation()
        test3= Test_PIM_3(driver)
        test3.main_menu()

        # Find the logout emelement and perform logout
        driver.find_element(by=By.XPATH, value=orangehrm_xpaths().logout_dropdown).click()
        logout_button = driver.find_element(by=By.XPATH, value=orangehrm_xpaths().logout_button).click()

    # If the URL doesn't match the dashboard URL, consider it a login failure  
    elif(url in driver.current_url):
        print("FAIL : Login failure with username ")
        driver.refresh()
except TimeoutException as selenium_error:
    print(selenium_error)
# close the web browser
driver.quit()
