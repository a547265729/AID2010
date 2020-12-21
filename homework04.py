"""
(选做)一个小球从100m高度落下,每次弹回原高度一半.
   计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)
    -- 全过程总共移动多少米?
"""
final_height = 0.01
height = 100
count = 0
s = 100
while height/2 >= final_height:
    s += height
    height /= 2
    count += 1
print("总共弹起%d次" % count)
print("总共弹起%.2f米" % s)
