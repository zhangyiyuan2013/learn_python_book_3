mark = []
sum = 0
for i in range(5):
    print("输入第" + str(i + 1) + "位成员的分数：",end="")
    number = input()
    mark.append(number)
    sum += int(mark[i])
average = sum / 5
print("小组5位成员的平均分是：",average)
