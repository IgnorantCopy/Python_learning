"""
Created by Ignorant on 2024/2/4
Description: Multi-inheritance
"""
import inspect


class Base(object):
    def test(self):
        print('Base.test')


class A(Base):
    def test1(self):
        print('A.test1')


class B(Base):
    def test2(self):
        print('B.test2')


class C(Base):
    def test3(self):
        print('C.test3')


class D(A, B, C):
    pass


d = D()
# breadth first
print(inspect.getmro(D))  # solution order
