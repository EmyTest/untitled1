class Animel():
    def __init__(self):
        print("anime")
class PaxingAni():
    def __init__(self,name):
        print("paxing dongwu","geluomi")
class Dog(PaxingAni):

    #每次实例化时第一个被调用 主要工作是进行初始化
    def __init__(self):
        print("i am a dog")

kaka = Dog()

class Cat(PaxingAni):
    pass
c = Cat()
