import os 
import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import exxpected_conditions as EC
from twilio.rest import Client



# Twilio account information from environment variables
account_sid = os.getenv("AC286bf29a5483c9de1014ef4937720e89")
auth_token = os.getenv("28930b9a5e26d95080a9b3f0116b739a")
twilio_phone_number = "+14132424123"  




user_phone_number = "+1" + "4132424123"

star_id = "Jo3165wl"
password = "Mancitylove2@"


client = Client(account_sid, auth_token)

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--remote-allow-origins")
driver = webdriver.chrome(options=options)

def send_sms(to, message):
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=to
    )

# Method to navigate to the shopping cart
def go_to_shopping_cart(driver):
    driver.get("https://eservices.minnstate.edu/esession/authentication.do?campusId=071&postAuthUrl=http%3A%2F%2Feservices.minnstate.edu%2Fstudent-portal%2Fsecure%2Fdashboard.do%3Fcampusid%3D071")
    if cart_is_empty(driver):
        try:
            driver.find_element(By.CSS_SELECTOR, "span[id='DERIVED_SSR_FL_SSR_NOCLASSES_MSG$88$']")
        except:
            for i in range(13):
                try:
                    driver.find_element(By.CSS_SELECTOR, f"a[id='SSR_CART_TRM_FL_TERM_DESCR30${i}']").click()
                    break
                except:
                    continue

def cart_is_empty(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, "span[id='DERIVED_SSR_FL_SSR_AVAIL_FL$0']")
    except:
        print("Shopping Cart is Empty")
        return True
    return False

def click_enroll(driver):
    enroll_button = driver.find_element(By.CSS_SELECTOR, "a[id='DERIVED_SSR_FL_SSR_ENROLL_FL']")
    enroll_button.click()

# Method to click the validate button
def click_validate(driver):
    validate_button = driver.find_element(By.CSS_SELECTOR, "a[id='DERIVED_SSR_FL_SSR_VALIDATE_FL']")
    validate_button.click()

# Delay method
def delay(seconds):
    print(f"Start of {seconds} second delay")
    time.sleep(seconds)
    print(f"End of {seconds} second delay")

# Method to parse class ID
def parse_id(text):
    return text.split("- ")[2]

# Method to parse class name
def parse_class_name(text):
    return " ".join(text.split(" ")[:2])

# Method to wait for the select class screen
def wait_for_select_class_screen(driver):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "span[id='DERIVED_SSR_FL_SSR_AVAIL_FL$0']"))
    )

# Method to wait for the validation screen
def wait_for_validation_screen(driver):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "span[id='DERIVED_REGFRM1_DESCRLONG$0']"))
    )

# Main method
def main():
    driver.get("https://sis.case.edu/psc/P92SCWR/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL?")
    driver.find_element(By.NAME, "SSO_Signin").click()

    driver.find_element(By.ID, "username").send_keys(case_id)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-submit").click()
    driver.find_element(By.ID, "PTNUI_LAND_REC_GROUPLET_LBL$2").click()

    go_to_shopping_cart(driver)
    try:
        wait_for_select_class_screen(driver)
    except:
        print("Slow internet probably")

    while not cart_is_empty(driver):
        delay(3)
        go_to_shopping_cart(driver)
        try:
            wait_for_select_class_screen(driver)
        except:
            print("Slow internet probably")

        # (Add the rest of the logic here for scrolling and enrolling in classes...)

        send_sms(user_phone_number, "Your Shopping Cart is Empty!")
        print("Program finished")

if __name__ == "__main__":
    main()