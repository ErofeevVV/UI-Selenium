from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

    browser.switch_to.alert.accept()

    num = browser.find_element(By.ID, "input_value")
    x = int(num.text)
    answer = str(math.log(abs(12*math.sin(x))))
    browser.find_element(By.ID, "answer").send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

finally:
    time.sleep(5)
    browser.quit()