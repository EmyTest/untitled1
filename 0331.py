class A():
    name = "dana"
    age = 18

# print(A.__dict__)
# yueyue = A()
# yueyue.__dict__
# print(yueyue.name)
def say(self):
    self.name = "aaa"
    self.age = 200

print(A.name)
print(A.age)

print("*"*20)
print(id(A.name))
print(id(A.age))

print("*"*20)
a = A()

print(a.age)
print(a.name)
print(id(a.name))
print(id(a.age))
