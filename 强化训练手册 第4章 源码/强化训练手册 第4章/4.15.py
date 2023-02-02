weight = float(input("请输入体重值（kg）："))
height = float(input("请输入身高值（m）："))
BMI = "%.1f" % (weight / (height * height))
print("用户的BMI指数是：" + BMI)
