
# 函数
# def say_hello():
#     print('hello world')
# say_hello()
# say_hello()

# 函数参数

# def print_max(a,b):
#     if a>b:
#         print(a,'is maximum')
#     elif a==b:
#         print(a,'is equal to',b)
#     else:
#         print(b,'is maximum')

# print_max(3,4)

# x=5
# y=7
# print_max(x,y)

# 局部变量

# x=50
# def func(x): 
#     print('x is ',x)
#     x=2
#     print('Changed local x to ',x)

# func(x)
# print('x is still',x)


# global语句

# x=50

# def func():
#     global x
#     print('x is ',x)
#     x=2
#     print('Changed global x to',x)

# func()
# print('Value of x is',x)


# 默认参数值
# def say(message,times=1):
#     print(message*times)
# say('hello')
# say('world',5)

# 关键字参数
# def func(a,b=5,c=10):
#     print('a is',a,'and b is',b,'and c is',c)
# func(3,7)
# func(25,c=24)
# func(c=50,a=100)

# 可变参数
# def total(a=5,*numbers,**phonebook):
#     print('a',a)

#     for single_item in numbers:
#         print('single_item',single_item)
    
#     for first_part,second_part in phonebook.items():
#         print(first_part,second_part)
# print(total(10,1,2,3,jack=1123,john=2231,Inge=1560))


# return 语句

# def maximum(x,y):
#     if x>y:
#         return x
#     elif x==y:
#         return 'The numbers are equal'
#     else:
#         return y
# print(maximum(2,3))

# def some_func():
#     pass
# print(some_func())

def print_max(x,y):
    '''Prints the maximum of two numbers.打印两个数值中的最大值。

    The two values must be integers.这两个数都应该是整数。'''

    x=int(x)
    y=int(y)

    if x>y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')

print_max(3,5)
print(print_max.__doc__)

