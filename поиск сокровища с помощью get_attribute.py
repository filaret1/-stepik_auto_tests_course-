from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, 'treasure')
x = x_element.get_attribute('valuex')
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.ID, 'treasure')
x = x_element.get_attribute('valuex')
y = calc(x)
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(y)
checkbox_input = browser.find_element(By.ID, 'robotCheckbox')
checkbox_input.click()
robot = browser.find_element(By.ID, 'robotsRule')
robot.click()
button=browser.find_element(By.CLASS_NAME, 'btn')
button.click()
print(x)