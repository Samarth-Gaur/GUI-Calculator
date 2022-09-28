from tkinter import *
from math import *

m=Tk()
m.configure(bg="Turquoise")
m.geometry("280x280")
m.title("CALCULATOR")
a=StringVar()
expression=""
#creating all usable fuctions
def press(n):
    global expression
    expression+=str(n)
    a.set(expression)
def sq():
    try:    
        global expression
        expression=str(sqrt(eval(expression)))
        a.set(expression)
    except:
        a.set("Not a valid expression")
        expression=""
def bspace():
    global expression
    x=""
    for i in range(0,len(str(expression))-1):
        x+=expression[i]
    expression=x    
    a.set(expression)
    
def eq():
    try:
        global expression
        t=str(eval(expression))
        a.set(t)
        expression=""
    except:
        a.set("Not A Valid Expression")
        expression=""
# creating buttons as well as text box
        
multi=Button(m,text="*",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("*"),bd=3)
div=Button(m,text="/",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("/"),bd=3)
add=Button(m,text="+",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("+"),bd=3)
sub=Button(m,text="-",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("-"),bd=3)
one=Button(m,text="1",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("1"),bd=3)
two=Button(m,text="2",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("2"),bd=3)
three=Button(m,text="3",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("3"),bd=3)
four=Button(m,text="4",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("4"),bd=3)
five=Button(m,text="5",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("5"),bd=3)
six=Button(m,text="6",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("6"),bd=3)
seven=Button(m,text="7",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("7"),bd=3)
eight=Button(m,text="8",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("8"),bd=3)
nine=Button(m,text="9",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("9"),bd=3)
zero=Button(m,text="0",bg="black",fg="white",activebackground="grey",width=12,height=2,command=lambda:press("0"),bd=3)
dot=Button(m,text=".",bg="black",fg="white",activebackground="grey",width=5,height=2,command=lambda:press("."),bd=3)
equ=Button(m,text="=",bg="black",fg="white",activebackground="grey",width=5,height=5,command=eq,bd=3)
rec=Button(m,text="√",bg="black",fg="white",activebackground="grey",width=5,height=2,command=sq,bd=3)
show=Entry(m,text="Enter the Expression",textvariable=a,width=18,font=("Times New Roman",20))
back=Button(m,text="<-",bg="black",fg="white",activebackground="grey",width=5,height=2,command=bspace,bd=3)
sq=Button(m,text="",bg="black",fg="white",activebackground="grey",width=5,height=2,command=bspace,bd=3)

#Placing all the variables on tkinter
back.place(x=215,y=95)
show.place(x=10,y=20,height=60)    
multi.place(x=165,y=140)
div.place(x=165,y=95)
rec.place(x=215,y=140)
equ.place(x=215,y=185)
add.place(x=165,y=230)
sub.place(x=165,y=185)
zero.place(x=15,y=230)
two.place(x=65,y=185)
one.place(x=15,y=185)
dot.place(x=115,y=230)
three.place(x=115,y=185)
four.place(x=15,y=140)
five.place(x=65,y=140)
six.place(x=115,y=140)
seven.place(x=15,y=95)
eight.place(x=65,y=95)
nine.place(x=115,y=95)

m.mainloop()
