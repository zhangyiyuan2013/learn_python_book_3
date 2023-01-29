letter = input("请输入英文字母：")
num = int(ord(letter))
if num >= 65 and num <= 86:
    print(chr(848+int(num)))
if num >= 97 and num <= 113:
    print(chr(848+int(num)))
if num >= 114 and num <= 118:
    print(chr(849+int(num)))
