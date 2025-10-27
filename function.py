#函数
#定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
#然后，在缩进块中编写函数体，函数的返回值用return语句返回。

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