# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 4.9 输出艺术团表演的节目单


item = []           # 存放输入的节目
for i in range(6):
    program = input("请输入表演的节目：\n")
    item.append(program)

# 输出节目单
print("\n\033[31m\t\t\t\t晚会节目单\n")
for j in range(6):
    print("\033[33m", str(j + 1) + ".", item[j], "\n")
    print("\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")