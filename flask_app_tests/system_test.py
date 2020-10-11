import time


def test_login(browser):
    browser.get("http://127.0.0.1:5000/")
    pass
    time.sleep(2)

    browser.find_element_by_xpath('/html/body/nav/div[2]/ul/li[1]/a').click()

    browser.find_element_by_xpath('/html/body/div[1]/div/form/fieldset/div[1]/input').send_keys('pol@gmail.com')
    browser.find_element_by_xpath('//*[@id="password"]').send_keys('mama')
    browser.find_element_by_xpath('/html/body/div[1]/div/form/div/input').click()
