from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="sk270405",database='PyBank')
mycur=mydb.cursor()
mycur.execute("CREATE DATABASE IF NOT EXISTS PyBank")
mycur.execute(""" 
            CREATE TABLE IF NOT EXISTS Accounts(
                name VARCHAR(255),
                fname VARCHAR(225),
                birth DATE,
                phone VARCHAR(15),
                account_no VARCHAR(15),
                password VARCHAR(225),
                email VARCHAR(225),
                city VARCHAR(225),
                UNIQUE (name, fname, birth)  -- Ensure this combination is unique
            )
        """)
def forget():
    subprocess.Popen(["python", "forget.py"])
    root.destroy()
def open_create_account():
    subprocess.Popen(["python", "newaccount.py"])
    root.destroy()

def signin():
    name=user.get()
    code=password.get()

    if name=='Account no.' or code=='Password':
        messagebox.showerror("Error","Invalid Account no and Password!")
    elif  len(name)<8:
        messagebox.showerror("Error","Invalid Account no")
    else:
        mycur.execute("select * from Accounts")
        myresult=mycur.fetchall()
        for c in myresult:
            if c[4]==name and c[5]==code:
                mycur.execute("SET SQL_SAFE_UPDATES = 0")
                mycur.execute("delete from login")
                mycur.execute("Insert into login(account_no) values(%s)",(name,))
                mydb.commit()
                subprocess.Popen(['Python','dashboard.py'])
                root.quit()
                return True
        messagebox.showerror("Error","Username and Password does not exit!")

root=Tk()
root.title("Login")
root.geometry("900x500")
root.configure(bg="#fff")
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()

    if name=='':
        user.insert(0,'Username')


def on_enter1(e):
    password.delete(0, 'end')


def on_leave1(e):
    code = password.get()

    if code=='':
       password.insert(0, 'Password')


root.resizable(False,False)
img = Image.open("login.png")
img = img.resize((420, 450), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
Label(root,image=img,bg="white").place(x=50,y=50)
Label(root,text="PyBank",font=('Calibri',26,'bold'),fg="Orange",bg="white").place(x=620,y=10)
frame=Frame(root,width=380,height=350,bg="white")
frame.place(x=480,y=75)
Label(frame,text="Sign in",fg="dark blue",bg="white",font=("Calibri",23,'bold')).place(x=150,y=10)
###############Entry for USername
user = Entry(frame, width=35, fg="black", border=0, bg="white", font=("Calibri", 13))
user.place(x=65, y=85)
user.insert(0, 'Account no')  # Now this works
Frame(frame,width=295,height=2,bg="black").place(x=65,y=105)
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
########Entry for passcode
password = Entry(frame, width=35, show='*',fg="black", border=0, bg="white", font=("Calibri", 13))
password.place(x=65, y=155)
password.insert(0, 'Password')  # Now this works
password.bind('<FocusIn>',on_enter1)
password.bind('<FocusOut>',on_leave1)
##########
Frame(frame,width=295,height=2,bg="black").place(x=65,y=175)
Button(frame,width=33,pady=7,text="Sign in",bg="orange",fg="white",border=0,font=("Calibri",13,'bold'),command=signin).place(x=60,y=213)
Label(frame,text= "Don't have an account?",fg="black",bg="white",font=("Calibri",11)).place(x=65,y=270)
signup=Button(frame,width=6,text="Sign up",border=0,bg="white",cursor='hand2',fg="#57a1f8",font=("Calibri",11,'bold'),command=open_create_account).place(x=215,y=267)
forget=Button(frame,command=forget,width=15,text="Forget Passcode",border=0,bg="white",cursor='hand2',fg="#57a1f8",font=("Calibri",11,'bold')).place(x=55,y=290)

root.mainloop()