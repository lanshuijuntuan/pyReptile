print 'hello world 这是单引号的字符串；';

print "hello world  这是双引号字符串；";


print '''这是三引号字符串，此字符串可以是多行

胜多负少费


胜多负少

水电费

''';


'''

此处报错所以注释掉 
print "这是包含转义字符的字符串\ 
这也是第一行内容\  
这还是第一行内容"

'''
# 长字符串多行表示 
print "dsfsfsdf \
sdfsfsfs";


# 字符串格式化
age=28
name="Swaroop"

print("{0} was {1} years old when he wrote this book".format(name,age))

print("Why is {0} playing with that python".format(name))


print("{} was {} years old when he wrote this book".format(name,age))

print("Why is {} playing  with that python".format(name))

# 对于浮点数“0.333”保留小数点（.）后三位
print('{0:.3f}'.format(1.0/3))

# 使用下划线填充文本，并保持文字处于中间位置
# 使用（^）定义"_____hello____"字符串长度为11
print('{0:_^11}'.format('hello'))


# 注意 print 总是会以一个不可见的'新一行'字符（\n)结尾，
# 因此重复调用 print 将会在相互独立的一行中分别打印。
# 为防止打印过程中出现这一换行符，你可以通过 end 指定其结尾

# print('a',end='')  不支持

# print('b',end='')  不支持


# 转义序列

print('this is the first line \n this is the second line')

# 如果不需要转义请在字符串前面加r或者R来指定一个原始（Raw）字符串：

print(r"Newlines are indicated by \n")


# 使用变量与字面量
i=5
print(i)
i=i+1
print(i)

s='''This is a multi-line string.
This is the second line.'''

print(s)


# python是一种缩进严格的语言


# 以下缩进不严格会报错
# i=5
#   print（“Value is ”,i)
# print("I repeat,the value is",i)




