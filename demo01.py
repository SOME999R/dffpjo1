 # "函数"
 # 两个正整数的和，差
def aa(num,num1):
    return num > 0 and num1 > 0
def add(num,num1):
    if aa(num,num1):
        # 只能在if中使用
        def ss(num,num1):
            return num + num1
        return ss(num,num1)

def j(num,num1):
    if aa(num,num1): #调用了判断是不是正整数的函数
        return num * num1
r = add(3,2)
r1 = j(3,9)
print(r)
print(r1)

def aa():
     def func1():
         print("aa")
     return func1
r = aa()
r()

# 函数嵌套使用
# 函数的位置，必须写在调用之前
# 在函数中定义函数并调用
# 函数的名称不能重复，会覆盖前面的
# 函数是通过函数名来调用，函数名是一个地址（变量）