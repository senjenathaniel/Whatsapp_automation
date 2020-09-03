from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

from functions import write_data_to_file, get_last_timestamp

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(
    'C:\\Users\\LAND\\Desktop\\chromedriver.exe', chrome_options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)


def get_status():

    messages = []

    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[1]/div'))).click()
    print("Opening Status page...")
    time.sleep(2)

    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="app"]/div/span[3]/div/span/div/div/div[1]/div[2]/div[1]/div/span/div[3]/div/div[1]/div/div/div'))).click()
    print("Opening Tchaku's status page...")

    while True:
        try:
            message = driver.find_element_by_xpath(
                '//*[@id="app"]/div/span[3]/div/span/div[2]/div/span/div/div/div/div[5]/div/span').text

            timestamp_txt = driver.find_element_by_xpath(
                '//*[@id="app"]/div/span[3]/div/span/div[2]/div/span/div/div/div/div[2]/div[2]/div').text

            timestamp = timestamp_txt[-5:] + "\n"

            messages.append(message)

            write_data_to_file('files/app.log', timestamp)

            time.sleep(1)

            print("Message downloaded.")
            # Go to next
            driver.find_element_by_class_name('_3THFw').click()

        except:
            break

    driver.close()
    return messages


for x in get_status():
    write_data_to_file(
        'files/messages.txt', x + "\n\n\n_________________________________________________________________________\n")
