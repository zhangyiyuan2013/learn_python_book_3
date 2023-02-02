print("\033[31m    计算牛奶蛋白质含量 \033[0m")
num = int(input("\033[34m请输入牛奶的袋数："))
total = float(num * 6.4)
print(num,"袋牛奶含有蛋白质：%.1f" % total)