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
    # Set up Selenium WebDriver (assuming Chrome here)
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Navigate to your university's student portal
        driver.get("https://web.mnsu.edu/eservices/")
        logging.info("Navigated to the student portal.")

        # Find and fill in the username and password fields
        username_field = driver.find_element(By.ID, "starid")
        password_field = driver.find_element(By.ID, "pinnbr")
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for the acknowledgment page
        acknowledgment_form = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="Job"]'))
        )
        logging.info("Acknowledgment form is present.")

        # Check the acknowledgment boxes
        checkbox1 = driver.find_element(By.XPATH, '//*[@id="accept_tuition"]')
        checkbox2 = driver.find_element(By.XPATH, '//*[@id="understand_drop"]')
        checkbox1.click()
        checkbox2.click()
        logging.info("Acknowledgment checkboxes clicked.")

        # Submit the acknowledgment form
        submit_button = driver.find_element(By.XPATH, '//*[@id="Job"]/p[3]/input')
        submit_button.click()
        logging.info("Acknowledgment form submitted.")

        # Navigate to enrollment page
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

        # Wait for the submit button to be clickable and click it
        submit_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="ViewCartForm"]/p/input[1]'))

        )
        submit_button.click()
        logging.info("Acknowledgment form submitted.")

        # Allow time for the registration process to complete
        time.sleep(5)

        # # Wait additional time before closing the browser

        #   # Scroll into view and click the submit button
        # driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        # time.sleep(1)  # Wait a moment for scrolling to complete

        # # Click the button using JavaScript to ensure it's clicked
        # driver.execute_script("arguments[0].click();", submit_button)
        # logging.info("Submit button clicked.")

        # Wait for navigation to the next page
        WebDriverWait(driver, 20).until(
            EC.url_contains("https://eservices.minnstate.edu/registration/register/confirm.html")
        )
        driver.get("https://eservices.minnstate.edu/registration/register/confirm.html")
        logging.info("Checkout chart")

        

        # Allow time for the registration process to complete
        time.sleep(5)
        

        driver.get("https://eservices.minnstate.edu/registration/register/confirm.html")
        logging.info("registration page")
        time.sleep(15)


      
    finally:
        # Close the browser
        driver.quit()

def send_sms_notification(message):
    # Your Twilio account SID and auth token
    account_sid = 'AC286bf29a5483c9de1014ef4937720e89'
    auth_token = '28930b9a5e26d95080a9b3f0116b739a'
    client = Client(account_sid, auth_token)
    
    # Send SMS
    message = client.messages.create(
        body=message,
        from_='+14058963087',
        to='+14132424123',
    )
    print(f"SMS notification sent: {message.sid}")

# Main
if __name__ == "__main__":
    enroll_in_class("jo3165wl", "Mancitylove2@")
