from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get("https://login.live.com/")
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys("Enter email")
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()

time.sleep(2)

navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys("Enter Password")
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()

time.sleep(2)

navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()