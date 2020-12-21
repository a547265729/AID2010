"""
汇率转换器
"""
# 输入美元
usd = float(input("请输入美元："))

# 逻辑处理
cny = usd * 6.7

# 输出人民币数量
print(str(usd) + "美元 = " + str(cny) + "人民币")
