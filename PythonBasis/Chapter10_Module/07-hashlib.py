"""
Created by Ignorant on 2024/2/6
Description: Module hashlib
"""
import hashlib

message = 'Hello World!'
# md5
print(hashlib.md5(message.encode('utf8')).hexdigest())
# sha1
print(hashlib.sha1(message.encode('utf8')).hexdigest())
# sha256
print(hashlib.sha256(message.encode('utf8')).hexdigest())

password = "123456"
password = hashlib.sha256(password.encode('utf8')).hexdigest()
trial = input("Enter your password: ")
trial = hashlib.sha256(trial.encode('utf8')).hexdigest()
if password == trial:
    print("Password matches!")
