import datetime

# 第一次查看倒计时时间
time1 = input("请输入倒计时时间：")                                                    	# 输入设定的时间，如0:0:0
print("\033[0;31m\n\t倒计时软件")
print('\033[0;32m' + "=" * 20)
delta = datetime.datetime.strptime(time1, '%H:%M:%S') - datetime.datetime.today()      	# 设定的时间距离当前的时间差
hour = int(delta.seconds / 60 / 60)                                                     # 设定的时间距离当前时间的小时差
minute = int((delta.seconds - hour * 60 * 60) / 60)                                     # 设定的时间距离当前时间的分钟差
second = delta.seconds - hour * 60 * 60 - minute * 60                                   # 设定的时间距离当前时间的秒钟差
print('\033[0m\t', str(hour) + ":" + str(minute) + ":" + str(second) + "\n")          	# 输出时间差

# 第二次查看倒计时时间
time2 = input("请输入倒计时时间：")                                                    	# 输入设定的时间，如0:0:0
print("\033[0;31m\n\t倒计时软件")
print('\033[0;32m' + "=" * 20)
delta = datetime.datetime.strptime(time2, '%H:%M:%S') - datetime.datetime.today()      	# 设定的时间距离当前的时间差
hour = int(delta.seconds / 60 / 60)                                                     # 设定的时间距离当前时间的小时差
minute = int((delta.seconds - hour * 60 * 60) / 60)                                     # 设定的时间距离当前时间的分钟差
second = delta.seconds - hour * 60 * 60 - minute * 60                                   # 设定的时间距离当前时间的秒钟差
print('\033[0m\t', str(hour) + ":" + str(minute) + ":" + str(second) + "\n")          	# 输出时间差

# 第三查看倒计时时间
time3 = input("请输入倒计时时间：")                                                    	# 输入设定的时间，如0:0:0
print("\033[0;31m\t倒计时软件")
print('\033[0;32m' + "=" * 20)
delta = datetime.datetime.strptime(time3, '%H:%M:%S') - datetime.datetime.today()      	# 设定的时间距离当前的时间差
hour = int(delta.seconds / 60 / 60)                                                     # 设定的时间距离当前时间的小时差
minute = int((delta.seconds - hour * 60 * 60) / 60)                                     # 设定的时间距离当前时间的分钟差
second = delta.seconds - hour * 60 * 60 - minute * 60                                   # 设定的时间距离当前时间的秒钟差
print('\033[0m\n\t', str(hour) + ":" + str(minute) + ":" + str(second))        		# 输出时间差
