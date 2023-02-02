# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 4.24 地铁站站牌显示

import datetime
a = input("请输入本站地铁名：")
print('')
print('\033[1;31m', "_" * 21)
print("|", " " * 19, "|")
print("|", datetime.datetime.now().strftime('    %Y-%m-%d'), "\t\t|",)
print("|", datetime.datetime.now().strftime('      %H:%m'), "\t\t\t|",)
print("|", datetime.datetime.now().strftime('     %A'), "\t\t|",)
print("|", "_" * 19, "|")
print("|", " " * 19, "|")
print("|", " " * 6, "本站", " " * 7, "|")
print("|", a.center(15), "|")
print("|", " " * 19, "|")
print('', "─" * 11)