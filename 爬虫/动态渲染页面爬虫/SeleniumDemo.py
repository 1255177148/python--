from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

# driver_path=(r'E:\firefox\geckodriver.exe')#driver_path就是你的驱动路径
binary_path=(r'C:\Program Files\Mozilla Firefox\firefox.exe')  #binary_path就是你的游览器路径
ops=Options()
ops.binary_location=binary_path

# serve=Service(driver_path)
driver = webdriver.Firefox(options=ops)
driver.get("https://www.csdn.net/")
time.sleep(2) # 打开页面后，要先休眠2秒，等页面加载出来后，在选中标签对象，不然页面还没加载出来，就选择对象，会报错的
textLabel = driver.find_element(By.ID, "toolbar-search-input") # 根据id属性获取对应的标签，这里定位到了CSDN的输入框

'''
根据css选择器获取对应的标签,【#】是id,【.】是class,【div>input】是选择父标签为div的所有input标签,
【div+input】是选择同一级中在div之后的所有input标签, 【type='text'】是选择标签中属性type值为text的所有标签
'''
button = driver.find_element(By.CSS_SELECTOR, "#toolbar-search-button")
button.click() # 鼠标左键
# ActionChains(driver).context_click(button).perform() # 鼠标右键，先选择点击的对象，然后执行鼠标事件