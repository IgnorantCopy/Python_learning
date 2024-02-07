"""
Created by Ignorant on 2024/2/5
Description: Singleton Pattern
"""


class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls)
        return cls.__instance


s1 = Singleton()
s2 = Singleton()
print(s1 == s2)
