import datetime
print("\033[0;31m未来星期几?".center(20))
print("今天是：", datetime.datetime.now().strftime("%Y-%m-%d %A \033[0m"))
day = int(input("输入未来天数："))
year = (datetime.datetime.now() + datetime.timedelta(day)).strftime("%Y")
month = (datetime.datetime.now() + datetime.timedelta(day)).strftime("%m")
date = (datetime.datetime.now() + datetime.timedelta(day)).strftime("%d")
week = (datetime.datetime.now() + datetime.timedelta(day)).strftime("%A")
time = year + "年" + month + "月" + date + "日" + "\t" + week
print("\033[0;32m未来是：" + time)
