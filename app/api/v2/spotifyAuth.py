from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from app.api.common.base import BaseResource
from selenium import webdriver


class SpotifyAuth(BaseResource):


    def on_get(self, req, res):

        browser = webdriver.Chrome('/Users/luizao/Downloads/chromedriver')
        browser.get('https://accounts.spotify.com/authorize?client_id=ba9e4d21b6774628a68f270cda29b344&response_type=code&redirect_uri=https://example.com/callback&scope=user-read-private%20user-read-email')

        WebDriverWait(browser, 90).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-facebook")))

        fb = browser.find_element_by_class_name("btn-facebook")

        fb.click()

        WebDriverWait(browser, 90).until(EC.url_contains('facebook'))

        email = browser.find_element_by_xpath('//*[@id="email"]')

        password = browser.find_element_by_xpath('//*[@id="pass"]')

        email.send_keys('luiz.darthvader@gmail.com')
        password.send_keys('marchas477')

        btn = browser.find_element_by_xpath('//*[@id="loginbutton"]')

        btn.click()

        WebDriverWait(browser, 90).until(EC.url_contains('example'))

        data = {'token': browser.current_url.split('=')[1].split('#')[0]}

        browser.close()
        browser.quit()
        res.body = self.to_json(data)