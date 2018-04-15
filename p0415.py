import  random
import math


def line():
     # 定义一个空字符串拼接字符
    str_num = ''
    #循环前四个随机字母 用ascii码对应值 随即转化为字母
    for i in range(4):
        #随机小写字母的ascii值
         num = random.randrange(97,123)
        #将ascii值转换成对应的字母
         str_s = chr(num)
        #依次拼接得到随即字母
         str_num = str_num + str_s
    #循环后8个随机数字
    for i in range (8):
        num = random.randrange(0,10)
        str_num=str_num+str(num)
    return str_num

num = input("请输入一个三位数")
random_num = random.randrange(100,1000)
if num.isdigit() and 100<=int(num) <=999:
    num = int(num)
    random_num = int(random_num)
    if num>random_num:
        #求百位数，地板除 或者floor()
        bai = num//100
        #求十位数字的方法：先把三位数字取100的余数，再地板除10
        shi =num%100//10
        #求个位数：直接取10的余
        ge = num%10
        print("这个三位数的个位数是{}十位数是{}百位是{}".format(ge,shi,bai))


    if num == random_num:
        print("你中奖了",random_num)
    if num <random_num:
        #由于120个字符每行12个，只需传入10行就可以
         for i in range(10):

            str_line = line()
           ## print(str_line)
        #执行文件存入操作
            with open('str_num.txt','a') as f:
                f.write(str_line+'\n')
            #自动关闭 不需要写close（）
        #print(random_num)
    pass
else:
    print("请按规定输入")





##print(ord('A'))  ascii码
# print(chr(97))      ##数字转ascii