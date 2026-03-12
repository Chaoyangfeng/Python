'''
Author: chaoyangfeng 1090098083@qq.com
Date: 2026-03-12 10:35:32
LastEditors: chaoyangfeng 1090098083@qq.com
LastEditTime: 2026-03-12 13:33:28
FilePath: \Personal_Learning\Python学习\C_数据类型转换.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
===========================数据类型转换============================
数据类型转换：
数据类型转换是指将一种数据类型转换为另一种数据类型。
数据类型转换有两种方式：
1. 强制类型转换：将一种数据类型转换为另一种数据类型，需要使用强制类型转换符号。
2. 自动类型转换：Python会自动将某些数据类型转换为另一种数据类型。

Python支持以下数据类型转换：

隐式类型转换：
在隐式类型转换中，Python 会自动将一种数据类型转换为另一种数据类型，不需要我们去干预。
以下实例中，我们对两种不同类型的数据进行运算，较低数据类型（整数）就会转换为较高数据类型（浮点数）以避免数据丢失
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int 数据类型为:",type(num_int))
print("num_flo 数据类型为:",type(num_flo))

print("num_new 值为:",num_new)
print("num_new 数据类型为:",type(num_new))

输出：
num_int 数据类型为: <class 'int'>
num_flo 数据类型为: <class 'float'>
new_num 值为: 135.23
new_num 数据类型为: <class 'float'>

代码解析：
实例中我们对两个不同类型的数据进行num_int和num_flo进行加法运算，由于num_int是整数，而num_flo是浮点数，因此Python会自动将num_int转换为num_flo类型，以避免数据丢失。
然后查看三个变量的数据类型，num_int为整数，num_flo为浮点数，num_new为浮点数。
在输出中，我们看见num_int是整形，num_flo是浮点型，num_new是浮点型。
同样，新的变量num_new的值是浮点型，这是python会将较小的数据类型转换成较大的数据类型，以避免数据丢失。
我们在看一个实例，整型数据和字符串型数据进行相加运算，会发生什么情况？ 

num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("num_str 数据类型为:",type(num_str))

print(num_int+num_str)

输出：
num_int 数据类型为: <class 'int'>
num_str 数据类型为: <class'str'>
Traceback (most recent call last):
    File "C_数据类型转换.py", line 11, in <module>
    print(num_int+num_str)
TypeError: unsupported operand type(s) for +: 'int' and'str'

从输出中可以看出，整型和字符串类型运算结果会报错，输出 TypeError。 Python 在这种情况下无法使用隐式转换。
但是，Python 为这些类型的情况提供了一种解决方案，称为显式转换。

显式类型转换：
在显式类型转换中，用户将对象的数据类型转换为所需的数据类型。 我们使用 int()、float()、str() 等预定义函数来执行显式类型转换。
案例：
int() 强制转换为整数
x = int(1)   # x 输出结果为 1
y = int(2.8) # y 输出结果为 2
z = int("3") # z 输出结果为 3

float() 强制转换为浮点数
x = float(1)     # x 输出结果为 1.0
y = float(2.8)   # y 输出结果为 2.8
z = float("3")   # z 输出结果为 3.0
w = float("4.2") # w 输出结果为 4.2

str() 强制转换为字符串
x = str("s1") # x 输出结果为 's1'
y = str(2)    # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'

整型和字符串类型进行运算，就可以用强制类型转换来完成：
num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("类型转换前，num_str 数据类型为:",type(num_str))

num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:",type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:",num_sum)
print("sum 数据类型为:",type(num_sum))

输出：
num_int 数据类型为: <class 'int'>  
类型转换前，num_str 数据类型为: <class 'str'>  
类型转换后，num_str 数据类型为: <class 'int'>  
num_int 与 num_str 相加结果为: 579  
sum 数据类型为: <class 'int'>  

其他转换类型：
int（x，base=10）：将x转换为整数，base为进制数，默认为10。
float（x）：将x转换为浮点数。
complex（real，imag）：创建一个复数，real为实数部分，imag为虚数部分。
str（object）：将对象转换为字符串。
repr（object）：将对象转换为表达式字符串。
eval（string）：将字符串转换为表达式并求值。
tuple（sequence）：将序列转换为元组。
list（sequence）：将序列转换为列表。
set（sequence）：将序列转换为集合。
dict（mapping）：将映射转换为字典,必须是一个序列(key,value)元组。
frozenset（sequence）：将序列转换为不可变集合。
chr(x): 将整数x转换为字符。
ord(x): 将字符x转换为整数。
hex(x): 将整数x转换为十六进制字符串。
oct(x): 将整数x转换为八进制字符串。
    
    
    
    
    
    
    
    
    
"""