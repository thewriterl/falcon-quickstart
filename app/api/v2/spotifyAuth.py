import requests
import json
import base64
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from sqlalchemy.orm import Session

from app.api.common.base import BaseResource
from selenium import webdriver

from app.api.model.welcome import Welcome


class SpotifyAuth(BaseResource):

    def auth(self):

        options = ChromeOptions()
        options.add_argument('--headless')

        browser = webdriver.Chrome('/Users/luizao/Downloads/chromedriver', options=options)
        browser.get('https://accounts.spotify.com/authorize?client_id=ba9e4d21b6774628a68f270cda29b344&response_type=code&redirect_uri=https://example.com/callback&scope=user-library-read')

        WebDriverWait(browser, 90).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-facebook")))

        fb = browser.find_element_by_class_name("btn-facebook").click()

        WebDriverWait(browser, 90).until(EC.url_contains('facebook'))

        email = browser.find_element_by_xpath('//*[@id="email"]').send_keys('luiz.darthvader@gmail.com')

        password = browser.find_element_by_xpath('//*[@id="pass"]').send_keys('marchas477')

        btn = browser.find_element_by_xpath('//*[@id="loginbutton"]').click()
        #
        # WebDriverWait(browser, 90).until(EC.url_contains('spotify'))
        #
        # agree = browser.find_element_by_xpath('//*[@id="auth-accept"]').click()

        WebDriverWait(browser, 90).until(EC.url_contains('example'))


        head = {'Authorization' : 'Basic YmE5ZTRkMjFiNjc3NDYyOGE2OGYyNzBjZGEyOWIzNDQ6ZDRlM2JjNTYxM2NlNDIwZGFiNDQ2MTA0MDg2MjA3ZGU='}
        data = {'grant_type' : 'authorization_code', 'redirect_uri' : 'https://example.com/callback', 'code': browser.current_url.split('=')[1].split('#')[0]}
        post = requests.post('https://accounts.spotify.com/api/token', headers=head, data=data)
        data = json.loads(post.content.decode('utf8').replace("'", '"'))

        browser.close()
        browser.quit()
        return data


    def on_get(self, req, res):
       auth = self.to_json(self.auth())
       res.body = auth

class SpotifyCallback(BaseResource):

    def on_get(self, req, res):

        print('asdfasdf')