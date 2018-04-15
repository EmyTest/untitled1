import random

while 1:
    num = input('输入1，2，3三个数字')
    if num == '-1':
        break

    rand_num = random.randrange(1,4)
    num = int(num)
    rand_num = int(rand_num)
    #定义一个变量用于存储初始变量
    source = 0
    if num>rand_num:
        print("输入的数比随机数大")
    elif num == rand_num:
        source += 100
        print('太棒了，分数为',source)
    elif num<rand_num:
        print("输入的数比随机数小")


