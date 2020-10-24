from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class KanbanStartPage:
    URL = "http://127.0.0.1:5000/"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)


class KanbanAppPage:
    URL = "http://127.0.0.1:5000/"

    TASK_INPUT = (By.XPATH, "/html/body/div/div[1]/div/form/div/div/input")
    TASK_ADD = (By.XPATH, "/html/body/div/div[1]/div/form/div/div/div/button")
    NEW_TASK_TAKE = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div[2]/a[1]")


    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def add_new_task(self, data):
        task_data = self.browser.find_element(*self.TASK_INPUT)
        task_data.send_keys(data)

        confirm_add = self.browser.find_element(*self.TASK_ADD)
        confirm_add.click()

    def take_new_task(self):
        take_task = self.browser.find_element(*self.NEW_TASK_TAKE)
        take_task.click()



