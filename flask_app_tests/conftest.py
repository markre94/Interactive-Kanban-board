import tempfile, os
import pytest
from selenium import webdriver
import subprocess
#
@pytest.fixture
def browser():
    """Initialazes the browser"""
    proc = subprocess.Popen('cd ..;export FLASK_APP=run.py;flask run', shell=True)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
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