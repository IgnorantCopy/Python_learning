"""
Created by Ignorant on 2024/2/5
Description: __init__.py
"""

'''
do while importing a package

functions:
    > put some initializing variables / functions / classes in __init__.py while importing a package
    > calling the variables / functions / classes in __init__.py just through <package name>.<argument>
    > 
'''
__all__ = ['model']


def create():
    print("create __init__")
