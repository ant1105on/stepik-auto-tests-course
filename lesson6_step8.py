from selenium import webdriver
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//input[@name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//form[@method="get"]/div[2]/input')
    input2.send_keys("Chernogolov")
    input3 = browser.find_element_by_xpath('//form//input[@class="form-control city"]')
    input3.send_keys("Minsk")
    input4 = browser.find_element_by_xpath('//form//input[@id="country"]')
    input4.send_keys("Belarus")
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла