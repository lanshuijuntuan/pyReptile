# 数据结构 

# list

shoplist=['apple','mango','carrot','banana']

print('I hava',len(shoplist),'item to purchase.')

print('These items are:',' ')

for item in shoplist:
    print(item,' ')

print('\n also have to buy rice ')
shoplist.append('rice')
print('My shopping list is ',shoplist)

print('I will sort my list now')

shoplist.sort()

print('Sorted shopping list is',shoplist)

print('The first item I will buy is',shoplist[0])
olditem=shoplist[0]
del shoplist[0]

print('I bought the',olditem)
print('My shopping list is nov',shoplist)


# 元组

zoo=('python','elephant','penguin')
print('Number of animals in the zoo is',len(zoo))

new_zoo='monkey','camel',zoo

print('Number of animals in the new zoo is',len(new_zoo))
print('All animals in new zoo are',new_zoo)
print('Animals brought from old zoo are',new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is',
    len(new_zoo)-1+len(new_zoo[2]))


# 字典

ab={
    'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larray@mail.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'
}
print("Swaroop's address is",ab['Swaroop'])

del ab['Spammer']

print('\n There are {} contacts in the address-book \n'.format(len(ab)))

for name,address in ab.items():
    print('Contact {} at {}'.format(name,address))

ab['Guido']='guido@python.org'

if 'Guido' in ab:
    print("\n Guido's address is",ab['Guido'])

# 序列
# index

shoplist=['apple','mango','carrot','banana']
name='swaroop'

print('Item 0 is ',shoplist[0])
print('Item 1 is ',shoplist[1])
print('Item 2 is ',shoplist[2])
print('Item 3 is ',shoplist[3])
print('Item -1 is ',shoplist[-1])
print('Item -2 is',shoplist[-2])
print('Character o is ',name[0])


# slicing on a list
print('Item 1 to 3 is',shoplist[1:3])
print('Item 2 to end is',shoplist[2:])
print('Item 1 to -1 is',shoplist[1:-1])
print('Item start to end is',shoplist[:])

# slicing on a string 
print('characters 1 to 3 is',name[1:3])
print('characters 2 to end is',name[2:])
print('characters 1 to -1 is',name[1:-1])
print('characters start to end is',name[:])

# 集合


bri=set(['brazil','russia','india'])
if 'india' in bri:
    print('india in bri')
else:
    print('india not in bri')

if 'usa' in bri:
    print('usa in bri')
else:
    print('usa not in bri')

bric=bri.copy()
bric.add('china')
if bric.issuperset(bri):
    print('bric is superset bri')
else:
    print('bric not is superset bir')
bri.remove('russia')

print(bri&bric)



# 引用

print('Simple Assignment')
shoplist=['apple','mango','carrot','banana']
mylist=shoplist

del shoplist[0]

print('shoplist is ',shoplist)
print('mylist is',mylist)

print('copy by making a full slice')
mylist=shoplist[:]
del mylist[0]

print('shoplist is',shoplist)
print('mylist is',mylist)


# 有关字符串的更多内容

name='Swaroop'

if name.startswith('Swa'):
    print('yes,the string starts with "swa"')

if 'a' in name:
    print('yes,it contains the string "a"')

if name.find('war')!=-1:
    print('yes,it contains the string "war"')

delimiter='_*_'
mylist=['Brazil','Russia','India','China']
print(delimiter.join(mylist))












