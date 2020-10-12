from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class KanbanStartPage:
    URL = "http://127.0.0.1:5000/"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
