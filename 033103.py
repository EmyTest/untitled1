#继承的语法
#在python中，任何类都有一个共同的父类叫object
class Person():
    name = "nono"
    age =0
    __score = 0
    _petmane = "sec"#小名 保护的 子类可以用，不能公用
    def sleep(self):
        print("sleeping....")
    def work(self):
        print("make money")
#父类写在括号里面
class Teacher(Person):
    teacher_id = "1234"
    name = "lalal"
    def make_test(self):
        print("attention")
    def work(self):
        #扩充父类，使用父类名.父类成员
        Person.work(self)
        #扩充父类的另一种方法，使用super（）.父类成员
        super().work()
        self.make_test()
t = Teacher()
t.work()
print(t.name)
# print(t._petmane)
# #print(t.__score)
# t.sleep()
# print(t.teacher_id)
# t.make_test()
