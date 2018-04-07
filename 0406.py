import tkinter


def reg():
    name = e1.get()
    pwd = e2.get()

    t1 = len(name)
    t2 = len(pwd)
    if name =="111" and pwd == "222":
        lb3["text"] = "登录成功"
    else:
        lb3['text'] = "用户名或密码错误"
        #输入框删除掉用户输入的内容
        e1.delete(0,t1)
        e2.delete(0,t2)
baseFrame = tkinter.Tk()

lb1 = tkinter.Label(baseFrame,text = "用户名")
lb1.grid(row =0,column=0,stick=tkinter.W)
#button参数command的意思是，当按钮被点击后启动相应的处理函数
btn = tkinter.Button(baseFrame,text ="登录",command=reg)
btn.grid(row=2,column=1,stick = tkinter.E)

lb3 = tkinter.Label(baseFrame,text=" ")
lb3.grid(row =3)
baseFrame.mainloop()

