"""
练习：
在终端中获取一个整数，作为边长，打印矩形。
效果：
	请输入整数:5
*****
*   *
*   *
*   *
*****
请输入整数:8
********
*      *
*      *
*      *
*      *
*      *
*      *
********
"""
count = int(input("请输入整数:"))
pic = "*"
blank = " "
print(pic*count)
for item in range(count-2):
    print("%s%s%s"%(pic,blank*(count-2),pic))
print(pic*count)