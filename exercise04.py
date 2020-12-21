"""
练习1：在终端中录入5个人的身高，计算平均身高
练习2：在终端中录入多个人的身高，如果输入空字符串，则停止录入，在计算平均身高
"""
# sum = 0
# for i in range(5):
#     sum += int(input("请输入身高："))
# print("平均身高为：" + str(sum / 5))

sum = 0
count = 0
while True:
    height = input("请输入身高：")
    if height == "":
        break
    else:
        sum += int(height)
        count += 1
print("平均身高为：" + str(sum / count))
