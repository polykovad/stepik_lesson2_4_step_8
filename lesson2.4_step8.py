from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # нажимаем на button
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()


    # считываем переменную х
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    # записываем в поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # нажимаем на Submit
    button2 = browser.find_element_by_id("solve")
    button2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()