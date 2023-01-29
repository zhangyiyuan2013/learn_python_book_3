for i in ["0","1","2","3","4","5","6","7","8","9",":",";"]:
    print(i,end = "\t")
print()
for i in range(9800,9812):
    print(chr(i),end = "\t")
print()
num = input("请输入需要查看的星座数字或符号：")
if num == ":":
    num = 10
if num == ";":
    num = 11
print("您要查看的星座是：",chr(9800+int(num)))
