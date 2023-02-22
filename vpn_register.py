from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os

# 创建 Firefox 浏览器驱动
driver = webdriver.Firefox()

# 打开 Outlook 注册页面
driver.get("https://ababybus.com/index.php#/register")

select_element = driver.find_element("css selector","select.form-control")
select = Select(select_element)
select.select_by_index(4)

username = driver.find_element("css selector","div.form-group:nth-child(1) > input:nth-child(1)")

# 读取文本文件第一行
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
filename = os.path.join(desktop_path, "outlook_email.txt")
with open(filename, "r") as f:
    first_line = f.readline().strip()  # 读取第一行并去除换行符
email_prefix = first_line.split("@")[0]  # 获取邮件地址前缀
username.send_keys(email_prefix)

password = driver.find_element("css selector","div.form-group:nth-child(3) > input:nth-child(1)")
password.send_keys("hello2023")

password_confirm = driver.find_element("css selector","div.form-group:nth-child(4) > input:nth-child(1)")
password_confirm.send_keys("hello2023")

next_button = driver.find_element("css selector",".btn-primary")
next_button.click()

#删除已注册邮箱
with open(filename, "r+") as f:
    data = f.readlines()
    f.seek(0)  # 将文件指针移动到开头
    f.writelines(data[1:])  # 写入除第一行之外的数据
    f.truncate()  # 截断文件，删除最后一行可能存在的多余内容


