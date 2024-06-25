from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client
import time
import logging 




logging.basicConfig(level=logging.INFO)

# Function to enroll in a class
def enroll_in_class(username, password):
    # Set up Selenium WebDriver (assuming Chrome here)
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # Navigate to your university's student portal
        driver.get("https://web.mnsu.edu/eservices/")
        logging.info("Navigated to the student portal.")
        
        # Find and fill in the username and password fields
        username_field = driver.find_element(By.ID,"starid")
        password_field = driver.find_element(By.ID,"pinnbr")
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


        driver.get("https://eservices.minnstate.edu/registration/secure/index.html?campusid=071&functionId=3009")
        logging.info("Navigated to enrollment page.")

        driver.get("https://eservices.minnstate.edu/registration/cart/view.html?campusid=071")
        logging.info("Navigated to enrollment page.")
        
        review_plan_link = driver.find_element(By.XPATH, '//*[@id="ViewCartForm"]/table/tbody[2]/tr[1]/td[1]/label')
        review_plan_link.click()
        logging.info("Navigated to review plan.")
        
        # Example: Wait until the wishlist table is loaded
        wishlist_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ViewCartForm"]/table/tbody[2]'))
        )
        desired_course_name = "Your Desired Course Name"
        courses = driver.find_elements(By.XPATH, '//*[@id="ViewCartForm"]/table/tbody[2]/tr')
        
        for course in courses:
            course_name = course.find_element(By.XPATH, './td[1]').text
            if course_name == desired_course_name:
                # Click the checkbox to select the course
                checkbox = course.find_element(By.XPATH, './td[5]/input')
                checkbox.click()
                logging.info(f"Selected course '{desired_course_name}' for registration.")
                
                # Example: Wait for the register button and click it
                register_button = driver.find_element(By.XPATH, '//*[@id="register-button"]')
                register_button.click()
                logging.info("Clicked register button.")
                
                # Example: Wait for confirmation message (adjust according to your portal)
                confirmation_message = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.ID, "confirmation-message"))
                )

        
        # Example: Wait until the enroll button is clickable
        enroll_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "enroll-button"))
        )
        
        # Click the enroll button
        enroll_button.click()
        
        # Example: Wait for the success message (adjust according to your portal)
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "success-message"))
        )
        
        # Send success notification via Twilio
        send_sms_notification("Enrollment successful!")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        send_sms_notification("Enrollment failed!")
        
    finally:
        driver.quit()

# Function to send SMS notification using Twilio
def send_sms_notification(message):
    # Your Twilio account SID and auth token
    account_sid = 'AC286bf29a5483c9de1014ef4937720e89'
    auth_token = '28930b9a5e26d95080a9b3f0116b739a'
    client = Client(account_sid, auth_token)
    
    # Send SMS
    message = client.messages.create(
        body=message,
        from_='+14058963087',
        to='+14132424123'
    )
    print(f"SMS notification sent: {message.sid}")

# Example usage
if __name__ == "__main__":
    enroll_in_class("jo3165wl", "Mancitylove2@")

