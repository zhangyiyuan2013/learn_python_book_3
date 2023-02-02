# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 4.4 计算牛奶中蛋白质的总量

print("\033[31m     计算牛奶蛋白质含量 \033[0m")
num = int(input("\033[34m请输入牛奶的袋数："))
total = float(num * 6.4)
print(num, "袋牛奶含有蛋白质：%.1f" % total)

