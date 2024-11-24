from tkinter import *
from tkinter import messagebox
import subprocess
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="sk270405",database='PyBank')
mycur=mydb.cursor()
from PIL import Image, ImageTk
root=Tk()
def change():
    mycur.execute("SELECT * FROM login")
    a = mycur.fetchone()
    if a is None:
        messagebox.showinfo("Info", "No login information found.")
        return
    account_no = a[0]
    f=father.get()
    b=birth.get()
    p=phone.get()
    e=email.get()
    c=city.get()
    if(f=='Fathe Name' or b=='DOB(YYYY/MM/DD)' or p=='Phone no' or e=='Email' or c=='City'):
        messagebox.showerror("Error","Field Missing")
    else:
        mycur.execute(
            "UPDATE Accounts SET fname = %s, birth = %s, phone = %s, email = %s, city = %s WHERE account_no = %s",
            (f, b, p, e, c, account_no))
        mydb.commit()
        messagebox.showinfo("Done", "Data Updated Successfully!")
def update1():
    subprocess.Popen(["Python", "update.py"])
    root.quit()
def delete1():
    subprocess.Popen(["Python", "delete.py"])
    root.quit()
def profile1():
    mycur.execute("SELECT * FROM login")
    a = mycur.fetchone()
    account_no = a[0]
    mycur.execute("SELECT * FROM Accounts WHERE account_no=%s", (account_no,))
    data = mycur.fetchone()
    if data is not None:
        # Display the account and balance information
        account.config(text=data[0])  # Assuming the first column is account info
        fname.config(text=data[1])
        birth.config(text=data[2])
        phone.config(text=data[3])
        email.config(text=data[6])
        city.config(text=data[7])

def dash():
    subprocess.Popen(["Python","dashboard.py"])
    root.quit()
def profile_view():
    subprocess.Popen(["Python", "view_profile.py"])
    root.quit()
def logout():
    subprocess.Popen(["Python","login.py"])
    root.quit()
def on_enterf(e):
    father.delete(0,'end')
def on_leavef(e):
    name=father.get()

    if name=='':
        father.insert(0,'Father Name')
def on_enterb(e):
    birth.delete(0,'end')
def on_leaveb(e):
    name=birth.get()

    if name=='':
        birth.insert(0,'DOB(YYYY/MM/DD)')
def on_enterp(e):
    phone.delete(0,'end')
def on_leavep(e):
    name=phone.get()

    if name=='':
        phone.insert(0,'Phone no')
def on_entere(e):
    email.delete(0,'end')
def on_leavee(e):
    name=email.get()

    if name=='':
        email.insert(0,'Email')
def on_enterc(e):
    city.delete(0,'end')
def on_leavec(e):
    name=city.get()

    if name=='':
        city.insert(0,'City')
root.geometry("1190x550")
frame=Frame(root,width=260,height=650,bg="white")
frame.grid(row=0,column=1)
img = Image.open("card.jpg")
img = img.resize((80, 70), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
Label(frame,image=img,bg="white").place(x=10,y=10)
Label(frame,text="PyBank",font=("Calibri",26,'bold'),fg="Orange",bg="white").place(x=110,y=21)
img1 = Image.open("home.jpg")
img1 = img1.resize((30, 30), Image.Resampling.LANCZOS)
img1 = ImageTk.PhotoImage(img1)
Label(frame,image=img1,bg="white",cursor="hand2").place(x=30,y=130)
dashboard=Label(frame,text="Dashboard",cursor="hand2",font=("Calibri",14),fg="dark blue",bg="white")
dashboard.place(x=110,y=131)
dashboard.bind("<Button-1>", lambda e: dash())
##View Profile
img2 = Image.open("viewp.jpg")
img2 = img2.resize((30, 30), Image.Resampling.LANCZOS)
img2 = ImageTk.PhotoImage(img2)
Label(frame,image=img2,bg="white",cursor="hand2").place(x=30,y=180)
profile=Label(frame,text="View Profile",cursor="hand2",font=("Calibri",14),fg="dark blue",bg="white")
profile.place(x=110,y=181)
profile.bind("<Button-1>", lambda e: profile_view())
###Quick transfer
img3 = Image.open("transfer.jpg")
img3 = img3.resize((30, 30), Image.Resampling.LANCZOS)
img3 = ImageTk.PhotoImage(img3)
Label(frame,image=img3,bg="white",cursor="hand2").place(x=30,y=230)
transfer=Label(frame,text="Quick Transfer",cursor="hand2",font=("Calibri",14),fg="dark blue",bg="white")
transfer.place(x=110,y=230)
##DEposit
img4 = Image.open("deposit.jpg")
img4 = img4.resize((25, 25), Image.Resampling.LANCZOS)
img4 = ImageTk.PhotoImage(img4)
Label(frame,image=img4,bg="white",cursor="hand2").place(x=30,y=285)
deposit=Label(frame,text="Deposit",cursor="hand2",font=("Calibri",14),fg="dark blue",bg="white")
deposit.place(x=110,y=285)
#update
img6 = Image.open("update.jpg")
img6 = img6.resize((25, 25), Image.Resampling.LANCZOS)
img6 = ImageTk.PhotoImage(img6)
Label(frame,image=img6,bg="white",cursor="hand2").place(x=30,y=330)
update=Label(frame,text="Update Profile",cursor="hand2",font=("Calibri",14),fg="dark blue",bg="white")
update.place(x=110,y=330)
update.bind("<Button-1>", lambda e: update1())

##delete
img8 = Image.open("delete.jpg")
img8 = img8.resize((25, 25), Image.Resampling.LANCZOS)
img8 = ImageTk.PhotoImage(img8)
Label(frame,image=img8,bg="white",cursor="hand2").place(x=30,y=380)
delete=Label(frame,text="Delete Account",cursor="hand2",font=("Calibri",14),fg="dark blue",bg="white")
delete.place(x=110,y=380)
delete.bind("<Button-1>", lambda e: delete1())
##logout
img9 = Image.open("logout.jpg")
img9 = img9.resize((22, 22), Image.Resampling.LANCZOS)
img9 = ImageTk.PhotoImage(img9)
Label(frame,image=img9,bg="white",cursor="hand2").place(x=30,y=430)
delete=Label(frame,text="Logout",cursor="hand2",font=("Calibri",14),fg="dark blue",bg="white")
delete.place(x=110,y=430)
delete.bind("<Button-1>", lambda e: logout())

pic = Image.open("update1.jpg")
pic = pic.resize((410, 476), Image.Resampling.LANCZOS)
pic = ImageTk.PhotoImage(pic)
Label(root,image=pic,bg="white",cursor="hand2").place(x=730,y=30)
Frame(root,width=460,height=480,bg="white").place(x=320,y=30)
Label(root,text="Update Account Details",font=("Calibri",22,'bold'),fg="orange",bg="white").place(x=470,y=50)
Label(root,text="You can update only these fields",font=("Calibri",14,'bold'),fg="dark blue",bg="white").place(x=370,y=110)

###Fathernane
father = Entry(root, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
father.place(x=370,y=150)
father.insert(0, 'Father Name')  # Now this works
Frame(root,width=280,height=2,bg="black").place(x=370,y=170)
father.bind('<FocusIn>',on_enterf)
father.bind('<FocusOut>',on_leavef)
###DOB
birth = Entry(root, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
birth.place(x=370, y=200)
birth.insert(0, 'DOB(YYYY/MM/DD)')  # Now this works
Frame(root,width=280,height=2,bg="black").place(x=370,y=220)
birth.bind('<FocusIn>',on_enterb)
birth.bind('<FocusOut>',on_leaveb)
##Phone number
phone= Entry(root, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
phone.place(x=370, y=250)
phone.insert(0, 'Phone no')  # Now this works
Frame(root,width=280,height=2,bg="black").place(x=370,y=270)
phone.bind('<FocusIn>',on_enterp)
phone.bind('<FocusOut>',on_leavep)
###Email
email= Entry(root, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
email.place(x=370, y=300)
email.insert(0, 'Email')  # Now this works
Frame(root,width=280,height=2,bg="black").place(x=370,y=320)
email.bind('<FocusIn>',on_entere)
email.bind('<FocusOut>',on_leavee)
###City
city= Entry(root, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
city.place(x=370, y=350)
city.insert(0, 'City')  # Now this works
Frame(root,width=280,height=2,bg="black").place(x=370,y=370)
city.bind('<FocusIn>',on_enterc)
Button(root,width=30,pady=7,text="Update Account",command=change,bg="Orange",fg="white",border=0,font=("Calibri",13,'bold')).place(x=370,y=400)
city.bind('<FocusOut>',on_leavec)


root.mainloop()