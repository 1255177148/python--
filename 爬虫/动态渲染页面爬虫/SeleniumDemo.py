from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# driver_path=(r'E:\firefox\geckodriver.exe')#driver_path就是你的驱动路径
binary_path=(r'C:\Program Files\Mozilla Firefox\firefox.exe')  #binary_path就是你的游览器路径
ops=Options()
ops.binary_location=binary_path
# serve=Service(driver_path)
driver = webdriver.Firefox(options=ops)