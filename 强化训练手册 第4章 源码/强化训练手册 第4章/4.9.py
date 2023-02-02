item = []
for i in range(6):
    program = input("请输入表演的节目：\n")
    item.append(program)

print("\n\033[31m\t\t\t\t晚会节目单\n")
for j in range(6):
    print("\033[33m",str(j + 1) + ".",item[j],"\n")
    print("\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
