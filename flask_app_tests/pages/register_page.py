from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class KanbanRegisterPage:
    URL = 'http://127.0.0.1:5000/register'

    USERNAME_INPUT = (By.XPATH, "/html/body/div[1]/div/form/fieldset/div[1]/input")
    PASSWORD_INPUT = (By.XPATH, "/html/body/div[1]/div/form/fieldset/div[3]/input")
    EMAIL_INPUT = (By.XPATH, "/html/body/div[1]/div/form/fieldset/div[2]/input")
    CONFIRM_PASS_INPUT = (By.XPATH, "/html/body/div[1]/div/form/fieldset/div[4]/input")
    REGISTER_BUTTON = (By.XPATH, "/html/body/div[1]/div/form/div/input")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def register(self, config_register):
        name_input = self.browser.find_element(*self.USERNAME_INPUT)
        name_input.send_keys(config_register['username'])

        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(config_register['email'])

        pass_input = self.browser.find_element(*self.PASSWORD_INPUT)
        pass_input.send_keys(config_register['password'])

        confirm_pass_input = self.browser.find_element(*self.CONFIRM_PASS_INPUT)
        confirm_pass_input.send_keys(config_register['password'])

        reg_button = self.browser.find_element(*self.REGISTER_BUTTON)
        reg_button.click()
