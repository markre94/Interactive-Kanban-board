import time
from flask_app_tests.pages.login_page import KanbanLoginPage
from flask_app_tests.pages.start_page import KanbanStartPage, KanbanAppPage
from flask_app_tests.pages.register_page import KanbanRegisterPage


def test_login(browser, config_login):
    login_page = KanbanLoginPage(browser)
    login_page.load()
    login_page.login(config_login)
    time.sleep(2)
    assert browser.current_url == "http://127.0.0.1:5000/app"


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

    assert start_page.get_title() == "KANBAN"
    time.sleep(2)
    start_page.go_to_title_page()
    time.sleep(2)


def test_add_task(browser, config_login):
    login_page = KanbanLoginPage(browser)
    login_page.load()

    login_page.login(config_login)

    task_page = KanbanAppPage(browser)
    task_page.load()
    task_page.add_new_task('make coffee')

    time.sleep(2)


def test_undertake_task(browser, config_login):
    # Login to the page
    login_page = KanbanLoginPage(browser)
    login_page.load()

    login_page.login(config_login)

    task_page = KanbanAppPage(browser)
    task_page.load()
    task_page.add_new_task('make coffee')
    # Switch to doing
    task_page.take_new_task()
    # Switch to completed
    task_page.finish_task()
    # remove task
    task_page.remove_task()
    # log out
    task_page.log_out()

    # LOG OUT URL VALIDATION
    assert browser.current_url == "http://127.0.0.1:5000/"


def test_login_redirect(browser, config_login):
    task_page = KanbanAppPage(browser)
    task_page.load()

    assert browser.current_url == "http://127.0.0.1:5000/login?next=%2Fapp"

    login_page = KanbanLoginPage(browser)
    login_page.login(config_login)

    assert browser.current_url == "http://127.0.0.1:5000/app"


def test_join_today(browser):
    login_page = KanbanLoginPage(browser)
    login_page.load()
    login_page.go_to_registration()
    assert browser.current_url == "http://127.0.0.1:5000/register"


def test_login_from_registration_page(browser):
    register = KanbanRegisterPage(browser)
    register.load()
    register.sign_in()
    assert browser.current_url == "http://127.0.0.1:5000/login"


