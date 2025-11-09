from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time


link = "https://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()
    num = browser.find_element(By.ID, "input_value")
    x = int(num.text)
    answer = str(math.log(abs(12*math.sin(x))))
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(5)
    browser.quit()
