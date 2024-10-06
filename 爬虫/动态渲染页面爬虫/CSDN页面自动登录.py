from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait # 显式等待用
from selenium.webdriver.support import expected_conditions as EC # 显式等待用
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os

binary_path=(r'C://Program Files//Mozilla Firefox//firefox.exe')  #binary_path就是你的游览器路径
ops=Options()
ops.binary_location=binary_path
ops.set_preference("dom.webdriver.enabled", False);

driver = webdriver.Firefox(options=ops)
driver.get("https://www.csdn.net/")
# '''
# 这里要隐藏特征,不然会被检测到是爬虫访问的,这个操作只能是chrome浏览器才能用
# 可以用一个js文件来隐藏,首先本地要先安装node.js,
# 然后在指定目录中cmd打开控制台,然后输入npx extract-stealth-evasions,等待片刻后,就会发现有个stealth.min.js文件下载下来了,
# 这个就是用来隐藏特征的
# '''
# print("当前的目录是:" + os.getcwd()) #看下当前工作目录，不然下面的open函数打开相对路径会有问题，这里找到正确的路径
# with open('stealth.min.js') as file:
#     js = file.read()
# driver.execute(
#     cmd_args={'source': js},
#     cmd="Page.addScriptToEvaluateOnNewDocument",
# )
messagePrompt = '超时了!'
'''
WebDriverWait是显式等待,这里是等待2秒,每0.5秒获取一次,直到获取到指定的元素为止,如果超过2秒还没获取到,则报【超时了!】提示,
这里显式等待,直到获取到登录按钮
'''
loginButton = WebDriverWait(driver, 2, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="toolbar-btn-loginfun"]')), message=messagePrompt)
# loginButton = driver.find_element(By.CSS_SELECTOR, 'a[class="toolbar-btn-loginfun"]') # 定位到登录按钮
loginButton.click() # 左键点击
driver.implicitly_wait(2)# 打开页面后，要先隐式等待2秒，等页面加载出来后，再切换iframe，不然页面还没加载出来，就选择对象，会报错的
driver.switch_to.frame("passport_iframe") # 切换iframe到弹出的登录框
# passwordLogin = driver.find_element(By.XPATH, '//div[@class="login-box-tabs-items"]/span[string()="密码登录"]')
driver.implicitly_wait(5) # 隐式等待2秒，这里是等当前页面全部刷新完之后，再执行下面的代码
# print(passwordLogin.text)
jsClik = 'document.getElementsByClassName("login-box-tabs-items")[0].children[3].click()' # 使用js语言来操作点击事件
driver.execute_script(jsClik)
userName = WebDriverWait(driver, 2, 0.5).until(EC.presence_of_element_located((By.XPATH, '//input[@class="base-input-text" and @autocomplete="username"]')), message=messagePrompt)
# userName = driver.find_element(By.XPATH, '//input[@class="base-input-text" and @autocomplete="username"]')
userName.clear()
userName.send_keys("18556976598")
password = driver.find_element(By.XPATH, '//input[@class="base-input-text" and @autocomplete="current-password"]')
password.clear()
password.send_keys("19941128ya@..")
driver.implicitly_wait(1)
checkboxClick = 'document.getElementsByClassName("inform-title")[0].click()'
driver.execute_script(checkboxClick)
driver.implicitly_wait(1)
buttonClik = 'document.getElementsByClassName("base-button")[0].click()' # 使用js语言来操作点击事件
driver.execute_script(buttonClik)

driver.implicitly_wait(2)
driver.switch_to.default_content() # 因为上面是切换iframe了，所以这里要返回上一层
message = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'toolbar-remind')), message=messagePrompt)# 选中CSDN右上角的消息标签
# message = driver.find_element(By.ID, 'toolbar-remind') # 选中CSDN右上角的消息标签
ActionChains(driver).move_to_element(message).perform() # 鼠标悬停
driver.implicitly_wait(1)
# following-sibling是同层向下查找，也就是通过哥哥获取弟弟节点，之类的following-sibling::div[1] 指的是获取所有弟弟节点中第一个div标签
# privateLetter = driver.find_element(By.XPATH, '//a[@id="toolbar-remind"]/following-sibling::div[1]/a[4]')
# privateLetter = driver.find_element(By.CSS_SELECTOR, '#toolbar-remind+div a:nth-child(4)') # css标签选择器，获取id为toolbar-remind第一个div弟弟节点的第四个a标签子节点
# css标签选择器，获取id为toolbar-remind第一个div弟弟节点的第四个a标签子节点
privateLetter = WebDriverWait(driver, 2, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#toolbar-remind+div a:nth-child(4)')), message=messagePrompt)
privateLetter.click()
driver.implicitly_wait(2)
driver.switch_to.frame("private")
chats = driver.find_element(By.XPATH, '//div[@id="app"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]') # XPATH选择器，下标是从1开始的
chats.click()