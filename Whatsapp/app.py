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
    'E:\\MegaSyncHP\\Sync\\Code\\python\\webdriver\\chromedriver.exe', chrome_options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)


def get_status():

    messages = []

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[1]/div'))).click()
    print("Opening Status page...")

    time.sleep(5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((
        By.CLASS_NAME, '_3ko75'))).click()

    while True:
        try:
            message = driver.find_element_by_xpath(
                '//*[@id="app"]/div/span[3]/div/span/div[2]/div/span/div/div/div/div[5]/div/span').text

            timestamp_txt = driver.find_element_by_xpath(
                '//*[@id="app"]/div/span[3]/div/span/div[2]/div/span/div/div/div/div[2]/div[2]/div').text

            log = timestamp_txt[-5:] + "...[" + message[:25] + "]\n"

            write_data_to_file('files/app.log', log)
            write_data_to_file(
                'files/messages.txt', timestamp_txt[-5:] + "...\n" + message + '\n\n')

            print("Message downloaded.")
            # Go to next
            driver.find_element_by_class_name('_3THFw').click()

        except:
            break
        finally:
            pass

    driver.close()
    return messages


get_status()
