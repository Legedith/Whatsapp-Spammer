from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
#Mi Amigos
names = ['Naveen Bsc B','Kochikame','Toph Beifong','Ninja Hattori'
         ,'Doremon V2.0','Grey Matter Pi','Lakshita Bsc Sf'
         ,'Echo Echo']
#mi message importante
msg = '_Nothing_ _again_ _again_'

input('Scan qr code, enter any key and press enter')
#time.sleep(5)
for name in names:
    #looks for search bar
    search = driver.find_element_by_class_name('_2zCfw')
    search.click()
    #inserts names into search bar and presses enter
    search.send_keys(name)
    search.send_keys(Keys.RETURN)
    #types the message and sends it
    msg_box = driver.find_element_by_class_name('_3u328')
    msg_box.send_keys(msg)
    msg_box.send_keys(Keys.RETURN)
