import requests
from tkinter import *
from tkinter import ttk
import time
import datetime
dte=datetime.date.today()

#Key
key="f2b7a577139f4631b5add4f6d7026a79"
#
w=Tk()
scr_width=str((w.winfo_screenwidth()-800)//2)
scr_height=str((w.winfo_screenheight()-700)//2)

w.geometry("800x650"+"+"+scr_width+"+"+scr_height)
w.maxsize(800,650)
w.config(bg="#D3D3D3")
w.title("News-XTREME")

heading=Label(w,text="News-XTREME",font="comicsans 30 bold")
heading.pack(fill=X,padx=4,pady=4)
#Dictionries and list for dropdowns
c_dic={'Australia':'au','Canada':'ca','China':'cn','France':'fr','Germany':'de','India':'in','Japan':'jp','Russia':'ru','USA':'us'}
cnty=list(c_dic.keys())
cnty.insert(0,"--Select--")
catgory=["--Select--",'Business', 'Entertainment', 'Health', 'Science', 'Sports', 'Technology']
#Frame
f=Frame(w,bg="#fff")
#

#Variables
cnt=StringVar()
cgy=StringVar()
#
def show_news():
    global f1
    try:
        if cnt.get()=="--Select--":
            nfic1=Label(w,fg="red",bg="#D3D3D3",font="arial 16")
            nfic1.place(x=285,y=190)
            nfic1.config(fg="red",text="*Please select country *")
            nfic1.update()
            time.sleep(1)
            nfic1.config(text="")
        elif cgy.get()=="--Select--":
            nfic2=Label(w,fg="red",bg="#D3D3D3",font="arial 16")
            nfic2.place(x=260,y=190)
            nfic2.config(fg="red",text="*Please select news category*")
            nfic2.update()
            time.sleep(1)
            nfic2.config(text="")
        else:
            f1.destroy()
            f.place(y=250,width=800,height=400)
            top.place(x=295,y=220)
            f1=Frame(w,bg="#fff")
            f1.place(y=250,width=800,height=400)

            code=c_dic[cnt.get()]
            url= f"https://newsapi.org/v2/top-headlines?country={code}&category={cgy.get()}&apiKey={key}"            
            response = requests.get(url).json()
            c=1
            for i in response['articles']:
                if len(i['title'])<118:
                    Label(f1,text=str(c)+".  "+i['title'],justify="left",font="arial 10 bold",bg="#fff").pack(anchor='w',pady=2)
                    c+=1
                    if c==16:
                        break
    except:
        if cnt.get()=="--Select--":
            nfic1=Label(w,fg="red",bg="#D3D3D3",font="arial 16")
            nfic1.place(x=285,y=190)
            nfic1.config(fg="red",text="*Please select country *")
            nfic1.update()
            time.sleep(1)
            nfic1.config(text="")
        elif cgy.get()=="--Select--":
            nfic2=Label(w,fg="red",bg="#D3D3D3",font="arial 16")
            nfic2.place(x=260,y=190)
            nfic2.config(fg="red",text="*Please select news category*")
            nfic2.update()
            time.sleep(1)
            nfic2.config(text="")
        else:
            f.place(y=250,width=800,height=400)
            top.place(x=295,y=220)
            f1=Frame(w,bg="#fff",width=800,height=400)
            f1.place(y=250)

            if cnt.get()=="--Select--":
                Label(w,text="Please select country ")
            if cgy.get()=="--Select--":
                Label(w,text="Please select news categoty")
            code=c_dic[cnt.get()]
            url= f"https://newsapi.org/v2/top-headlines?country={code}&category={cgy.get()}&apiKey={key}"
            response = requests.get(url).json()
            c=1
            for i in response['articles']:
                if len(i['title'])<118:
                    Label(f1,text=str(c)+".  "+i['title'],justify="left",font="arial 10 bold",bg="#fff").pack(anchor='w',pady=2)
                    c+=1
                    if c==16:
                        break
    
#
Label(w,text="Date : ",font="arial 16 bold").place(x=10,y=60)
Label(w,text=dte,font="arial 16 bold").place(x=75,y=60)

Label(w,text="Country :",font=("arial",16,"bold")).place(x=10,y=100)

country=ttk.Combobox(w,textvariable=cnt,justify=CENTER,font=("Times New Roman",16),state="readonly")
country['values']=cnty
country.current(0)
country.place(x=120,y=100)

Label(w,text="Category :",font=("arial",16,"bold")).place(x=380,y=100)

cat=ttk.Combobox(w,textvariable=cgy,justify=CENTER,font=("Times New Roman",16),state="readonly")
cat['values']=catgory
cat.current(0)
cat.place(x=510,y=100)
w.option_add("*TCombobox*Listbox.font","arial 14")
Button(w,text="Get News",activebackground="#32CD32",activeforeground="#fff",font="arial 16",command=show_news).place(x=320,y=150)
top=Label(w,text="Top 15 Headlines",font="arial 16 bold",bg="#fff")

def ent(event):
    dev.config(font=("calibri", 10,"underline"))
def lea(event):
    dev.config(font=("calibri",10))
def close(event):
    f4.destroy()
    
def devcntc(event):
    global f4
    f4=Frame(w,bg="#000")
    Label(f4,text="Developed by :-",fg="#fff",bg="#000",font="Arial 16 underline").place(x=10,y=10)
    Label(f4,text="2021020_Arpan Kumar",fg="#fff",bg="#000",font="Arial 16").place(x=10,y=45)
    Label(f4,text="E-mail : arpan21020@iiitd.ac.in",fg="#fff",bg="#000",font="Arial 16").place(x=10,y=85)
    f4.place(x=200,y=120,width=400,height=120)
    
    cl=Label(f4,text=" X ",bg="red",fg="#fff")
    cl.place(x=380,y=0)
    cl.bind("<ButtonPress-1>",close)
dev=Label(w,text="Developer;s contact",bg="#D3D3D3",fg="#0000EE",font="calibri 10")
dev.place(x=680,y=60)
dev.bind("<Enter>",ent)
dev.bind("<Leave>",lea)
dev.bind("<ButtonPress-1>",devcntc)
