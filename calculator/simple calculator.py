from tkinter import *

def btn(number):
    global operator
    operator = operator + str(number)
    txt_input.set(operator)

def Clear():
    global operator
    operator=''
    txt_input.set('')
    display.insert(0,'0.0')

def Equal():
    global operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator=''

root=Tk()
root.title("Calculator")

operator=""
txt_input=IntVar(value="0.0")

#===================Screen====================
display=Entry(root,font=('arial',20,'bold'),fg='white',bg='green',justify='right',bd=20,textvariable=txt_input)
display.grid(columnspan=4)

#===================Row1======================
btn7=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='7',command=lambda:btn(7))
btn7.grid(row=1,column=0)

btn8=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='8',command=lambda:btn(8))
btn8.grid(row=1,column=1)

btn9=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='9',command=lambda:btn(9))
btn9.grid(row=1,column=2)

btnC=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='C',bg='green',command=Clear)
btnC.grid(row=1,column=3)

#====================Row2=======================
btn4=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='4',command=lambda:btn(4))
btn4.grid(row=2,column=0)

btn5=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='5',command=lambda:btn(5))
btn5.grid(row=2,column=1)

btn6=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='6',command=lambda:btn(6))
btn6.grid(row=2,column=2)

btnplus=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='+',bg='orange',command=lambda:btn('+'))
btnplus.grid(row=2,column=3)

#=====================Row3========================
btn1=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='1',command=lambda:btn(1))
btn1.grid(row=3,column=0)

btn2=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='2',command=lambda:btn(2))
btn2.grid(row=3,column=1)

btn3=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='3',command=lambda:btn(3))
btn3.grid(row=3,column=2)

btnminus=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='-',bg='orange',command=lambda:btn('-'))
btnminus.grid(row=3,column=3)

#=====================Row4=======================
btn0=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='0',command=lambda:btn(0))
btn0.grid(row=4,column=0)

btndot=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='.',bg='orange',command=lambda:btn('.'))
btndot.grid(row=4,column=1)

btndivision=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='/',bg='orange',command=lambda:btn('/'))
btndivision.grid(row=4,column=2)

btnmultiply=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='x',bg="orange",command=lambda:btn('*'))
btnmultiply.grid(row=4,column=3)

#======================Row5======================
btnequals=Button(root,height=1,width=9,bd=6,fg="black",font=('arial',20,'bold'),text='=',bg='green',command=Equal)
btnequals.grid(row=5,column=0,columnspan=2)

btnopenbracket=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text='(',bg='orange',command=lambda:btn('('))
btnopenbracket.grid(row=5,column=2)

btnclosebracket=Button(root,height=1,width=4,bd=6,fg="black",font=('arial',20,'bold'),text=')',bg='orange',command=lambda:btn(')'))
btnclosebracket.grid(row=5,column=3)

root.mainloop()
