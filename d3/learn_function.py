#函数
#基础函数
def calculate_salary(base, bonus):
    total = base + bonus
    print(f'月薪总计：{total}元')
    return total
salary = calculate_salary(15000,5000)
#位置参数、默认参数、可变参数、命名关键字参数、关键字参数
#递归函数

#定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
#然后，在缩进块中编写函数体，函数的返回值用return语句返回。


#小结
#可变参数和关键字参数的语法：
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。
#调用函数时如何传入可变参数和关键字参数的语法：
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})
#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值
#定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数

"""
help(abs)
help(hex)
n1 = 255
n2 = 1000
print(str(hex(n1)))
print(str(hex(n2)))
"""

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    if x < 0:
        return -x
print(my_abs(-678))

#pass 占位符
#raise 语句用于手动引发异常
import math
def quadratic(a, b, c):
    if not (isinstance(a, (int, float)) or isinstance(b, (int, float)) or isinstance(c, (int, float))):
        raise TypeError('bad operand type')
    x1 = (-b + math.sqrt((b*b)-(4*a*c)))/(2*a)
    x2 = (-b - math.sqrt((b*b)-(4*a*c)))/(2*a)
    x = (x1,x2)
    return x
 
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

# 位置参数
def power(x): #x -> 位置参数
    return x*x

# 默认参数 默认参数必须指向不变对象！
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
s=[1,2,3]
print(add_end(s))

# 可变参数
def calc(*numbers): # * 收集多个位置参数为一个元组（打包）
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum
print(calc(1,2,3))
nums = [1,2,3]
print(calc(*nums))# *将可迭代对象解包为多个位置参数（解包）

#关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:',name,'age:',age,'others',kw)
extra = {'city':'Beijing','job':'Engineer'}
person('jack',24,**extra)

#命名关键字参数
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)
person('jack',24,city='Beijing',job='Engineer')
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
def person(name,age,*args,city,job):
    print(name,age,args,city,job)

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

def mul(*args):
    if len(args)==0:
        raise TypeError
    mul = 1
    for a in args:
        mul = mul*a
    return mul

print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')

#递归函数
# 函数内部，可以调用其他函数。
# 如果一个函数在内部调用自身本身，这个函数就是递归函数
def fact(n):
    if n==1:
        return 1
    
    return n*fact(n-1)
print(fact(5))

#尾递归
# 函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，
# 使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
# BUT Python解释器也没有做优化
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return 1
    return fact_iter(num-1,num*product)
#print(fact(1000))

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)

move(2, 'A', 'B', 'C')


