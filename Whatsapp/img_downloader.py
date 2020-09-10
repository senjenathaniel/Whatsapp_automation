from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests

from functions import write_data_to_file, get_last_timestamp

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(
    'E:\\MegaSyncHP\\Sync\\Code\\python\\webdriver\\chromedriver.exe', chrome_options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)


def get_status(username):

    messages = []

    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[1]/div'))).click()
    print("Opening Status page...")
    time.sleep(2)

    chats = driver.find_elements_by_class_name("_3ko75")

    for chat in chats:
        if chat.text == username:
            chat.click()

        while True:
            try:
                if driver.find_element_by_class_name('_3Whw5'):
                    image = driver.find_element_by_class_name(
                        '_3Whw5').get_attribute('src')
                    print(image + "Image found.")

                    r = requests.get(image)
                    with open('files/' + image, 'wb') as f:
                        f.write(r.content)
                else:
                    print("No image found!")
                # Go to next
                driver.find_element_by_class_name('_3THFw').click()

            except:
                driver.close()
            finally:
                break

    return messages


get_status("Faiye")
