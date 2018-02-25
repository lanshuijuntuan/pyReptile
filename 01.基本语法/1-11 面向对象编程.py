# 面向对象编程

# __init__函数 self

class Person:


    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print(self.name)

p=Person('张三')

p.sayHi()

# 类变量和对象变量


class Robot:
    population=0

    def __init__(self,name):
        self.name=name
        print('initializing {}'.format(self.name))

        Robot.population+=1
    def die(self):

        print('{} is being destroyed'.format(self.name))

        Robot.population-=1

        if Robot.population==0:
            print('{} was the last one'.format(self.name))
        else:
            print('There are still {:d} robots working'.format(Robot.population))
        
    def say_hi(self):
        print('Greetings,my masters call me {}'.format(self.name))

    @classmethod
    def how_many(cls):
        print('we have {:d} robots.'.format(cls.population))

droid1=Robot('R2-02')
droid1.say_hi()
Robot.how_many()

droid2=Robot('C-3P0')
droid2.say_hi()
Robot.how_many()

print('\nRobots can do some work here.\n')

droid1.die()
droid2.die()

Robot.how_many()

# 继承

class SchoolMember:
    def __init__(self,name,age):
        '''代表相关学校里的成员'''
        self.name=name
        self.age=age
        print('Initialized SchoolMember:{}'.format(self.name))

    def tell(self):
        '''告诉我有关我的信息'''
        print('Name:{} Age: {} '.format(self.name,self.age,end=' '))

class Teacher(SchoolMember):
    '''代表一位老师'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('Initialized Teacher:{}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Salary {}'.format(self.salary))

class Student(SchoolMember):
    '''代表一位学生'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print('Initialized Student:{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks {}'.format(self.marks))

t=Teacher('Mrs.Shrividya',48,30000)
s=Student('Swaroop',25,75)

print('')

mermbers=[t,s]

for member in mermbers:
    member.tell()

