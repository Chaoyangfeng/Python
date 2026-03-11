#===================学习===================
"""
------------------------------------------
标识符：
第一个字符必须以字母（a-z, A-Z）或下划线 _ 。
标识符的其他的部分由字母、数字和下划线组成。    
标识符对大小写敏感，count 和 Count 是不同的标识符。
标识符对长度无硬性限制，但建议保持简洁（一般不超过 20 个字符）。    
禁止使用保留关键字，如 if、for、class 等不能作为标识符。

合法的标识符命名：
age = 25 普通的变量名
user_name = "Alice" 用下划线连接的变量名
_name = "Bob" 单个下划线开头的变量名，通常内部使用或者私有变量
__name = "Charlie" 双下划线开头的变量名，有特殊含义，一般用于系统内部使用
MAX_VALUE = 100 全部大写一般用于常量，表示一个固定值不会改变的变量；
calculate_sum = lambda x, y: x + y 匿名函数的命名，动词+名词
StudentInfo = {"name": "Alice", "age": 25} 驼峰命名法，多个单词的变量名，首字母大写，后续单词首字母小写。

非法的标识符命名：
1name = "Alice" 数字开头的变量名，不符合命名规范
name-age = "Bob" 连字符的变量名，不符合命名规范
name!age = "Charlie" 特殊字符的变量名，不符合命名规范
calculate-sum = lambda x, y: x + y 匿名函数的命名，动词+名词，不符合命名规范
等等；

备注：
python3允许使用中文和Unicode以及非ASCII字符作为标识符，但不建议这么做。
例如：
中文：名字 = "张三"
Unicode：名字 = "你好，世界"
非ASCII字符：名字 = "こんにちは，世界"

测试标识符是否合法：
def is_valid_identifier(name):
    try:
        exec(f"{name} = None")
        return True
    except:
        return False

print(is_valid_identifier("2var"))  # False
print(is_valid_identifier("var2"))  # True
------------------------------------------

python的保留关键字：
and、as、assert、break、class、continue、def、del、elif、else、except、
False、finally、for、from、global、if、import、in、is、lambda、None、
nonlocal、not、or、pass、raise、return、True、try、while、with、yield。 

逻辑值：
true 和 false 是python的两个逻辑值，它们的类型是 bool。
None 是一个特殊的逻辑值，表示空值或无值。

逻辑运算符：
and、or、not 是python的逻辑运算符。

条件运算符：
if 条件判断语句后面可以跟一个条件表达式，条件表达式的结果为 True 或 False。
elif 否则如果分支语句，只有前面的条件判断不成立时才执行。
else 否则分支语句，当所有条件判断都不成立时执行。

循环控制语句：
for 循环语句，用于遍历序列或其他可迭代对象。
while 循环语句，用于循环执行一段代码，直到条件判断为 False。    
break 语句，用于跳出循环。
continue 语句，用于跳过当前循环的剩余语句，开始下一轮循环。
try 语句，用于捕获异常并处理异常。
except 语句，用于处理 try 语句中捕获到的异常。
finally 语句，用于在 try-except 代码块执行完毕后执行一些代码，无论是否有异常发生。无论发生什么异常，finally 语句都会执行。
raise 语句，用于抛出异常。

函数定义：
def 定义函数的关键字，后面跟函数名，括号中可以指定函数的参数。def 函数名(参数1, 参数2, ...):
return 语句，用于返回函数的结果。
lambda 表达式，用于创建匿名函数。

类与对象：
class 定义类，后面跟类名。class 类名:
del 语句，用于删除对象。

模块导入：
import 语句，用于导入模块。
from 语句，用于从模块中导入指定的对象。
as 语句，用于给模块或对象指定别名。

作用域：
global 语句，用于声明全局变量。
monlocal 语句，用于声明局部变量。一般用于嵌套函数内部。

异步编程：
async 定义异步函数，后面跟函数名。async def 函数名(参数1, 参数2, ...):
await 语句，用于等待异步函数的结果。

其他：
assert 语句，用于断言。
in 运算符，用于判断元素是否在序列中，或者检查成员关系。
is 运算符，用于判断两个对象是否是同一个对象。
pass 语句，用于占位符。
with 语句，用于上下文管理，资源管理。
yeild 语句，用于生成器。从生成器中返回的值，可以赋值给变量。

------------------------------------
注释：
单行注释以 # 开头。
多行注释以 '''''' 或 """"""开头，并以相同的符号结尾
-----------------------------------

行与缩进：
python是用缩进来表示代码块，相同缩进表示代码在同一个代码块中。
python的缩进规则是4个空格，不要使用tab。

------------------------------------
多行语句：

python通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠（\）来实现多行语句。
例如：
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three   # 多行语句
print(total)  # 6

在[]{}()中的多行语句，不需要使用反斜杠。例如：
my_list = [1, 2, 3,
           4, 5, 6]
my_dict = {'name': 'Alice', 'age': 25,
           'city': 'Beijing'}
my_tuple = (1, 2, 3,
           4, 5, 6)


-------------------------------------
数字类型（number）：
python有四种数字类型：整数、布尔值、浮点数、复数:

int 整数类型，没有大小限制，可以是正数、负数、0。
bool 布尔值类型，只有True、False两种值。
float 浮点数类型，用来表示小数。        
complex 复数类型，用来表示复数，由实数部分和虚数部分构成。

字符串(string) ：
字符串是python中最常用的基本类型，用单引号(')或双引号(")括起来的任意文本。或者使用三引号'''或""括起来的多行文本。

转义符 '\' 用来转义特殊字符，反斜杠 '\' 后面可以跟 'n' (换行)、 't' (制表符)、 'r' (回车)、 'b' (退格)、 'f' (换页)、 '"' (双引号)、 "'" (单引号)、 'uXXXX' (16进制Unicode字符) 等。
使用r前缀可以让字符串中的反斜杠不被转义。如 r"this is a line with \n" 则\n会显示，并不是换行。

使用字面意义级连接字符串，如"Hello" "World"，会自动用空格连接。会转换成字符串"Hello World"。

字符串可以使用+运算符连接，也可以使用*运算符重复。

字符串的索引有两种方式，从左往右以0开始，从右往左以-1开始。

字符串的切片操作，语法为"[start:end:step]"，start表示切片开始的索引，默认为0，end表示切片结束的索引，默认为字符串长度，step表示切片的步长，默认为1。
例如："hello world"[0:5:2] 结果为"hlow"。

字符串的格式化，语法为"{} {}".format(value1, value2)，其中value1、value2为要格式化的变量。

字符串的常用方法：
str = '123456789'
print(str）  # 输出字符串
print(str[0:-1])  # 输出字符串的第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串的第一个字符
print(str[2:5])  # 输出字符串的第三个到第五个的所有字符
print(str[2:])  # 输出从第三个字符开始的所有字符
print(str * 2)  # 输出字符串两次
print(str[1:5:2])  # 输出字符串的第二个到第五个的每两个字符,步长为2
print(str+'hello')  # 连接字符串
print('hello\nworld') # 使用反斜杠换行+n转义字符
print(r'hello\nworld')# 使用r前缀，不转义反斜杠

--------------------------------------

空行：
函数之间或类之间用空行分隔，表示一段新的代码块的开始。类和函数入口之间也用一行空行。用来突出函数入口的开始
空行和代码的缩进不同，空行不是python语法的一部分，而是用来美化代码的。书写的时候可以不加空行，但是为了美观，还是建议加上空行。记住：空行是python语法的一部分。

--------------------------------------
同一行显示多条语句：
python允许同一行显示多条语句，语句之间使用分号 ; 分隔。例如：
x = 1; y = 2; z = 3;

--------------------------------------
多个语句能够构建成一个代码组
缩进相同的一组语句构成一个代码块，像if、while、def、class这类复合语句首行都是以关键字开始的，后面跟一个代码块。
例如：
if expression:
    suite1
elif expression:
    suite2
else:
    suite3

--------------------------------------
print 输出
print 输出语句可以输出多个值，多个值之间用逗号隔开。同时print默认是换行输出，如果要实现不换行输出，可以结合end参数和sep参数一起使用。
例如：
print(value1, value2, value3, sep=' ', end=' ')

--------------------------------------
import和from...import
在python中使用import和from...import语句可以导入模块。
将整个模块(module)导入，格式为：import module_name。
从某个模块中导入某个函数或变量，格式为：from module_name import function_name。
从某个模块中导入多个函数或变量，格式为：from module_name import function1, function2, function3。
将某个模块中的全部函数或变量导入，格式为：from module_name import *。

例如：
导入sys模块
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

导入sys模块的argv，path成员
from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path


"""
