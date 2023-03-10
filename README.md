# -chatgpt-vpn 新手写的第一个项目，如果能帮助到您，麻烦给个星星鼓励一下，谢谢~ 使用之前请下载好火狐浏览器，并配置好火狐浏览器的驱动变量，安装python相关库文件
此项目可以半自动傻瓜式注册outlook邮箱和vpn账号，每注册一次，可免费使用该vpn一天，此vpn可以稳定打开chatgpt

该vpn的台湾和美国节点可稳定使用chatgpt，此vpn新用户注册可免费获得一天使用时长，因此有了这个自动注册outlook邮箱（outlook邮箱无需手机验证码，因此可无限注册），并自动注册vpn账号的项目。
第一步，运行email_generate, 可在桌面看到生成了outlook_email.txt；
第二步，运行outlook_vpn_register.py，自动化注册邮箱直到最后一步人工验证，人工验证后，返回python执行界面，输入"是"，将继续执行自动注册vpn步骤。
