#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#输入输出， 
#数据类型、变量、常量（通常全大写表示、None，
#转义 \ 、r''
# /、//、%
#list、tuple、dict、set
#条件判断 if、elif、else
#模式匹配 match 
#循环 for x in 、while

# name = input('please enter your name:')
# print('nihao',name)
print('1024 * 768 =' , 1024 * 768  )

a1 = -100
if a1 >= 0:
    print(a1)
else:
    print(-a1)


    #转义字符\  I'm "OK"!
    #  r''字符串默认不转义
print("I'm \"OK\"!")
print(r'\\\t\\')
print('''
      line1
      line2
      line3''')
print(r'''hello,\n
      world''')
#数据类型：整数，浮点数，字符串，布尔
#空值None
print(None)
_a_1 = 1

#除法   / 结果为浮点 
#地板除 //结果为整型 
#求余数 %
print('10/3=',10/3,'\n10//3=',10//3,'\n10%3=',10%3)

n = 123 
f = 123.21321 
s1 = 'hello,world'
s2 = 'hello,\'adam\''
s3 = r'hello,"bart"' 
s4= r'''hello,
bob!'''
print('n =',n,
      '\nf =',f,
      '\ns1 =',s1,
      '\ns2 =',s2,
      '\ns3 =',s3,
      '\ns4 =',s4)

name = '斩首战士'
day = 2
salary =  30000.5
is_angry = True
print(f'我是{name},第{day}天作战，目标月薪{salary},愤怒状态:{is_angry}')

#list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
classmates.append('stdephn')
print(classmates)
classmates.pop()
print(classmates)
classmates.insert(1,'jim')
print(classmates)
classmates[1] = 'sam'
print(classmates)
print(len(classmates))
#tuple
# tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates_01 = ('Michael', 'Bob', 'Tracy')
print(classmates_01)

#dict 
# key-value形式
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d.get('Bob'))
d.pop('Bob')
#set
# set和dict类似，也是一组key的集合，但不存储value
s = set([1, 2, 3])
print(len(s))
s = {1, 1, 2, 2, 3, 3}
print(s)
s.add(4)
print(s)
s.remove(4)

#条件判断 if、elif、else
#模式匹配match 
# match可以嵌套进条件判断的else:后，而且match后还能嵌套if条件判断

'''
b=input('b:')
if b <= 200 :
    print(True)
else:
    print(False)
'''

"""
while(1):
    a = int(input('Enter a number'))
    if a > 100:
        print('a>100')
    else:
        match a:
            case a if a < 50:
                print('a<50')
            case 50:
                print('a=50')
            case 100:
                print('a=100')
            case a if 50 < a < 100:
                if a < 80:
                    print('50<a<80')
                else:
                    print('80<=a<100')
            case _:
                print('Error')
"""

"""
height = float(input('请输入身高：'))
weight = float(input('请输入体重：'))
bmi = (weight/(height*height))
print(bmi)
if bmi < 18.5:
    print('过轻')
elif (bmi >= 18.5) & (bmi <  25):
    print('正常')
elif (bmi >= 25) & (bmi < 28):
    print('过重')
elif (bmi >= 28) & (bmi < 32):
    print('肥胖')
else :
    print('严重肥胖')
"""

#循环 for x in
#while
sum = 0
for x in range(101):
    sum += x
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print(f'hello,{x}')

n = 1
while n < 101:
    if n == 10:
        continue
    if n > 10:
        break
    print(n)
    n=n+1
  
