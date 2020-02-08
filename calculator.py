from tkinter import *
calc=Tk()
calc.geometry("354x460")
calc.title("Calculator")
calclabel=Label(calc,text="CALCULATOR",font=("Courier New",30,'bold'))
calclabel.pack(side=TOP)
textin=StringVar()
operator=""
def clickbut(numbers):
    global operator
    operator=operator+str(numbers)
    textin.set(operator)

def eqbut():
     global operator
     result=str(eval(operator))
     textin.set(result)
     operator=""
def clrbut():
    global operator
    text1.delete(0, END)
    operator=""

text1=Entry(calc,font=("Courier New",20,'bold'),textvar=textin,width=20,bd=5)
text1.pack()
one=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut(1),text="1",font=("Courier New",12,'bold'))
one.place(x=10,y=100)
two=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut(2),text="2",font=("Courier New",12,'bold'))
two.place(x=10,y=170)
three=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut(3),text="3",font=("Courier New",12,'bold'))
three.place(x=10,y=240)
four=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut(4),text="4",font=("Courier New",12,'bold'))
four.place(x=70,y=100)
five=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut(5),text="5",font=("Courier New",12,'bold'))
five.place(x=70,y=170)
six=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut(6),text="6",font=("Courier New",12,'bold'))
six.place(x=70,y=240)
seven=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut(7),text="7",font=("Courier New",12,'bold'))
seven.place(x=130,y=100)
eight=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut(8),text="8",font=("Courier New",12,'bold'))
eight.place(x=130,y=170)
nine=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut(9),text="9",font=("Courier New",12,'bold'))
nine.place(x=130,y=240)
sub=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut("-"),text="-",font=("Courier New",12,'bold'))
sub.place(x=190,y=170)
mul=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut("*"),text="X",font=("Courier New",12,'bold'))
mul.place(x=190,y=240)
zero=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut(0),text="0",font=("Courier New",12,'bold'))
zero.place(x=10,y=310)
dot=Button(calc,padx=44,pady=14,bd=4,command=lambda:clickbut("."),text=".",font=("Courier New",12,'bold'))
dot.place(x=70,y=310)
eq=Button(calc,padx=95,pady=0,bd=4,command=eqbut,text="=",font=("Courier New",22,'bold'))
eq.place(x=10,y=380)
add=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut("+"),text="+",font=("Courier New",12,'bold'))
add.place(x=190,y=100)
div=Button(calc,padx=14,pady=14,bd=4,command=lambda:clickbut("/"),text="/",font=("Courier New",12,'bold'))
div.place(x=190,y=310)
clr=Button(calc,padx=10,pady=140,bd=4,command=clrbut,text="CE",font=("Courier New",22,'bold'))
clr.place(x=260,y=100)
calc.mainloop()
