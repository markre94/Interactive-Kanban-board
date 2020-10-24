import time
from flask_app_tests.pages.login_page import KanbanLoginPage
from flask_app_tests.pages.start_page import KanbanStartPage, KanbanAppPage
from flask_app_tests.pages.register_page import KanbanRegisterPage


def test_login(browser):
    login_page = KanbanLoginPage(browser)
    login_page.load()
    mail_data = 'marcin@gmail.com'
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
    time.sleep(2)


def test_add_task(browser):
    login_page = KanbanLoginPage(browser)
    login_page.load()
    mail_data = 'marcin@gmail.com'
    passwd_data = 'mama'

    login_page.login(mail_data, passwd_data)

    task_page = KanbanAppPage(browser)
    task_page.load()
    task_page.add_new_task('make coffee')

    time.sleep(2)


def test_undertake_task(browser):
    # Login to the page
    login_page = KanbanLoginPage(browser)
    login_page.load()
    mail_data = 'marcin@gmail.com'
    passwd_data = 'mama'

    login_page.login(mail_data, passwd_data)

    task_page = KanbanAppPage(browser)
    task_page.load()
    task_page.take_new_task()
    time.sleep(2)
    #



