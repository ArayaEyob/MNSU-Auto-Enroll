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

