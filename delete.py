from tkinter import *
from tkinter import messagebox
import subprocess
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="sk270405",database='PyBank')
mycur=mydb.cursor()
from PIL import Image, ImageTk
root=Tk()
root.geometry("900x550")
# root.configure(bg="#fff")
root.resizable(False,False)


def delete1():
    try:
        mycur.execute("SELECT * FROM login")
        a = mycur.fetchone()
        if a is None:
            messagebox.showinfo("Info", "No login information found.")
            return
        account_no = a[0]
        ac = user.get()
        p = password.get()
        s = sure.get()

        if ac == "Account no" and p == "Password" and s == "Are you sure (y/n)":
            messagebox.showerror("Error", "Field Missing:")
        else:
            if ac != account_no:
                messagebox.showerror("Error", "Your Account number is Invalid.")
            else:
                if s.lower() == "y":
                    mycur.execute("DELETE FROM Accounts WHERE account_no=%s", (account_no,))
                    mydb.commit()  # Commit the delete operation
                    messagebox.showinfo("Done", "Account deleted successfully")
                    subprocess.Popen(["Python", "login.py"])
                    root.quit()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))
def delete1():
    subprocess.Popen(["Python", "delete.py"])
    root.quit()

def profile_view():
    subprocess.Popen(["Python", "view_profile.py"])
    root.quit()
def update1():
    subprocess.Popen(["Python", "update.py"])
    root.quit()
def dash():
    subprocess.Popen(["Python","dashboard.py"])
    root.quit()
def logout():
    subprocess.Popen(["Python","login.py"])
    root.quit()
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()

    if name=='':
        user.insert(0,'Account no.')


def on_enter1(e):
    password.delete(0, 'end')


def on_leave1(e):
    code = password.get()

    if code=='':
       password.insert(0, 'Password')

def on_enter2(e):
    sure.delete(0, 'end')


def on_leave2(e):
    code = sure.get()

    if code=='':
       sure.insert(0, 'Are you Sure (y/n)')


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

Frame(root,width=400,height=380,bg="white").place(x=380,y=80)
Label(root,text="Delete Account",font=('Calibri',15,'bold'),fg="orange",bg="white").place(x=520,y=100)
Label(root,text="Verify your Account Deatils ",font=('Calibri',12,'bold'),fg="dark blue",bg="white").place(x=440,y=150)
user = Entry(root, width=35, fg="black", border=0, bg="white", font=("Calibri", 13))
user.place(x=440, y=200)
user.insert(0, 'Account no')  # Now this works
Frame(root,width=290,height=2,bg="black").place(x=440,y=220)
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
########Entry for passcode
password = Entry(root, width=35, show='*',fg="black", border=0, bg="white", font=("Calibri", 13))
password.place(x=440, y=250)
password.insert(0, 'Password')
Frame(root,width=290,height=2,bg="black").place(x=440,y=270)# Now this works
password.bind('<FocusIn>',on_enter1)
password.bind('<FocusOut>',on_leave1)


sure= Entry(root, width=35, fg="black", border=0, bg="white", font=("Calibri", 13))
sure.place(x=440, y=290)
sure.insert(0, 'Are you Sure (y/n)')
Frame(root,width=290,height=2,bg="black").place(x=440,y=315)
sure.bind('<FocusIn>',on_enter2)
sure.bind('<FocusOut>',on_leave2)
Button(root,width=32,pady=7,text="Delete Account",bg="orange",fg="white",border=0,font=("Calibri",13,'bold')).place(x=440,y=350)
root.mainloop()