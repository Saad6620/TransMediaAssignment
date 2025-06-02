import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def createLists(driver, url):
    time.sleep(2)

    # 1st List
    driver.find_element(By.XPATH, "//input[@data-cy='add-list-input']").send_keys('test1')
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Add list')]").click()
    time.sleep(2)

    # 2nd List
    driver.find_element(By.XPATH, "//input[@data-cy='add-list-input']").send_keys('test2')
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Add list')]").click()
    time.sleep(2)
