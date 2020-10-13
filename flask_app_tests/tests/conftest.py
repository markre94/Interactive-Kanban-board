import tempfile,os
import pytest
from selenium import webdriver
import subprocess
import json

SUPPORTED_BROWESERS = ['chrome', 'firefox']


@pytest.fixture(scope='session')
def config():
    with open("config.json") as c_file:
        data = json.load(c_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config file does not have the "browser element"')
    elif config ['browser'] not in SUPPORTED_BROWESERS:
        raise Exception("The current browser is not in the supported browser scope")
    return config ['browser']


@pytest.fixture(scope='session')
def config_register():
    with open('register_data.json') as reg_data:
        data = json.load(reg_data)
        return data


@pytest.fixture
def browser(config_browser, config):
    """Initialazes the browser"""
    proc = subprocess.Popen('cd ..;export FLASK_APP=run.py;flask run', shell=True)
    if config_browser == 'chrome':
        driver = webdriver.Chrome()
    elif config_browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception(f'{config_browser} is not supported browser')

    driver.implicitly_wait(config ['wait_time'])
    yield driver
    proc.kill()
    driver.quit()

    """Kills the server"""
    p = subprocess.run("lsof -i -n -P | grep 5000", capture_output=True, shell=True, encoding="utf8")
    print(p.stdout)
    x = [elem for elem in p.stdout.split()]
    if x [0] == 'Python':
        subprocess.run(f'kill {x [1]}', shell=True)
    print("Killed")
