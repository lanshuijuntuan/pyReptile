# for循环

for i in range(1,5):
    print(i)
else:
    print("The for loop is over")


# break语句

while True:
    s=input('Enter something:')
    print(s)
    if s=='quit':
        print("input value is {0}".format(s))
        break
    print('Length of the string is {0}'.format(len(s)))
print('Done')


# continue语句

while True:
    s=input("Enter something:")
    if s=='quit':
        break
    if len(s)<3:
        print('Too Small')
        continue
    print('Input is of sufficient length')