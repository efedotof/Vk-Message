#import
import sys

from selenium import *
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import main
from data_source import *
import win10toast
import plyer.platforms.win.notification
from plyer import notification
from main import *
#arguments



global numbers_c, color_lbl1, color_lbl2,color_lbl3, color_lbl4, color_lbl5
color_lbl1 = 0
color_lbl2 = 0
color_lbl3 = 0
color_lbl4 = 0
color_lbl5 = 0

#toast = win10toast.ToastNotifier()

with open('txt/login.txt', 'r',encoding='utf-8') as myfile:
    login_polizovatel = myfile.read().replace('\n', '')
with open('txt/password.txt', 'r',encoding='utf-8') as f:
    password_polizavatel = f.read().replace('\n','')
with open('txt/link.txt', 'r',encoding='utf-8') as f:
    link_mm = f.read().replace('\n','')
with open('txt/message.txt', 'r',encoding='utf-8') as myfile:
    text = myfile.read().replace('\n', '')
chasa = 3600
poltora_chasa = 5400
pol_chasa = 1800

three_minuts = 180

numbers_c = 0
k = 0

#main cycle
def _browser_():
    print("Начало работы бота")
    global browser
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(executable_path=r"chromedriver.exe",chrome_options=options)
    browser.get(vk_url)
    time.sleep(3)
    _browser__logout_login_()

    _browser__logout_password_()

    _browser__logout_vhode_()

    _browser__messi_profile_()


    message_repiut()

def _browser__logout_login_():
    print("Ввод логина")
    browser.find_element(By.ID, input_login).send_keys(login_polizovatel)
    browser.save_screenshot('screenshots/login_screen.png')
    time.sleep(10)
    browser.save_screenshot('screenshots/win4_input_screen.png')

def _browser__logout_password_():
    print("Ввод пароля")
    time.sleep(10)
    browser.find_element(By.ID, input_password).send_keys(password_polizavatel)
    browser.save_screenshot('screenshots/password_screen.png')
    time.sleep(10)
    browser.save_screenshot('screenshots/win3_input_screen.png')

def _browser__logout_vhode_():
    print("Авторизация")
    time.sleep(10)
    browser.find_element(By.ID, input_vhode).click()
    browser.save_screenshot('screenshots/window_screen.png')
    time.sleep(10)
    browser.save_screenshot('screenshots/win2_input_screen.png')
    color_lbl1 = 1
def _browser__messi_profile_():
    print("Обновление")
    browser.save_screenshot('screenshots/win1_input_screen.png')
    time.sleep(10)
    browser.get(link_mm)
    browser.save_screenshot('screenshots/update_screen.png')
    time.sleep(10)

def _browser__mess_mess_():
    print("печатание сообщения")
    time.sleep(30)
    browser.save_screenshot('screenshots/massage1_input_screen.png')
    browser.find_element(By.ID,text_write).send_keys(text)
    browser.save_screenshot('screenshots/massage2_input_screen.png')
    time.sleep(10)
    browser.save_screenshot('screenshots/massage_input_screen.png')
    time.sleep(10)
    print("Отправка сообщения")
    browser.find_element(By.XPATH,otprav).click()
    browser.save_screenshot('screenshots/massege_shipment_screen.png')
    print("Уведомление")
    push()
def message_repiut():
    with open('txt/polizovatel_time.txt', 'r', encoding='utf-8') as myfile:
        polizovatel_times = myfile.read().replace('\n', '')
    with open('txt/miss_pol.txt', 'r', encoding='utf-8') as myfile:
        mission_componion = myfile.read().replace('\n', '')
    polsss_n = int(mission_componion)
    pollis_timess = int(polizovatel_times)
    setting = True
    while setting:
        if polsss_n != 0:
            _browser__mess_mess_()
            polsss_n -= 1
            if polsss_n != 0:
                print("Ожидание повтороной отправки, так как - polsss_n = ", polsss_n)
                time.sleep(pollis_timess - 50)
            else:
                setting = False
                print("Конец программы, так как polsss_n = ", polsss_n)
                sys.exit()
        else:
            setting = False
            print("Конец программы")
            sys.exit()

def push():
    notification.notify("Сообщение отправлено", "Ваше сообщение дошло вашему отправителю")

def main_mess():
    _browser_()
