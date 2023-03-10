import os

# 批量生成邮箱号并保存到桌面

print("请输入你想生成的邮箱名前缀，将根据输入的前缀生成“前缀_001”形式的邮箱名")
print("例如输入chatgpt23，那么将生成chatgpt23_001@outlook.com-chatgpt23_999@outlook.com的邮箱名\n")
email_prefix = input("请输入前缀：")
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
filename = os.path.join(desktop_path, "outlook_email11.txt")
with open(filename, "w") as f:
    for i in range(5, 1000):
        email = email_prefix + "_{:03d}@outlook.com".format(i)
        f.write(email + "\n")

#邮箱名前缀"chatgpt111_"可自行更改，能注册就行
#生成后，该文件即可删除

print("邮箱列表文本outlook_email1.txt已生成")
