"""
Created by Ignorant on 2024/1/18
Description: Exercise 1
    用户注册
    用户名：全部小写，首字母不能是数字，长度必须六位以上
    手机号码：11位数字
    密码：6位数字
"""

name = input("please enter your name: ")
phone = input("please enter your phone number: ")
password = input("please enter your password: ")
if ((name.islower() and not name[0].isdigit() and len(name) > 6) and (phone.isdigit() and len(phone) == 11)
        and (password.isdigit() and len(password) == 6)):
    print("welcome")
else:
    print("invalid")
