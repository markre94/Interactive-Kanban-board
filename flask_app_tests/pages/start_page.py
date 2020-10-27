from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class KanbanStartPage:
    URL = "http://127.0.0.1:5000/"

    TITLE_PAGE = (By.LINK_TEXT, "KANBAN")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def go_to_title_page(self):
        self.browser.find_element(*self.TITLE_PAGE).click()

    def get_title(self):
        return self.browser.find_element(*self.TITLE_PAGE).text


class KanbanAppPage:
    URL = "http://127.0.0.1:5000/app"

    TASK_INPUT = (By.XPATH, "/html/body/div/div[1]/div/form/div/div/input")
    TASK_ADD = (By.XPATH, "/html/body/div/div[1]/div/form/div/div/div/button")
    NEW_TASK_TAKE = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div[2]/a[1]")
    DOING = (By.XPATH, "/html/body/div/div[2]/div/div/div[2]/a[1]")
    REMOVE_BTN = (By.XPATH, "/html/body/div/div[3]/div/div/div[2]/a")
    LOG_OUT = (By.XPATH, "/html/body/nav/div[2]/ul/li[2]/a")

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

    def finish_task(self):
        finish_task = self.browser.find_element(*self.DOING)
        finish_task.click()

    def remove_task(self):
        remove = self.browser.find_element(*self.REMOVE_BTN)
        remove.click()

    def log_out(self):
        log_out = self.browser.find_element(*self.LOG_OUT)
        log_out.click()
