from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client
import time
import logging 

logging.basicConfig(level=logging.INFO)

def enroll_in_class(username, password):
    
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
       
        driver.get("https://web.mnsu.edu/eservices/")
        logging.info("Navigated to the student portal.")

        
        username_field = driver.find_element(By.ID, "starid")
        password_field = driver.find_element(By.ID, "pinnbr")
        username_field.send_keys(username)
        password_field.send_keys(password)

       
        password_field.send_keys(Keys.RETURN)

       
        acknowledgment_form = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="Job"]'))
        )
        logging.info("Acknowledgment form is present.")

      
        checkbox1 = driver.find_element(By.XPATH, '//*[@id="accept_tuition"]')
        checkbox2 = driver.find_element(By.XPATH, '//*[@id="understand_drop"]')
        checkbox1.click()
        checkbox2.click()
        logging.info("Acknowledgment checkboxes clicked.")

       
        submit_button = driver.find_element(By.XPATH, '//*[@id="Job"]/p[3]/input')
        submit_button.click()
        logging.info("Acknowledgment form submitted.")

        
        driver.get("https://eservices.minnstate.edu/registration/secure/index.html?campusid=071&functionId=3009")
        logging.info("Navigated to enrollment page.")

        driver.get("https://eservices.minnstate.edu/registration/cart/view.html?campusid=071")
        logging.info("Navigated to enrollment cart page.")

        time.sleep(5)



    
        checkbox3 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="selectAll202530071"]'))
        )
        checkbox3.click()
        logging.info("Select all courses clicked.")

        
        submit_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="ViewCartForm"]/p/input[1]'))

        )
        submit_button.click()
        logging.info("Acknowledgment form submitted.")

        
        time.sleep(5)

       
        WebDriverWait(driver, 20).until(
            EC.url_contains("https://eservices.minnstate.edu/registration/register/confirm.html")
        )
        driver.get("https://eservices.minnstate.edu/registration/register/confirm.html")
        logging.info("Checkout chart")

    
        time.sleep(5)
        

        driver.get("https://eservices.minnstate.edu/registration/register/confirm.html")
        logging.info("registration page")
        time.sleep(15)


      
    finally:
        
        driver.quit()

def send_sms_notification(message):
   
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=message,
        from_='',
        to='',
    )
    print(f"SMS notification sent: {message.sid}")


def main():
    rate_limiter = RateLimiter()
    key = 'enrollment'

    for i in range(50):
        if rate_limiter.is_allowed(key, 5, 60):  # Limit to 5 enrollments per minute
            auto_enrollment()
            
          
            send_sms('+1234567890', f'Student {i} enrolled successfully.')
        else:
           
            send_sms('+1234567890', f'Rate limit exceeded for student {i}.')

# Main
if __name__ == "__main__":
    enroll_in_class("", "")
    
