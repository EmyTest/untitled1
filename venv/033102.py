# class Student():
#     name = "dana"
#     age = 18
#     def say(self):
#         self.name = "aaaa"
#         self.age = 200
#         print("my name is {0}".format(self.name))
#         print("my age is {0}".format(self.age))
# yueyue = Student()
# yueyue.say()
#
# class Teacher():
#     name = "dana"
#     age = 19
#
#     def say(self):
#         self.name = "huihui"
#         self.age = 17
#         #调用类的成员变量需要用__class__
#         print("my name is {0}".format(__class__.name))
#         print("my age is {0}".format(self.age))
#     def sayAgain():
#         print(__class__.name)
#         print(__class__.age)
#         print("hello , nice to meet you !")
# t = Teacher()
# t.say()
# # #调用绑定函数使用类名
# # Teacher.sayAgain()
#
# #关于self的案例
# class A():
#     name = "liuying"
#     age = 18
#     def __init__(self):
#         self.name = "aaaa"
#         self.age = 200
#     def say(self):
#         print(self.name)
#         print(self.age)
# class B():
#     name = "bbbb"
#     age = 90
# a = A()
# a.say()
# #此时 系统会默认把a作为第一个参数传入函数
# A.say(A)
# #此时，传入的是实例类B，因为B具有name和age属性，所以不会报错
# A.say(B)

class Person():
    name = "liuying"
    __age =18
p = Person()
#print(p.name)
print(Person.__dict__)

p.Persion__age =19
print(p.Persion__age)