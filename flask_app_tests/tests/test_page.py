import time
from flask_app_tests.pages.login_page import KanbanLoginPage
from flask_app_tests.pages.start_page import KanbanStartPage
from flask_app_tests.pages.register_page import KanbanRegisterPage


def test_login(browser):
    login_page = KanbanLoginPage(browser)
    login_page.load()
    mail_data = 'pol@gmail.com'
    passwd_data = 'mama'

    login_page.login(mail_data, passwd_data)

    time.sleep(2)
    assert browser.current_url is "http://127.0.0.1:5000/app"


def test_register(browser, config_register):
    reg_page = KanbanRegisterPage(browser)
    reg_page.load()

    reg_page.register(config_register)

    time.sleep(2)
    """CHECKS PROPER REGISTRATION if the browser redirects to login page"""
    print(browser.current_url)
    assert browser.current_url == "http://127.0.0.1:5000/login"


def test_home(browser):
    start_page = KanbanStartPage(browser)
    start_page.load()
