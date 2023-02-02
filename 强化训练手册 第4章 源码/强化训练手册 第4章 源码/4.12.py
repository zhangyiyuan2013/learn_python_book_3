# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 4.12 计算外卖价格

p1 = 18.5
p2 = 2
p3 = 1

if p1 + p2 + p3 >= 20:
    p4 = -1
else:
    p4 = 0

print("虾仁鲜肉馄饨-小份10个", "\t×1", "\t￥", p1)
print("秘制麻酱单打", "\t\t\t×1", "\t￥", p2)
print("餐盒", "\t\t\t\t\t\t\t￥", p3)
print("商家配送", "\t\t\t\t×1", "\t￥", 0)
print("在线支付立减优惠", "\t\t\t\t\033[31m￥", p4, "\033[0m")
print("\033[34m☎联系商家\033[0m\t\t\t\t实付\t￥", p1 + p2 + p3 + p4)