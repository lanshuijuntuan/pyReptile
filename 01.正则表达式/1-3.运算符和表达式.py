# 运算符和表达式

# 加法运算
a=12
b=18
c=a+b
print(c)


# 减法运算

a=12
b=15
c=a-b
print(c)

# 乘法运算

a=12
b=22
c=a*b
print(c)

# 除法运算

a=12
b=3
c=a/b
print(c)

# 乘方运算

a=12
b=3
c=a**b
print(c)

# 整除

a=13
b=3
c=a//b
print(c)

a=-13
c=a//b
print(c)

# 取模

a=13
b=3
c=a%b
print(c)

a=-25.5
b=2.25
c=a%b
print(c)


# 左移

a=8
b=a<<2
print(b)

# 右移

a=11
b=a>>1
print(b)

# 按位与

a=5
b=3
c=a&b
print(c)

# 按位或
a=5
b=3
c=a|b
print(c)


# 按位异或

a=5
b=3
c=a^b
print(c)



# 按位取反

a=5
b=~a
print(b)

# 小于

a=13
b=3
print(b<a)


# 大于

a=3
b=13
print(b>a)

# 等于

a=3
b=3

print(a==b)


# 大于等于

a=4
b=5
print(b>=a)


# 小于等于

a=4
b=3
print(b<=a)

# 不等于
a=4
b=3
print(a!=b)

# not（布尔“非”）
a=4
b=3
print(not(a>b))

# or (布尔“或”)

a=4
b=3

print(a>b or a==3)

# and (布尔“与”)

a=4
b=3

print(a>b and a==3)


# 求值顺序
# lambda:lambda表达式
# if-else：条件表达式
# or：布尔“或”
# and：布尔“与”
# not x:布尔“非”
# in，not in，is，is not，<,<=,>,>=,!=,==:比较，包含成员资格测试
# （Memebership Tests）和身份测试（identify Tests)
# |:按位或
# ^：按位异或
# &：按位与
# <<,>>:移动
# +，-：加与减
# *，/,//,%:乘、除、整除、取余
# +x,-x,~x:正、负、按位取反
# **：求幂
# x[index],x[index:index],x[arguments...],x.attribute:下标、切片、调用、属性引用
# （expression...）,[expression...],{key:value...},{expression...}:显示绑定或
# 数组、显示列表、显示字典、显示设置

# 结合性

# 运算符通常由左至右结合。这意味着具有相同优先级的运算符将从左至右的
# 方式一次进行求值。如2+3+4将会以（2+3）+4的形式加以计算。

length=5
breadth=2

area=length*breadth
print("Area is {0}".format(area))
print("Perimeter is {0}".format(2*(length+breadth)))

