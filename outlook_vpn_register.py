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

time.sleep(2)

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

time.sleep(10)
print("已注册邮箱：",first_line)
confirm = input("请完成oulook邮箱注册验证码环节后开始注册vpn\n准备好注册vpn了吗?(是或否)\n")


def auto_rig(filename):
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
    #filename = os.path.join(desktop_path, "outlook_email.txt")
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
    return 1

if confirm == "yes" or confirm == "是":
    # 执行后续代码
    print("Continuing...")
    auto_rig(filename)
    driver.get("https://outlook.live.com/mail/0/junkemail")
    #删除已注册邮箱
    with open(filename, "r+") as f:
        data = f.readlines()
        f.seek(0)  # 将文件指针移动到开头
        f.writelines(data[1:])  # 写入除第一行之外的数据
        f.truncate()  # 截断文件，删除最后一行可能存在的多余内容
    print("已删除已注册邮箱")
    print("恭喜你拥有了vpn，麻烦您在GitHub点一颗星星鼓励一下！")
else:
    # 不执行后续代码
    print("注册已中断，请重新开始")


