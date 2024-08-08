from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException


class skiponboarding:
 def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

 def init_elements(self):
        self.get_started   = (AppiumBy.XPATH,'//XCUIElementTypeButton[@name="GET STARTED"]')
        self.doitlater     = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="DO IT LATER"]')
        self.setupnotif    = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="SET UP NOTIFICATIONS"]')
        self.allow         = (AppiumBy.ACCESSIBILITY_ID,'Allow')
        self.setuptracking = (AppiumBy.XPATH,'//XCUIElementTypeButton[@name="SET UP TRACKING"]')
        self.todaylogo_home= (AppiumBy.ID,'//XCUIElementTypeImage[@name="logo-today-new"]')
       
  
 def tap_getstarted(self): 
        # Wait for the "Get Started" button to be visible
        self.wait.until(lambda driver: driver.find_element(*self.get_started))
        self.driver.find_element(*self.get_started).click()
    
 def doitlaterlink(self):
       self.wait.until(lambda driver: driver.find_element(*self.doitlater))
       self.driver.find_element(*self.doitlater).click()

 def setup_notification(self):
       self.wait.until(lambda driver: driver.find_element(*self.setupnotif))
       self.driver.find_element(*self.setupnotif).click()
       self.driver.find_element_by_name("Allow")

def setup_tracking(self):
       self.wait.until(lambda driver: driver.find_element(*self.setuptracking))
       self.driver.find_element(*self.setuptracking).click()
       self.driver.find_element_by_name("Allow")
 
def home_page(self):
    try:
        # Wait for the logo element to be present
        logo = self.wait.until(lambda driver: driver.find_element(*self.todaylogo_home))

        if logo:  # Check if logo element was found
            print("Logo is present")
        else:
            print("Logo is not present")

    except TimeoutException:
        print("Logo did not appear within the timeout")

 
