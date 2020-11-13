import time
import string
import random
import os
from random import choice
from string import ascii_letters
from selenium import webdriver
from captcha2upload import CaptchaUpload

a = input("Введите количество итераций: ")
b = 0

while b != int(a):
    name_r = ("".join(choice(ascii_letters) for i in range(12)))
    sur_r = ("".join(choice(ascii_letters) for n in range(12)))
    pasw_r = ("".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16)))


    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("headless")

    #browser = webdriver.Chrome(options=chromeOptions)
    browser = webdriver.Chrome()
    browser.get("https://passport.yandex.ru/registration")
    name = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[1]/span/input")
    surname = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[2]/span[1]/input")
    login = browser.find_element_by_xpath("//*[@id=\"login\"]")
    pasw = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[2]/div[1]/span/input")
    pasw2 = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[2]/div[2]/span/input")
    no_tel = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div[1]/span")
    reg = browser.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div/main/div/div/div/form/div[4]/span/button")

    name.send_keys(name_r)
    surname.send_keys(sur_r)
    login.send_keys(name_r)
    pasw.send_keys(pasw_r)
    pasw2.send_keys(pasw_r)
    no_tel.click()

    otvet = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[1]/div[2]/span/input")
    cptch = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div[1]/span/input")
    otvet.send_keys("privet")
    time.sleep(2)

    with open('filename.png', 'wb') as file:
        file.write(browser.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div[2]/div/div[1]/img').screenshot_as_png)

    captcha = CaptchaUpload("551835801dd0bedd0f97d7ebf358b2c7")
    answ = captcha.solve("filename.png")
    os.remove("filename.png")
    b = int(b) + 1

    if answ == "1":
        print("Не удалось получить капчу")



    else:
        cptch.send_keys(answ)
        reg.click()
        f = open('mail.txt', 'w')
        f.write(name_r)
        f.write("@yandex.ru:")
        f.write(pasw_r)














