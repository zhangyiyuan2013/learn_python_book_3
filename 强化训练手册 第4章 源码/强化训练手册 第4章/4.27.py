p = 2.00
c = input("目的车站：")
num = int(input("购票数量："))
p2 = p * num
p3 = int(input("已支付金额为："))
p4 = p3 - p2
print()
print("\033[1;42m    购票信息     \033[0m")
print("目的车站：" + c)
print("票    价：%.2f" % p)
print("购票数量：" + str(num))
print("应付金额：" + str(int(p2)))
print("已付金额：" + str(int(p3)))
print("找    零：" + str(int(p4)))
