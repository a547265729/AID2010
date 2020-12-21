"""
练习5：
    程序产生1个,1到100之间的随机数。
    让玩家重复猜测,直到猜对为止。
每次提示：大了、小了、恭喜猜对了,总共猜了多少次。
效果：
	请输入要猜的数字:50
大了
请输入要猜的数字:25
小了
请输入要猜的数字:35
大了
请输入要猜的数字:30
小了
请输入要猜的数字:32
恭喜猜对啦,总共猜了5次
"""
import random

correct = random.randint(1, 100)
count = 0
while True:
    num = int(input("请输入要猜的数字："))
    if num > correct:
        print("大了")
    elif num < correct:
        print("小了")
    else:
        print("恭喜猜对了")
        break
    count += 1
print("总共猜了" + str(count) + "次")
