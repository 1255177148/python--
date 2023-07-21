from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

binary_path=(r'C://Program Files//Mozilla Firefox//firefox.exe')  #binary_path就是你的游览器路径
ops=Options()
ops.binary_location=binary_path

driver = webdriver.Firefox(options=ops)
driver.get("https://www.csdn.net/")
time.sleep(2) # 打开页面后，要先休眠2秒，等页面加载出来后，在选中标签对象，不然页面还没加载出来，就选择对象，会报错的

loginButton = driver.find_element(By.CSS_SELECTOR, 'a[class="toolbar-btn-loginfun"]') # 定位到登录按钮
loginButton.click() # 左键点击
time.sleep(1)
driver.switch_to.frame("passport_iframe") # 切换iframe到弹出的登录框
passwordLogin = driver.find_element(By.XPATH, '//div[@class="login-box-tabs-items"]/span[string()="密码登录"]')
time.sleep(1)
# print(passwordLogin.text)
jsClik = 'document.getElementsByClassName("login-box-tabs-items")[0].children[3].click()' # 使用js语言来操作点击事件
driver.execute_script(jsClik)
time.sleep(1)
userName = driver.find_element(By.XPATH, '//input[@class="base-input-text" and @autocomplete="username"]')
userName.clear()
userName.send_keys("18556976598")
password = driver.find_element(By.XPATH, '//input[@class="base-input-text" and @autocomplete="current-password"]')
password.clear()
password.send_keys("19941128ya@..")
time.sleep(1)
buttonClik = 'document.getElementsByClassName("base-button")[0].click()' # 使用js语言来操作点击事件
driver.execute_script(buttonClik)