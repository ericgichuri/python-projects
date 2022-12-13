from tkinter import *
import math
import re

win=Tk()
scr_h=win.winfo_screenheight()
scr_w=win.winfo_screenwidth()
win_h=430
win_w=292
x_cord=(scr_w-win_w)/2
y_cord=(scr_h-win_h)/2
win.geometry("%dx%d+%d+%d"%(win_w,win_h,x_cord,y_cord))
win.title("Calculator")

#------------------functions------------
def enter_number(value):
    current_text=textbox.get()
    current_text=re.sub('^0','',current_text)
    insert_text=value
    textbox.delete(0,END)
    insert_text1=str(current_text)+str(insert_text)
    textbox.insert(END,insert_text1)   

def check_cleared(value,*args):
    if textbox.get()=="":
        textbox.delete(0,END)
        textbox.insert(END,0)
    else:
        current_text=textbox.get()
        current_text1=re.sub('[^0123456789.]',"",current_text)
        textbox.delete(0,END)
        enter_number(current_text1)
        #textbox.insert(END,current_text)

def clear_textbox():
    textbox.delete(0,END)
def insert_operator(value):
    current_text=textbox.get()
    textbox.insert(END,value)
def calculate_answer():
    current_text=textbox.get()
    current_text=re.sub('^0','',current_text)
    try:
        answer=eval(current_text)
        if str(answer).isdigit()==True:
            pass
        else:
            answer=round(answer,4)
    except:
        answer="Error"
    
    ans_textbox.delete(0,END)
    ans_textbox.insert(END,answer)

def calculate_percentage():
    
    try:
        value=float(textbox.get())
        answer=value/100
        answer=round(answer,6)
        ans_textbox.delete(0,END)
        ans_textbox.insert(END,answer)
    except:
        ans_textbox.delete(0,END)
        ans_textbox.insert(END,"Error")
def calculate_square():
    num=textbox.get()
    try:
        answer=pow(float(num),2)
        ans_textbox.delete(0,END)
        ans_textbox.insert(END,answer)
    except:
        ans_textbox.delete(0,END)
        ans_textbox.insert(END,"Error")
def enter_answer(value):
    if value=="Error":
        value=0
    textbox.delete(0,END)
    textbox.insert(END,value)

frame1=LabelFrame(win,relief=RIDGE,border=1,borderwidth=2,text=" ")
frame1.pack(fill=X,side=TOP)
textbox=Entry(frame1,font=("times",25,"bold"),bd=2,borderwidth=5)
textbox.pack(fill=BOTH,expand=1,side=TOP)
textbox.insert(END,0)
textbox.bind("<KeyRelease>",check_cleared)
ans_textbox=Entry(frame1,font=("times",16,"bold"),bg="lightblue",bd=1,borderwidth=3,width=13)
ans_textbox.pack(side=RIGHT)
ans_textbox.insert(END,0)
frame2=LabelFrame(win,relief=SUNKEN,border=1,borderwidth=3)
frame2.pack(fill=BOTH,side=TOP,expand=1)
fontbtn=("times",15,"bold")
btn_w=5
btn_h=2
btn=Button(frame2,text="C",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=clear_textbox)
btn.grid(column=0,row=0)
btn=Button(frame2,text="%",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=calculate_percentage)
btn.grid(column=1,row=0)
btn=Button(frame2,text="^2",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=calculate_square)
btn.grid(column=2,row=0)
btn=Button(frame2,text="÷",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:insert_operator("/"))
btn.grid(column=3,row=0)
btn=Button(frame2,text="7",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:enter_number(7))
btn.grid(column=0,row=1)
btn=Button(frame2,text="8",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:enter_number(8))
btn.grid(column=1,row=1)
btn=Button(frame2,text="9",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:enter_number(9))
btn.grid(column=2,row=1)
btn=Button(frame2,text="×",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:insert_operator("*"))
btn.grid(column=3,row=1)
btn=Button(frame2,text="4",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:enter_number(4))
btn.grid(column=0,row=2)
btn=Button(frame2,text="5",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:enter_number(5))
btn.grid(column=1,row=2)
btn=Button(frame2,text="6",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:enter_number(6))
btn.grid(column=2,row=2)
btn=Button(frame2,text="-",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:insert_operator("-"))
btn.grid(column=3,row=2)
btn=Button(frame2,text="1",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:enter_number(1))
btn.grid(column=0,row=3)
btn=Button(frame2,text="2",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:enter_number(2))
btn.grid(column=1,row=3)
btn=Button(frame2,text="3",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:enter_number(3))
btn.grid(column=2,row=3)
btn=Button(frame2,text="+",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:insert_operator("+"))
btn.grid(column=3,row=3)
btn=Button(frame2,text="0",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:enter_number(0))
btn.grid(column=0,row=4)
btn=Button(frame2,text=".",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:enter_number("."))
btn.grid(column=1,row=4)
btn=Button(frame2,text="ans",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=lambda:enter_answer(ans_textbox.get()))
btn.grid(column=2,row=4)
btn=Button(frame2,text="=",font=fontbtn,width=btn_w,height=btn_h,relief=RAISED,bd=2,borderwidth=3,command=calculate_answer)
btn.grid(column=3,row=4)
win.mainloop()