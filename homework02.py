"""
模拟登录
    如果账号的密码错误3次，提示锁定账户，效果如下：
        请输入账号：qtx
        请输入密码：1234
        登录失败
        你还剩余 2 次机会
        请输入账号：Qtx
        请输入密码：1234
        登录失败
        你还剩余 1 次机会
        请输入账号：Qtx
        请输入密码：123456
        登录成功
"""
count = 3
right_account = "Pqz"
right_pwd = "123456"
while count > 0:
    account = input("请输入账号:")
    pwd = input("请输入密码:")
    if account == right_account and pwd == right_pwd:
        print("登录成功")
        break
    else:
        print("登录失败")
        count-=1
        print(f"你还剩余 {count} 次机会")
else:
    print("锁定账户")

