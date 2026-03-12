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

List 内置了有很多方法，例如 append()、pop() 等等，这在后面会讲到。
注意：
1、列表写在方括号 [] 之间、用逗号分隔开的元素列表。
2、和字符串一样，列表同样可以被索引和截取。
3、列表可以使用+运算符进行拼接，也可以使用*运算符进行复制。
4、列表中的元素类型可以不同，列表中的元素也可以是另一个列表。可以进行变更

如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
def reverseWords(input): 
      
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ") 
  
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样) 
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1] 
  
    # 重新组合字符串
    output = ' '.join(inputWords) 
      
    return output 
  
if __name__ == "__main__": 
    input = 'I like runoob'
    rw = reverseWords(input) 
    print(rw)
    
===================Tuple类型=====================
Tuple类型：
Tuple 和 List 类似，不同之处在于 Tuple 一旦初始化就不能修改。
Tuple 写在小括号 () 里、元素之间用逗号隔开。
元组中的元素类型也可以不相同。例如：

tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

以上实例输出结果如下：
('abcd', 786, 2.23, 'runoob', 70.2)
abcd
(786, 2.23)
(2.23, 'runoob', 70.2)
(123, 'runoob', 123, 'runoob')
('abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob')
元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
其实，可以把字符串看作一种特殊的元组。
>>> tup = (1, 2, 3, 4, 5, 6)
>>> print(tup[0])
1
>>> print(tup[1:5])
(2, 3, 4, 5)
>>> tup[0] = 11  # 修改元组元素的操作是非法的
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>

虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
如果你想创建只有一个元素的元组，需要注意在元素后面添加一个逗号，以区分它是一个元组而不是一个普通的值，这是因为在没有逗号的情况下，
Python会将括号解释为数学运算中的括号，而不是元组的表示。
如果不添加逗号，如下所示，它将被解释为一个普通的值而不是元组：
not_a_tuple = (42)
这样的话，not_a_tuple 将是整数类型而不是元组类型。
string、list 和 tuple 都属于 sequence（序列）

注意：
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用 + 操作符进行拼接。


===================Set类型=====================
Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。
集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。
另外，也可以使用 set() 函数创建集合。
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
parame = {value01,value02,...}
或者
set(value)

例如：
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

以上实例输出结果：
{'Zhihu', 'Baidu', 'Taobao', 'Runoob', 'Google', 'Facebook'}
Runoob 在集合中
{'b', 'c', 'a', 'r', 'd'}
{'r', 'b', 'd'}
{'b', 'c', 'a', 'z', 'm', 'r', 'l', 'd'}
{'c', 'a'}
{'z', 'b', 'm', 'r', 'l', 'd'}

===================Dictionary类型=====================
Dictionary（字典）类型：
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的
例如：
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

以上实例输出结果：
1 - 菜鸟教程
2 - 菜鸟工具
{'name': 'runoob', 'code': 1,'site': 'www.runoob.com'}
dict_keys(['name', 'code','site'])
dict_values(['runoob', 1, 'www.runoob.com'])

构造函数dic（）可以直接从键值对序列中构建字典。
例如：
>>> dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Runoob': 1, 'Google': 2, 'Taobao': 3}

{x: x**2 for x in (2, 4, 6)} 该代码使用的是字典推导式，更多推导式内容可以参考：Python 推导式。
另外，字典类型也有一些内置的函数，例如 clear()、keys()、values() 等。
注意：
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。




'''