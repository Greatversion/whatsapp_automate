from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()
option.add_argument("user-data-dir=C:/Users/verma/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=option)
print("Chrome launched")
driver.get("https://web.whatsapp.com")
print("WhatsApp Web opened")
wait = WebDriverWait(driver, 200000000)

target = '"The trio"'
print("Finding contact:", target)

contact_path = '//span[contains(@title,' + target + ')]'
contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
print("Contact found")
contact.click()
time.sleep(5)  # Adding a wait for the page to load properly ..
print("Message box clicked")

message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
message_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
print("Message box located")

# Define the message with emoticons on separate lines ..
message = "golu"
number_of_times = 100  # Reduced for testing ..
for x in range(number_of_times):
    for line in message.split('\n'):
        message_box.send_keys(line)
        message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(Keys.ENTER)
    print("Message sent:", x + 1)
    time.sleep(1)  # Increase sleep time to 1 second ..

print("Script completed, quitting browser")
driver.quit()
