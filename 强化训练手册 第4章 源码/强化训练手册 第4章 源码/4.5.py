# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 4.5 模拟输出中国联通流量提醒

f1 = 3.592   # 已用流量
f2 = 3.408   # 剩余流量
char = "http://u.10010.cn/tAE3v"
print("\033[34m中国联通流量提醒：")
print("截至10月21日24时，")
print("您当月共享国内通用流量已用" + str(float(f1)) + "GB，剩余" + str(float(f2)) + "GB；")
print("其他流量使用情况请点击进入" + char + "查询详解。\n")
