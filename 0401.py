# class A():
#     def __init__(self):
#         self.name = "haha"
#         self.age = 18
#     def fget(self):
#         print("我被录取了")
#         return self.name
#     def fset(self,name):
#         print("我被写入了，但是还可以做好多事")
#         self.n  = "tulingxy:" +name
#     def fdel(self):
#         pass
#     name2 = property(fget,fset,fdel,"这是一个说明文档")
# a = A()
# print(a.name)
# print(a.name2   )
#
# class Animel():
#     def sayHello(self):
#         pass
# class Dog(Animel):
#     def sayHello(self):
#         print("wen yi xia dui fang")
# class Person(Animel):
#     def sayHello(self):
#         print("kiss me")
# d = Dog()
# d.sayHello()
#
# p =Person()
# p.sayHello()
#
# import abc
# class Human(metaclass = abc.ABCMeta):
#     @abc.abstractclassmethod
#     def smoking(self):
#         pass
#     #定义类的抽象方法
#     @abc.abstractclassmethod
#     def drink():
#         pass
#     @abc.abstractclassmethod
#     def play():
#         pass
#     def sleep(self):

#
# def say(self):
#     print("saying...")
# def talk(self):
#     print("talking...")
# A = type("AName",(object,),{"class_say":say,"class_talk":talk})
# a = A()
# dir(a)

