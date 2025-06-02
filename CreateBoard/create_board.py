import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def createBoard(driver, url):
    time.sleep(2)

    driver.find_element(By.XPATH, "//h1[contains(text(),'Create new board')]").click()
    time.sleep(2)
    # driver.find_element(By.CLASS_NAME, 'new-board-input').send_keys('Test', Keys.ENTER)
    input_field = driver.find_element(By.CLASS_NAME, 'new-board-input')
    input_field.send_keys('Test')
    time.sleep(2)
    input_field.send_keys(Keys.ENTER)
    time.sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div[1]/nav/button').click()
    # time.sleep(2)
