# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 4.30 输出出发日期列表


import datetime

week = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
today = int(datetime.datetime.now().strftime("%w"))                 # 获取今天是星期几
date = int(datetime.datetime.now().strftime("%d"))                  # 获取今天是几号
print("\033[22;37;40m\t\t\t\t\t请选择出发日期\t\t\t\t\t\t\033[0m".center(0))

for i in range(7):
    print("\033[22;32;40m", week[today - 1], "\t\033[0m", end="")
    today += 1
    if today >= 7:
        today = 0

print()
for j in range(7):
    print("\033[22;37;40m", date, "\t\033[0m", end="")
    tomorrow = datetime.date.today() + datetime.timedelta(days=j+1) # 获取明天是几号
    date = tomorrow.day