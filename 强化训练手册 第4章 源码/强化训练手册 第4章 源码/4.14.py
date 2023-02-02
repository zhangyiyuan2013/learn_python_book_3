# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 4.14 计算小组成员平均分

mark = []           				# 存放成绩
sum = 0             				# 总分数
for i in range(5):
    print("输入第" + str(i + 1) + "位成员的分数：", end="")
    number = input()
    mark.append(number)
    sum += int(mark[i])
average = sum / 5   				# 平均分
print("小组5位成员的平均分是：", average)