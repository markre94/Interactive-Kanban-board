import time
from flask_app_tests.pages.login_page import KanbanLoginPage
from flask_app_tests.pages.start_page import KanbanStartPage


def test_login(browser):
    login_page = KanbanLoginPage(browser)
    login_page.load()
    mail_data = 'pol@gmail.com'
    passwd_data = 'mama'

    login_page.login(mail_data, passwd_data)


def test_home(browser):
    start_page = KanbanStartPage(browser)
    start_page.load()
