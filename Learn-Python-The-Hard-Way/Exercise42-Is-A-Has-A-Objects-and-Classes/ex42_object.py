# -*- coding: utf-8 -*-

class Employee:

    # 类文档字符串
    '类的帮助信息'

    empCount = 0

    # 类似C++里面的构造函数，每创建一个实例，该函数需要执行一次用来初始化
    # self 自定义的实例参数，可更改
    # 类的方法和普通的函数只有一个特别的区别：他们必须有额外的第一个参数名称
    # 按照惯例使用self
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Emloyee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

    def test(self):
        print(self)
        print(self.__class__)



# 创建实例对象
y = Employee('ying', 1200)
t = Employee('ai', 1200)

# 访问属性
y.displayEmployee()
t.displayEmployee()

# empCount在外部内部都可以访问
print "Total Employee %d" % Employee.empCount

# 对self的测试理解
# self代表的是类的实例，代表当前对象地址，self.class则指向类
t.test()


# python的内置属性
# __doc__:类文档字符串
print "Employee.__doc__:", Employee.__doc__
# __name__:类名
print "Employee.__name__:", Employee.__name__
# __module__:类定义所在的模块(类的全名是'__main_.className', 如果
#     类位于一个导入模块sys中，那么className.__module__等于sys)
print "Employee.__module__:", Employee.__module__
# __bases__: 类的所有父类构成元素(包含了一个由所有父类组成的元祖)
print "Employee.__bases__:", Employee.__bases__
# __dict__:累的属性(包含一个字典，由类的数据属性组成)
print "Employee.__dict__:", Employee.__dict__




# 类的继承

class Parent1:
    parentAttr = 100
    def __init__(self):
        print "调用父类1构造函数"

    def parentMethod1(self):
        print "调用父类1方法"

    def setAttr(self, attr):
        Parent1.parentAttr = attr

    def getAttr(self):
        print "父类属性：", Parent1.parentAttr

class Parent2:
    def __init__(self):
        print "调用父类2构造函数"
    def parentMethod2(self):
        print "调用父类2方法"

class Child(Parent1, Parent2):
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print "调用子类方法child method"

c = Child()
c.childMethod()
c.parentMethod1()
c.parentMethod2()
c.setAttr(200)
c.getAttr()
