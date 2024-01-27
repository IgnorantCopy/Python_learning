"""
Created by Ignorant on 2024/1/25
Description: Function Annotation
"""


def login(name, password):
    """
    用户登录
    :param name: 用户名
    :param password: 密码
    :return: 是否登录成功
    """
    if name == "Admin" and password == "mkh123":
        print("login successfully")
        return True
    print("login failed")
    return False


print(login("Admin", "mkh123"))
