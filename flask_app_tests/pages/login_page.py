from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class KanbanLoginPage:
    URL = "http://127.0.0.1:5000/login"

    LOGIN_INPUT = (By.XPATH, "/html/body/div[1]/div/form/fieldset/div[1]/input")
    PASS_INPUT = (By.XPATH, '//*[@id="password"]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def login(self, login_data, passwd):
        login_input = self.browser.find_element(*self.LOGIN_INPUT)
        login_input.send_keys(login_data)

        pass_input = self.browser.find_element(*self.PASS_INPUT)
        pass_input.send_keys(passwd + Keys.RETURN)


