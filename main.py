import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('/Users/shakayahaya/Desktop/chromedriver')
driver = webdriver.Chrome(service=s)
URL = "https://tinder.com/"
driver.get(URL)
main_page = driver.current_window_handle
time.sleep(5)
btn = driver.find_element(By.LINK_TEXT, 'Log in').click()
time.sleep(3)
fb_log_in = driver.find_element(By.XPATH,
                                '//*[@id="t-1776868400"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
time.sleep(5)

for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

driver.switch_to.window(login_page)
time.sleep(5)
cookies = driver.find_elements(By.CSS_SELECTOR, 'Button')
cookies[1].click()


def fb_login_page():
    time.sleep(5)
    email = driver.find_element(By.NAME, 'email')
    email.send_keys('wangsolong86@gmail.com')
    time.sleep(5)
    password = driver.find_element(By.NAME, 'pass')
    password.send_keys('childofgod1')
    time.sleep(5)
    login_fb = driver.find_element(By.NAME, 'login')
    login_fb.click()
    time.sleep(5)


fb_login_page()

driver.switch_to.window(main_page)


def notification_and_cookie_handla():
    driver.find_element(By.XPATH, '//*[@id="t-48487324"]/div/div[2]/div/div/div[1]/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="t-1776868400"]/div/div/div/div/div[3]/button[1]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="t-1776868400"]/div/div/div/div/div[3]/button[2]').click()


notification_and_cookie_handla()


def random_like_and_dislike():
    time.sleep(20)
    btn_ = driver.find_elements(By.CSS_SELECTOR, '.recsCardboard__cards button')
    both_like_and_dislike = random.choice([btn_[13], btn_[14]])

    for _ in range(20):
        both_like_and_dislike.click()
        time.sleep(10)


random_like_and_dislike()

time.sleep(5)
