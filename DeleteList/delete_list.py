import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def deleteList(driver, url):
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[1]/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[contains(text(),'Delete list')]").click()
    time.sleep(2)
