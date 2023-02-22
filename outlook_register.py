from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os

# 创建 Firefox 浏览器驱动
driver = webdriver.Firefox()

# 打开 Outlook 注册页面
driver.get("https://signup.live.com/signup")

# 输入用户名
username = driver.find_element("name","MemberName")
# 读取文本文件第一行
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
filename = os.path.join(desktop_path, "outlook_email.txt")
with open(filename, "r") as f:
    first_line = f.readline().strip()  # 读取第一行并去除换行符
username.send_keys(first_line)

# 点击“下一步”按钮
next_button = driver.find_element("id","iSignupAction")
next_button.click()

time.sleep(1)

# 输入密码
password = driver.find_element("css selector","#PasswordInput")
password.send_keys("hello2023")

# 点击“下一步”按钮
next_button = driver.find_element("id","iSignupAction")
next_button.click()

time.sleep(1)

# 输入名字
firstname = driver.find_element("name","FirstName")
firstname.send_keys("Wang")

# 输入姓氏
lastname = driver.find_element("name","LastName")
lastname.send_keys("Dong")

# 点击“下一步”按钮
next_button = driver.find_element("id","iSignupAction")
next_button.click()

# 等待一段时间，直到页面加载完成
time.sleep(2)

select_month = driver.find_element("css selector","#BirthMonth")
select = Select(select_month)
select.select_by_index(1)

select_day = driver.find_element("css selector","#BirthDay")
select = Select(select_day)
select.select_by_index(12)

year = driver.find_element("css selector","#BirthYear")
year.send_keys("1990")

# 点击“下一步”按钮
next_button = driver.find_element("id","iSignupAction")
next_button.click()

time.sleep(30)

# 点击“下一步”按钮
next_button1 = driver.find_element("xpath","/html/body/div/div/div[1]/button")
next_button1.click()

print("已注册邮箱",first_line)

