no1 = input("请输入您的队名：")
no2 = input("请输入您的队名：")
no3 = input("请输入您的队名：")
no4 = input("请输入您的队名：")

# 批量行输出队名
print("\n输出为：")
for i in range(100):
    print(no1 + "\t" + no2 + "\t" + no3 + "\t" + no4)

# 单组列输出队名
print("\n输出为：")
for j in range(100):
    print(no1)
for j in range(100):
    print(no2)
for j in range(100):
    print(no3)
for j in range(100):
    print(no4)

# 分组列输出队名
print("\n输出为：")
for a in range(100):
    print(no1)
    print(no2)
    print(no3)
    print(no4)
