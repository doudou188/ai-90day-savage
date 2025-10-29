#类和实体
#数据封装
#继承、多态
#type()、 types
# isinstance()
# dir()


#特殊方法__init__前后分别有两个下划线！！！
#__init__方法的第一个参数永远是self，表示创建的实例本身，
# 因此，在__init__方法内部，就可以把各种属性绑定到self，
# 因为self就指向创建的实例本身

#有了__init__方法，在创建实例的时候，就不能传入空的参数了，
# 必须传入与__init__方法匹配的参数，
# 但self不需要传，Python解释器自己会把实例变量传进去
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
        print(f'{self.name}:{self.score}')
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
print(bart.name)
bart.print_score()
lisa.print_score()

#数据封装
#变量名如果以__开头，就变成了一个私有变量（private）

#在Python中，变量名类似__xxx__的，
# 也就是以双下划线开头，并且以双下划线结尾的，是特殊变量
# 特殊变量是可以直接访问的，不是private变量，
# 所以，不能用__name__、__score__这样的变量名
class Student(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score
    def print_score(self):
        print(f'{self._name}:{self._score}')
    def get_name(self):
        return self._name
    def get_score(self):
        return self._score
    def set_name(self, name):
        self._name = name
    def set_score(self, score):
        if 0 <= score <= 100:
            self._score = score
        else:
            raise ValueError('bad score')
        
class Student1(object):
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender
    def get_name(self):
        return self._name
    def get_gender(self):
        return self._gender
    def set_name(self, name):
        self._name = name
    def set_gender(self, gender):
        self._gender = gender

bart = Student1('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

#继承
#面向对象编程当我们定义一个class的时候，可以从某个现有的class继承，
# 新的class称为子类（Subclass），
# 而被继承的class称为基类、父类或超类（Base class、Super class)
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
dog = Dog()
dog.run()
#多态
#方法重写和向上转型。
class cat(Animal):
    def run(self):
        print('cat is running...')

#静态语言 vs 动态语言
#对于静态语言（例如Java）来说，如果需要传入Animal类型，
# 则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

#对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以了
class Timer(object):
    def run(self):
        print('Start...')
#动态语言的“鸭子类型”，它并不要求严格的继承体系，
# 一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

#Python的“file-like object“就是一种鸭子类型。
# 对真正的文件对象，它有一个read()方法，返回其内容。
# 但是，许多对象，只要有read()方法，都被视为“file-like object“。
# 许多函数接收的参数就是“file-like object“，
# 你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。


#type()、 types
#判断对象类型,基本类型，函数，类
#返回对应的Class类型
print(f'{type(123)}{type('str')}{type(None)}')
print(type(abs))
#types 模块中定义的常量 判断是否是函数
import types
def fn():
    pass
print(type(fn))
print(types.FunctionType)
type(fn)==types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType
type((x for x in range(10)))==types.GeneratorType
# isinstance()
# 判断一个对象是否是某种类型
class Husky(Dog):
    pass
a = Animal()
d = Dog()
h = Husky()
print(isinstance(h,Husky))  #True
print(isinstance(h,Animal)) #True
print(isinstance(d,Husky))  #False
#并且还可以判断一个变量是否是某些类型中的一种，
# 比如下面的代码就可以判断是否是list或者tuple
isinstance([1, 2, 3], (list, tuple)) #True

# dir()
#获得一个对象的所有属性和方法，返回一个包含字符串的list
#print(dir('ABC'))
#配合getattr()、setattr()、hasattr()
# 我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__ (self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
hasattr(obj,'x')# 有属性'x'吗？
hasattr(obj,'y')# 有属性'y'吗？
setattr(obj,'y',19)# 设置一个属性'y'
getattr(obj,'y')# 获取属性'y'
hasattr(obj,'power')# 有函数'power'吗？
#如果试图获取不存在的属性，会抛出AttributeError的错误：
#可以传入一个default参数，如果属性不存在，就返回默认值
getattr(obj,'n',404) # 获取属性'z'，如果不存在，返回默认值404

#实例属性和类属性
#可以直接在class中定义属性，这种属性是类属性，归Student类所有
#但类的所有实例都可以访问到
class Student(object):
    name = 'Student'
s = Student()
print(s.name)

class Student3(object):
    count = 0
    def __init__(self, name):
        self._name = name
        Student3.count += 1

if Student3.count != 0:
    print('测试失败!')
else:
    bart = Student3('Bart')
    if Student3.count != 1:
        print('测试失败!')
    else:
        lisa = Student3('Bart')
        if Student3.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student3.count)
            print('测试通过!')


class CodeWarrior:
    def __init__(self, name, target_salary):
        self.__name = name
        self.__target_salary = target_salary
        self.skills = []

    def learn_skill(self,skill):
        self.skills.append(skill)
        print(f'{self.__name}学会了{skill}')
            
    def show_target(self):
        print(f'{self.__name}的目标薪资是：{self.__target_salary}元')

warrior = CodeWarrior('斩首战士',30000)
warrior.learn_skill('Python面向对象')
warrior.show_target
                      




    