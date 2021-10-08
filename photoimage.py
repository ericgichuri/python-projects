from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import ImageDraw
from PIL import ImageTk,Image,ImageFont,ImageDraw
from tkinter import messagebox

root=Tk()
root.title("watermark photos")
root.minsize(700,600)
root.maxsize(700,600)
root.configure(bg="lightblue")
#root.iconbitmap('myiconapp.ico')

def openfile():
    global my_image
    global myimg
    root.filename = filedialog.askopenfilename(initialdir='"/Users/pc/Pictures/"', title='open files'
                    , filetypes=(('png file', '*.png'),('jpg file', '*.jpg'),('gif file', '*.gif'), ('all files', '*.*')))
    my_label = Label(root, text=root.filename,font=("arial",10,"bold"),width=30)
    my_label.grid(column=0,row=2,columnspan=1)

    my_image = ImageTk.PhotoImage(Image.open(root.filename))

    def convert():


        myimg = Image.open(root.filename)
        #myimg.save('C:\\Users\\pc\\Pictures\\images' + name.get() + '.ico', format='ICO', sizes=[(70, 70)])
        myimg.save('C:\\Users\\pc\\Pictures\\images\\'+savename.get()+'.'+type.get(), format=type.get(), sizes=[(60, 60)])
        messagebox.showinfo("message", "image converted"+type.get())
    def watermark():


        myimg=Image.open(root.filename)
        width,height=myimg.size

        draw=ImageDraw.Draw(myimg)
        text=watermarkname.get()
        fontsiz=int(fontsize.get())
        font = ImageFont.truetype('times.ttf', fontsiz)
        textwidth, textheight = draw.textsize(text, font)



        margin=10
        x=width-textwidth-margin
        y=height-textheight-margin
        draw.text((x,y),text,font=font)
        myimg.save('C:\\Users\\pc\\Pictures\\images/myimage'+savename.get()+'.png', format='PNG', sizes=[(70, 50)])
        messagebox.showinfo("message", "water mark added")


    labelsave=Label(root,text='Name',font=("times",13,"bold"),anchor=W)
    labelsave.grid(column=0, row=4,sticky=W+E)
    watertext = Label(root, text="Text for watermark", font=("times", 13, "bold"),anchor=W)
    watertext.grid(column=0, row=6,sticky=W+E)
    labelfont = Label(root,text='font size', font=("times", 13, "bold"),anchor=W)
    labelfont.grid(column=0,row=8,sticky=W+E)
    labelfiletype = Label(root, text="type", font=('times', 13, "bold"),anchor=W)
    labelfiletype.grid(column=0, row=10,sticky=W+E)
    savename = Entry(root, bg="lightpink", font=("times", 15, "bold"), borderwidth=4)
    savename.grid(column=0, row=5,sticky=W+E)
    watermarkname = Entry(root, bg="lightpink", font=("times", 15, "bold"),borderwidth=4)
    watermarkname.grid(column=0, row=7,sticky=W+E)
    fontsize = Entry(root, bg="lightpink", font=("times", 15, "bold"),borderwidth=4)
    fontsize.grid(column=0, row=9,sticky=W+E)
    type=ttk.Combobox(root,state="readonly",font=("times", 13, "bold"),width=20,height=25)
    type['value']=('PNG','GIF','ICO')
    type.current(0)
    type.grid(column=0,row=11,sticky=W+E)

    btnframe=Frame(root)
    btnframe.grid(column=0,row=13,pady="10")
    btnconvert=Button(btnframe,text="convert",bg="#1aff1a",fg="black",font=("times",15,"bold"),command=convert)
    btnconvert.grid(column=1,row=0)
    btnwatermark=Button(btnframe,text="watermark",bg="#8000ff",fg="black",font=("times",15,"bold"),command=watermark)
    btnwatermark.grid(column=2,row=0)

mainlabel=Label(root,text="Image watermark creater",height=2,fg="gold",bg="#555555"
                ,font=("Colonna MT",30,"bold"),width=35)
mainlabel.grid(column=0,row=0,columnspan=4)
btnbrowser=Button(root,text="open file",bg="blue",fg="cyan",font=("times",15,"bold"),command=openfile)
btnbrowser.grid(column=0,row=1)

canvas=Canvas(root,width=300,height=300)
canvas.grid(column=2,row=4,rowspan=15)
img=(Image.open("C:\\Users\\pc\\Pictures\\fr.png"))
resized_img=img.resize((300,300),Image.ANTIALIAS)
new_image=ImageTk.PhotoImage(resized_img)
canvas.create_image(20,20,anchor=NW,image=new_image)
root.mainloop()