class Student():
    def __init__(self,name="noname",age =18):
        self.name = name
        self.age = age
    def say(self):
        print("My name is {0}".format(self.name))
def sayHello():
        print("hi nice to meet")
print("我是模块")