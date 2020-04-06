from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    #button.click()

    rr = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y=str(math.log(abs(12*math.sin(int(x)))))
    input4 = browser.find_element_by_id("answer")
    input4.send_keys(y)

  
    button2 = browser.find_element_by_css_selector("[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()
    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(40)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
