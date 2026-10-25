from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    # 1. Открываем страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # 2. Ждём, пока цена станет $100
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element(
            (By.ID, "price"),
            "$100"
        )
    )

    # 3. Нажимаем Book
    browser.find_element(By.ID, "book").click()

    # 4. Получаем x
    x = browser.find_element(By.ID, "input_value").text

    # Считаем функцию
    y = calc(x)

    # Вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)

    # Нажимаем Submit
    browser.find_element(By.ID, "solve").click()

    # Получаем число из alert
    alert = browser.switch_to.alert
    print(alert.text)

    time.sleep(5)

finally:
    browser.quit()
