"""
在终端中录入4个同学年龄,打印最小的年龄。
"""
temp = 1000
for i in range(4):
    age = int(input("请输入年龄："))
    if age < temp:
        temp = age

print("最小的年龄为：%s" % str(temp))
