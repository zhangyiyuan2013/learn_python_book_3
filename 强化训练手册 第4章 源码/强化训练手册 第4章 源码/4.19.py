# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 4.19 输出饭店菜谱

dishs = []              # 存放菜名
prices = []             # 存放价格
for i in range(8):
    dish = input("请输入菜名：")
    price = input("请输入价格：")
    dishs.append(dish)
    prices.append(price)

print("\t\t特色小菜")
for j in range(8):
    print(dishs[j] + "\t………………", prices[j] + "元")