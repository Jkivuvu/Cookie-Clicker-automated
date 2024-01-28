from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

start_time = time.time()
end_time = start_time + 5
stop_loop = start_time + 300
chrome_driver_path = 'Chrome_driver\chromedriver.exe'
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome()
driver.get('http://orteil.dashnet.org/experiments/cookie/')
Cookie = driver.find_element(By.ID, 'cookie')


def func(money):
    if 15 <= money < 100:
        cursor = driver.find_element(By.ID, 'buyCursor')
        cursor.click()
    elif 100 <= money < 500:
        Grandma = driver.find_element(By.ID, 'buyGrandma')
        Grandma.click()
    elif 500 <= money < 2000:
        Factory = driver.find_element(By.ID, 'buyFactory')
        Factory.click()
    elif 2000 <= money < 7000:
        Mine = driver.find_element(By.ID, 'buyMine')
        Mine.click()
    elif 7000 <= money < 50000:
        shipment = driver.find_element(By.ID, 'buyShipment')
        shipment.click()
    elif 50000 <= money < 1000000:
        alchemy = driver.find_element(By.ID, 'buyAlchemy lab')
        alchemy.click()
    elif 1000000 <= money < 123456789:
        portal = driver.find_element(By.ID, 'buyPortal')
        portal.click()
    elif 123456789 <= money:
        Time_machine = driver.find_element(By.ID, 'buyTime machine')
        Time_machine.click()

while not start_time >= stop_loop:
    start_time = time.time()
    Cookie.click()
    if end_time <= start_time:
        money = (driver.find_element(By.ID, 'money')).text
        money = int(money.replace(',', ''))
        func(money=money)
        end_time = start_time + 5
