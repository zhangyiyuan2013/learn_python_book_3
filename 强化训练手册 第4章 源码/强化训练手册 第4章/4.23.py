words = ["天猫","聚划算","天猫超市","淘抢购","电器城","司法拍卖","淘宝心选","兴农扶贫","飞猪旅行"]

for i in range(9):
    print("\033[1;31;43m",words[i],"\033[0m",end="")
print()

for j in range(9):
    word = input()
    words[j] = word
    print("\033[31;0m请输入第"+str(j + 1) + "个要替换的导航菜单：",word,"\033[0m")
    for k in range(9):
        if k <= j:
            print("\033[1;32;43m",words[k],"\033[0m",end="")
        else:
            print("\033[1;31;43m",words[k],"\033[0m",end="")
    print()

print()
for m in range(9):
    print("\033[1;31;43m",words[m],"\033[0m",end="")
