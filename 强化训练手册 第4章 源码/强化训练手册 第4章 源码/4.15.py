# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 4.15 计算身体质量指数（BMI）


weight = float(input("请输入体重值（kg）："))
height = float(input("请输入身高值（m）："))
BMI = "%.1f" % (weight / (height * height))
print("用户的BMI指数是：" + BMI)