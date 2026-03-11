#===================Python基本数据类型===================
'''
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)

===================标准数据类型===================
Python3中常见的标准数据类型有以下几种：
1. 数值（Number）
2. 字符串（String）
3. 布尔值（Boolean）
4. 列表（List）
5. 元组（Tuple）
6. 集合（set）
7. 字典（Dictionary）

python3的6个标准数据类型中：
不可变数据：Number（int、float、complex）、String（字符串）、Tuple；
可变数据：Lis（列表）、Dic（字典）、Set（集合）；
此外还有一些高级的数据类型，如：文件、函数、模块、类等。

===================Number类型=====================

Number类型：
python3中支持int、float、complex三种数值类型。
int类型：整数，如：1、2、3、4、5等。
float类型：浮点数，如：3.14、2.5、1.0等。
complex类型：复数，如：3+2j、4-5j等。
内置的type（）可以用来查询变量的类型。
例如：
a = 100
print(type(a)) # <class 'int'>
此外还能用isinstance()函数来判断变量是否为某种类型。
例如：
a = 100 
print(isinstance(a, int)) # True
打印为True，说明a是int类型。

isinstance和type的区别：
type（）不会认为子类是一种父类类型，不考虑继承关系。
isinstance（）会认为子类是一种父类类型，考虑继承关系。

数值运算：
python3支持四则运算、比较运算、位运算、逻辑运算等。
例如：
5 + 4 = 9 加法
5 - 4 = 1 减法
5 * 4 = 20 乘法
5 / 4 = 1.25 除法
5 // 4 = 1 取整除法
5 % 4 = 1 取余数
5 ** 4 = 625 幂运算
5 > 4 = True 大于
5 < 4 = False 小于
5 == 4 = False 等于
5!= 4 = True 不等于
5!= 4 = True 不等于
5 >= 4 = True 大于等于
5 <= 4 = False 小于等于

注意：
1、python可以同时为多个变量赋值，如：a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的数据，如：a = 100，a = "runoob"。
3、数值的除法包含两个运算符：/返回一个浮点数，//返回一个整数。
4、在混合运算中python会首先把数字转换为浮点数，然后再进行运算。
5、python还支持复数，复数是由实数部分和虚数部分构成的，可以用a+bj的形式表示

===================String类型=====================
String类型：
Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
字符串的截取的语法格式如下：
变量[头下标:尾下标]

索引值以 0 为开始值，-1 为从末尾的开始位置。
加号（+）用于字符串的拼接，星号（*）用于重复输出字符串。
str = 'Runoob'  # 定义一个字符串变量
print(str)           # 打印整个字符串
print(str[0:-1])     # 打印字符串第一个到倒数第二个字符（不包含倒数第一个字符）
print(str[0])        # 打印字符串的第一个字符
print(str[2:5])      # 打印字符串第三到第五个字符（不包含索引为 5 的字符）
print(str[2:])       # 打印字符串从第三个字符开始到末尾
print(str * 2)       # 打印字符串两次
print(str + "TEST")  # 打印字符串和"TEST"拼接在一起

Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
>>> print('Ru\noob')
Ru
oob
>>> print(r'Ru\noob')
Ru\noob
>>>

===================Boolean类型=====================
布尔类型即 True 或 False。
在 Python 中，True 和 False 都是关键字，表示布尔值。
布尔类型可以用来控制程序的流程，比如判断某个条件是否成立，或者在某个条件满足时执行某段代码。
布尔类型特点：
布尔类型只有两个值：True 和 False。
布尔是int的子类型，可以进行数值运算。因此布尔可以被看作整数来使用，其中 0 表示 False，其他值表示 True。
布尔类型可以和其他数据类型进行比较，比如数字、字符串、列表等。在比较时True会被转换为1，False会被转换为0。
布尔类型可以和逻辑运算符（and、or、not）进行逻辑运算。这些运算符号可以用来组合多个布尔值，并返回一个新的布尔值。
布尔类型也能转换成其他数据类型，比如字符串、整数等。在转换的时候，True会被转换为1，False会被转换为0。
可以使用bool()函数将其他数据类型转换为布尔类型。以下值转换成布尔类型时，结果为True：
非零数值、非空字符串、非空列表、非空元组、非空集合、非空字典等。
以下值转换成布尔类型时，结果为False：
0、空字符串、空列表、空元组、空集合、空字典、None、False。

例如：
# 布尔类型的值和类型
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

# 布尔类型的整数表现
print(int(True))   # 1
print(int(False))  # 0

# 使用 bool() 函数进行转换
print(bool(0))         # False
print(bool(42))        # True
print(bool(''))        # False
print(bool('Python'))  # True
print(bool([]))        # False
print(bool([1, 2, 3])) # True

# 布尔逻辑运算
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 布尔比较运算
print(5 > 3)  # True
print(2 == 2) # True
print(7 < 4)  # False

# 布尔值在控制流中的应用
if True:
    print("This will always print")
    
if not False:
    print("This will also always print")
    
x = 10
if x:
    print("x is non-zero and thus True in a boolean context")
    
注意：在python中，所有非0的数字和非空的字符串、列表、元组等都会被视为True，只有0、空字符串、空列表、空元组、空集合、空字典、None、False都被视为False。
因此，在进行布尔值转换的时候，需要注意数据类型的准确性；

===================List类型=====================
List类型：
List 是 Python 中使用最频繁的数据类型。
List 是一种有序的集合，可以随时添加和删除其中的元素。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表
列表的截取的语法格式如下：
变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。
加号（+）用于列表的拼接，星号（*）用于重复输出列表。
如以下实例：
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]  # 定义一个列表
tinylist = [123, 'runoob']

print (list)            # 打印整个列表
print (list[0])         # 打印列表的第一个元素
print (list[1:3])       # 打印列表第二到第四个元素（不包含第四个元素）
print (list[2:])        # 打印列表从第三个元素开始到末尾
print (tinylist * 2)    # 打印tinylist列表两次
print (list + tinylist)  # 打印两个列表拼接在一起的结果


'''