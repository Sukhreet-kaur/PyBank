from tkinter import *
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import random
import mysql.connector


def set():
    mydb = mysql.connector.connect(host="localhost", user="root", password="sk270405", database='PyBank')
    mycur = mydb.cursor()

    ac = account.get()
    p = phone.get()
    b = birth.get()
    pa = pcode.get()
    cp = ccode.get()

    mycur.execute("Select * from Accounts where account_no=%s and phone=%s and birth=%s ", (ac, p, b))
    account_exists = mycur.fetchone()

    if account_exists is None:
        messagebox.showerror("Error", "Account details do not match")
        return

    if pa != cp:
        messagebox.showerror("Error", "New password and Confirm Password do not match")
    elif len(pa) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long")
    else:
        mycur.execute("update Accounts set password=%s where account_no=%s and phone=%s and birth=%s", (pa, ac, p, b))
        mydb.commit()
        result.config(text="Password has been successfully updated!!")

    mycur.close()
    mydb.close()
def on_entera(e):
    account.delete(0,'end')
def on_leavea(e):
    name=account.get()

    if name=='':
        account.insert(0,'Account no')
def on_enterp(e):
    phone.delete(0,'end')
def on_leavep(e):
    name=phone.get()

    if name=='':
        phone.insert(0,'Phone no')
def on_enterb(e):
    birth.delete(0,'end')
def on_leaveb(e):
    name=birth.get()

    if name=='':
        birth.insert(0,'DOB(YYYY/MM/DD)')
def on_enterc(e):
   pcode.delete(0,'end')
def on_leavec(e):
    name=pcode.get()

    if name=='':
        pcode.insert(0,'New Password')
def on_entercc(e):
    ccode.delete(0,'end')
def on_leavecc(e):
    name=ccode.get()

    if name=='':
        ccode.insert(0,'Confirm Password')
def signin():
    subprocess.Popen(["Python","login.py"])
    root.quit()
root=Tk()
root.geometry("820x550")
root.configure(bg="#fff")
img = Image.open("forgetpassword.jpg")
img = img.resize((450, 450), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
Label(root,image=img,bg="white").grid(row=0,column=1)
frame=Frame(root,width=380,height=600,bg="white")
frame.grid(row=0,column=2)
Label(frame,text="Forget Password",fg="#10375C",bg="white",font=("Calibri",23,'bold')).place(x=70,y=40)
#########Name
Label(frame,text="Enter your details for Confirmation",fg="#10375C",bg="white",font=("Calibri",13,'bold')).place(x=70,y=100)
account = Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))

account.place(x=50, y=165)
account.insert(0, 'Account no')  # Now this works
account.bind('<FocusIn>',on_entera)
account.bind('<FocusOut>',on_leavea)
Frame(frame,width=280,height=2,bg="black").place(x=52,y=185)

###Fathernane
phone= Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
phone.place(x=50, y=205)
phone.insert(0, 'Phone no')  # Now this works
Frame(frame,width=280,height=2,bg="black").place(x=52,y=225)
phone.bind('<FocusIn>',on_enterp)
phone.bind('<FocusOut>',on_leavep)
###DOB
birth = Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
birth.place(x=50, y=245)
birth.insert(0, 'DOB(YYYY/MM/DD)')  # Now this works
Frame(frame,width=280,height=2,bg="black").place(x=52,y=265)
birth.bind('<FocusIn>',on_enterb)
birth.bind('<FocusOut>',on_leaveb)
##Phone number
pcode= Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
pcode.place(x=50, y=285)
pcode.insert(0, 'New Password')  # Now this works
Frame(frame,width=280,height=2,bg="black").place(x=52,y=305)
pcode.bind('<FocusIn>',on_enterc)
pcode.bind('<FocusOut>',on_leavec)
###Email
ccode= Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
ccode.place(x=50, y=325)
ccode.insert(0, 'Confirm Password')  # Now this works
Frame(frame,width=280,height=2,bg="black").place(x=52,y=345)
ccode.bind('<FocusIn>',on_entercc)
ccode.bind('<FocusOut>',on_leavecc)
Button(frame,command=set,width=30,pady=7,text="Set Password",bg="#FFC300",fg="white",border=0,font=("Calibri",13,'bold')).place(x=52,y=390)
signin=Button(frame,width=6,text="Sign in",border=0,bg="white",cursor='hand2',fg="#57a1f8",font=("Calibri",11,'bold'),command=signin).place(x=52,y=450)
result=Label(frame,text="",font=("Calibri",13,'bold'),bg="white",fg="red")
result.place(x=52,y=480)
root.mainloop()