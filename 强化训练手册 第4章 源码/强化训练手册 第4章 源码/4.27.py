# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 4.27 地铁购票金额计算


p = 2.00				# 票价
c = input("目的车站：")			# 目的车站
num = int(input("购票数量："))		# 购票数量
p2 = p * num                            # 应付金额
p3 = int(input("已付金额为："))		# 已付金额
p4 = p3 - p2                            # 找零金额
print()
print("\033[1;42m    购票信息     \033[0m")
print("目的车站：" + c)
print("票    价：%.2f" % p)
print("购票数量：" + str(num))
print("应付金额：" + str(int(p2)))
print("已付金额：" + str(int(p3)))
print("找    零：" + str(int(p4)))