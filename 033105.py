# class Fish():
#     def __init__(self,name):
#         self.name = name
#     def swim(self):
#         print("i am swimming...")
# # class Bird():
# #     def __init__(self,name):
# #         self.name = name
# #     def fly(self):
# #         print("i am flying...")
# # class Person():
# #     def __init__(self,name):
# #         self.name = name
# #     def work(self):
# #         print("working...")
# # class SuperMan(Person,Bird,Fish):
# #     def __init__(self,name):
# #         self.name = name
# # s = SuperMan("yueyue")
# # s.fly()
# # s.swim()
#
# class A():
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
#
# class D(B,C):
#     pass


# class Person():
#     name = "liuying"
#     age = 18
#     def eat(self):
#         print("eat...")
#     def drink(self):
#         print("drink")
#     def sleep(self):
#         print("sleep...")
# class Teacher(Person):
#     def work(self):
#         print("work")
# class Student(Person):
#     def study(self):
#         print("Study")
# class Tutor(Teacher,Student):
#     pass
# t = Tutor()
#
# print(Tutor.__mro__)
# print(t.__dict__)
# print(Tutor.__dict__)
#
# print("*"*20)
# class TeacherMixin():
#     def work(self):
#         print("work")
# class StudentMinxin():
#     def study(self):
#         print("study")
# class TutorM(Person,TeacherMixin,StudentMinxin):
#     pass
# tt = TutorM()
# print(TutorM.__mro__)
# print(tt.__dict__)
# print(TutorM.__dict__)

#
# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.setName(name)
#     def intro(self):
#         print("hai , my name is {0}".format(self.name))
#     def setName(self,name):
#         self.name = name.upper()
# s1 = Student("liu ying",19)
# s2 = Student("michi stangle",24)
#
# s1.intro()
# s2.intro()

#property 案例
#定义一个person类，具有name，age属性
#对于任意输入的姓名，我们希望都用大写的方式保存
#年龄，我们希望内部统一用整数保存
# x = property(fget,fset,fdel,doc)
class Person():
    def fget(self):
        return self._name *2
    def fset(self,name):
        self._name = name.upper()
    def fdel(self):
        self._name = "noname"
    name = property(fget,fset,fdel,"对name进行下列操作")

p1 = Person()
p1.name = "tuling"
print(p1.name)