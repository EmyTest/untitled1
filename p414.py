# ##exercise 1
# print("hello world")
# print("hello again")
# print("i like typing this.")
# print(" this is fun")
# print("yay! printing.")
# print("i`d much rather you 'not'.")
# print('i "said" do not touch this.')
#
# ##exercise 2
#
# print("i could have code like this")
# print("this will run")
# #
# #
# # # ##exercise 3
# print("i will now count my chickens")
# print("hens",25+30/6)
# print("roosters",100-25*3%4)
# print("now i will count the eggs:")
# print(3+2+1-5+4%2-1/4+6)
# print("is it true that 3+2 <5-7 ?")
# print("oh ,thats why its false")
# print("how about some more")
# print("it is greater?",5>-2)
# print("it is less or equal?",5<=-2)
# print("it is less or equal?",5>=-2)
#
# ##exercise 4
# cars =100
# space_in_a_car = 4.0
# drivers =30
# passengers =90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven
#
# #加号只能同类型相加
# print("there are",cars,"cars available")
# print("there are only ",drivers,"drivers available.")
# print("there will be",cars_not_driven,"empty cars today")
# print("we can transport",carpool_capacity,"people today")
# print("we have ",passengers,"to carpool today.")
# print("we need to put about",average_passengers_per_car,"in each car.")
#
#
# ##exercise 5
#
# my_name = 'zed a .shaw'
# my_age = 17
# my_height = 74
# my_weight = 100
# my_eyes = 'blue'
# my_teeth = 'white'
# my_hair = 'brown'
#
#
# # f'Task {name} nothing to do' 等价于 'Task {name} nothing to do'.format(name=name)
# print(f"1、lets talk about {my_name}.")
# print("2、lets talk about {my_name}".format(my_name=my_name))
# print(f"he is {my_height} inches tall.")
# print(f"he is {my_weight} pounds heavy.")
# print("actually that is not too heavy.")
# print(f"he is got {my_eyes} eyes and {my_hair} hair.")
# print(f"his teeth are usually {my_teeth} depending on the co")
# #this line is tricky,try to get it exactly right
# total = my_age +my_height +my_weight
# print("total :",total)

#
# ##exercise 6
# types_of_people = 10
# x = f"there are {types_of_people} types of people"
#
# binary = "binary"
# do_not = "don`t"
# y = f"thosde who know {binary} add those who {do_not}."
# print(x)
# print(y)
#
# print(f"i said :{x}")
# print(f"i also said: '{y}' ")
#
# #***************************************************
# hilarious = True
# joke_evaluation = "isn`t that joke so funny?! {}"
#
# print(joke_evaluation.format(hilarious))
# #****************************************************
# w = "this is the left side of..."
# e = "a string with a right side."
#
# print(w+e)

# ##exercise 7
# print("mary had a little lamb.")
# print("its fleece was white as {}.".format('snow'))
# print("and everywhere that mary went.")
# print("."*10) #what`d that do?
# end1 = "c"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "b"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"
# print(end1+end2+end3+end4+end5+end6,end=' ')
# print(end7+end8+end9+end10+end11+end12)
#
# ##exercise 8
#
# formatter = "{}{}{}{}"
# print(formatter.format(1,2,3,4))
# print(formatter.format("one", "two", "three", "four"))
# print(formatter.format(True ,False ,False ,True))
# print(formatter.format(formatter,formatter,formatter,formatter))
# print(formatter.format(
#     "try your",
#     "own text here ",
#     "maybe a poem ",
#     "or a song about fear"
# ))
# #
#
#
# ##exercise 9
#
# days = "mon tue wed thu fri sat sun"
# months = "jan\nfeb\nmar\napr\nmay\njun\njul\naug"
#
# print("here are the days: ",days)
# print("here are the months: ",months)
#
# print("""
# there is something going on here.
# with the three double-guotes.
# we will be able to type as much as we like.
# even 4 lines if we want ,or 5,or 6.
# """)
# #
# ##exercise 10
# tabby_cat = "\t i am tabbed in."
# persian_cat = "i am split \n on a line."
# backslash_cat = "i am \\ a \\ cat."
# fat_cat = """
# i will do a list:
# \t* cat food
# \t* fishies
# \t* catnip\n\t*grass
# """
# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat)

## 11-20****************************************************************

# ##ex11.py
# print("how old are you?",end=' ')
# age = input()
# print("how tall are you? ",end = ' ')
# height = input()
# print("how uch do you weight?",end =' ')
# weight = input()
#
# print(f"so,you are {age} old ,{height} tall and {weight} ")
# #
# ##ex12.py
# age = input("how old are you?")
# height = input("how tall are you?")
# weight = input("how much do you weigh?")
#
# print(f"so ,you are {age} old ,{height} tall and {weight} hevy")
# #
# # ##ex13.py
# from sys import argv
# #read the WYSS section for how to run this
# script = argv
# first = argv
# second = argv
# third = argv
#
# print("the script is called: ",script)
# print("your first variable is:",first)
# print("your second variable is :",second)
# print("your third variable is: ",third)
# #
# #
# # ##ex14.py
# from sys import argv
#
# script = argv
# user_name = argv
# prompt = '> '
#
# print(f"Hi {user_name}, I'm the {script} script.")
# print("I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}?")
# likes = input(prompt)
#
# print(f"Where do you live {user_name}?")
# lives = input(prompt)
#
# print("What kind of computer do you have?")
# computer = input(prompt)
#
# print(f"""
#  Alright, so you said {likes} about liking me.
#  You live in {lives}. Not sure where that is.
#  And you have a {computer} computer. Nice.
#  """)
# #
# # #
# #
# # ##ex15.py
# from sys import argv
# script = argv
# filename = argv
# txt = open('/aaa.txt','r')
# print(f"Here's your file {'/aaa.txt'}:")
# print(txt.read())
# print("Type the filename again:")
# file_again = input("> ")
# #
# # # ##ex16.py
# from sys import argv
# script = argv
# filename =argv
# print(f"we are going to erase{'/aaa.txt'}")
# print("if you do not want that,hit ctrl-c(^c).")
# print("if you do want that,hit return")
# input("?")
# print("opening the file...")
# ####**********************************
# target = open('/aaa.txt','w')
#
# print("truncating the file.goodbye!")
# ###**************************
# target.truncate()
# ###**************************
# line1 = input("line 1: ")
# line2 = input("line 2: ")
# line3 = input("line 3 :")
#
# print(" i an going to write these to the file.")
#
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
#
# print("and finally , we close it.")
# target.close()
# # #
# # ###ex17.py
# # #
# from sys import argv
# from os.path import exists
# script = argv
# from_file = argv
# to_file = argv
#
# print(f"copying from {'/aaa.txt'} to {'/bbb.txt'}")
# in_file = open('/aaa.txt')
# indata = in_file.read()
#
# print(f"the input file is {len(indata)} bytes long")
# print(f"does the output file exist? {exists('/bbb.txt')}")
# print("ready,hit return to continue ,ctrl-c to abrot.")
#
# input()
# out_file = open('/bbb.txt','w')
# out_file.write(indata)
#
# print("alright,all done.")
#
# out_file.close()
# in_file.close()

#
#
# #
# #
# # # ##ex18.py
# def print_two(*args):
#     arg1,arg2 = args
#     print(f"arg1:{arg1},arg2:{arg2}")
# def print_two_again(arg1,arg2):
#     print(f"arg1:{arg1},arg2:{arg2}")
# def print_one(arg1):
#     print(f"arg1:{arg1}")
# def print_note():
#     print("i got nothin.")
# print_two("zed","shaw")
# print_two_again("zed","shaw")
# print_one("first!!!")
# print_note()

# #
# #
# # ##ex19.py
# def cheese_and_crackers(cheese_count,boxes_of_crackers):
#     print(f"you have {cheese_count} cheese!")
#     print(f"you have {boxes_of_crackers}boxes of crackers!")
#     print("man that is enough for a party!!")
# print("we can just give the function numbers directly:")
# cheese_and_crackers(20,30)
#
# print("or,we can use variables from our script: ")
# amount_of_cheese = 10
# amount_of_crackers =50
#
# cheese_and_crackers(amount_of_cheese,amount_of_crackers)
#
# print("we can eben do math inside too:")
# cheese_and_crackers(10+20,5+6)
#
# print("and we can combine the two,variables and math:")
# cheese_and_crackers(amount_of_cheese +100,amount_of_crackers)
# #
#
# ##ex20.py
#
from sys import argv
script = argv
input_file = argv

def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0)
def print_a_line(line_count,f):
    print(line_count,f.readline())
current_file = open('/bbb.txt')

print("first let us print the whole file:\n")
print_all(current_file)
print("now let us rewind,kind of like a tape.")
rewind(current_file)

print("let us print three lines: ")
current_line = 1
print_a_line(current_line,current_file)
current_line=current_line+1
print_a_line(current_line,current_file)

current_line = current_line+1
print_a_line(current_line,current_file)
