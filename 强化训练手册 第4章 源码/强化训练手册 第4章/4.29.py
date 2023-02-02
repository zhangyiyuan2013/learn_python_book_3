import datetime

time1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dl = input("请输入登录密码：")
print("\033[32m*******欢迎登录明日电子商城*********\033[0m")

time2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
gm = input("请输入要购买的商品：")
print("\033[32m***********购买成功！！************\033[0m")

time3 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
tc = input("是否退出？")
print("\033[32m***********已退出网站**************\033[0m")

print("\n\033[0;31m用户理理今天在网站的操作\033[0m")
print(time1, "登录网站")
print(time2, "购买" + gm)
print(time3, "退出网站")
