from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from rich.console import Console
from rich.theme import Theme

from selenium.webdriver.chrome.options import Options

from CreateBoard.create_board import createBoard
from CreateLists.create_lists import createLists
from DeleteList.delete_list import deleteList


chromeOptions = Options()

custom_theme = Theme({'success': 'green', 'error': 'bold red'})

serv_obj = Service("C:/BrowserDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
console = Console(theme=custom_theme)

# driver = webDriver.Chrome()
driver.get("http://localhost:3000/")
driver.maximize_window()


try:
    if driver.find_element(By.XPATH, "//h1[contains(text(), 'My Boards')]").is_displayed():
        console.print('App Installed Successfully', style='success')

        # Create Board
        try:
            createBoard(driver, "")
            console.print('Create Board: Successful ✔', style='success')
        except Exception as e:
            console.print('Create Board: Failed! 👎', style='error')
            console.print(f"Error from Create Board: {e}")

        # Create Lists
        try:
            createLists(driver, "")
            console.print('Create Lists: Successful ✔', style='success')
        except Exception as e:
            console.print('Create Lists: Failed! 👎', style='error')
            console.print(f"Error from Create Lists: {e}")

        # Delete List
        try:
            deleteList(driver, "")
            console.print('Delete List: Successful ✔', style='success')
        except Exception as e:
            console.print('Delete List: Failed! 👎', style='error')
            console.print(f"Error from Delete List: {e}")


except Exception as e:
    console.print('When Access Website: Failed! 👎', style='error')
    console.print(f"Error from Accessing Website: {e}")

driver.close()
