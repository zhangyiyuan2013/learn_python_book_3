from decimal import Decimal
mark = []                                               # 存放裁判打分
for i in range(8):
    print("请输入第" + str(i + 1) + "名裁判的打分：", end="")
    score = float(input())
    mark.append(score)
print("8名裁判打分：", end="")
for k in range(8):
    print(mark[k], end="  ")

marks = sorted(mark)                                    # 按由低到高排序8个分数
sum = 0                                                 # 总得分
for j in range(6):
    sum += float(marks[j + 1])
average = Decimal(sum / 6).quantize(Decimal('0.0'))     # 平均分，四舍五入保留1位小数
print("\n最后选手的分数为：", average)
