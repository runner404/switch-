import os

# 批量生成邮箱号并保存到桌面
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
filename = os.path.join(desktop_path, "outlook_email.txt")
with open(filename, "w") as f:
    for i in range(1, 1000):
        email = "chatgpt111_{:03d}@outlook.com".format(i)
        f.write(email + "\n")

#邮箱名前缀"chatgpt111_"可自行更改，能注册就行
#生成邮箱文本后，该文件即可删除
