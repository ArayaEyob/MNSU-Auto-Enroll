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
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
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