"""
练习1：
在终端中录入一个内容,循环打印每个文字的编码值。
效果：
请输入文字：qtx
113
116
120
"""
text = input("请输入文字：")
for item in text:
    print(ord(item))
    