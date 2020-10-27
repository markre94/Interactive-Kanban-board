from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class KanbanLoginPage:
    URL = "http://127.0.0.1:5000/login"

    LOGIN_INPUT = (By.ID, 'email')
    PASS_INPUT = (By.ID, 'password')
    JOIN_BTN = (By.LINK_TEXT, 'Join today')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def login(self, config_login):
        login_input = self.browser.find_element(*self.LOGIN_INPUT)
        login_input.send_keys(config_login['email'])

        pass_input = self.browser.find_element(*self.PASS_INPUT)
        pass_input.send_keys(config_login['password'] + Keys.RETURN)

    def go_to_registration(self):
        join_today = self.browser.find_element(*self.JOIN_BTN)
        join_today.click()
