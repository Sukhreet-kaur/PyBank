from tkinter import *
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import random
import mysql.connector


import random
from tkinter import messagebox
import mysql.connector

def signin():
    name = user.get()
    fname = father.get()
    bdate = birth.get()
    pno = phone.get()
    eid = email.get()
    cityn = city.get()
    pcode = password.get()
    pccode = cpassword.get()

    # Check for missing fields
    if name == 'Username' or fname == "Father Name" or bdate == "DOB(DD/MM/YYYY)" or pno == "Phone no" or eid == "Email" or cityn == "City" or pcode == "Password" or pccode == "Confirm Password":
        messagebox.showerror("Error", "Field Missing")
        return  # Exit the function if there's an error

    n = random.randint(111111111111, 999999999999)  # Generate account number
    try:
        # Connect to MySQL and create database/table if necessary
        mydb = mysql.connector.connect(host="localhost", user="root", password="sk270405")
        mycur = mydb.cursor()
        mycur.execute("CREATE DATABASE IF NOT EXISTS PyBank")
        mycur.execute("USE PyBank")  # Ensure you are using the right database

        # Create table if not exists
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

        # Check if passwords match
        if pcode != pccode:
            messagebox.showerror("Error", "Password and Confirm Password do not match")
            return  # Exit the function if passwords do not match

        # Check for existing accounts with the same name, father name, and birth date
        mycur.execute("SELECT * FROM Accounts WHERE name=%s AND fname=%s AND birth=%s", (name, fname, bdate))
        account_exists = mycur.fetchone()

        # Ensure account number is unique
        while True:
            mycur.execute("SELECT * FROM Accounts WHERE account_no=%s", (str(n),))
            if not mycur.fetchone():  # If no account exists with this number, break
                break
            n = random.randint(11111111, 99999999)

        if account_exists:
            messagebox.showerror("Error", "Account already exists")
        elif len(pcode) < 8:
            messagebox.showerror("Error", "Your passcode must be of 8 characters")
        else:
            # Insert new account
            mycur.execute(""" 
                INSERT INTO Accounts (name, fname, birth, phone, account_no, password, email, city,balance)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
            """, (name, fname, bdate, pno, str(n), pcode, eid, cityn,0))
            mydb.commit()

            # Update UI with success message
            result1.config(text=f"Account no: {n}")
            result2.config(text="Account Successfully Created!!")
            messagebox.showinfo("Success", "Account Created Successfully")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        mydb.close()


def openlogin():
    subprocess.Popen(['Python','login.py'])
    root.destroy()
def on_enteru(e):
    user.delete(0,'end')
def on_leaveu(e):
    name=user.get()

    if name=='':
        user.insert(0,'Username')
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
def on_entercode(e):
    password.delete(0,'end')
def on_leavecode(e):
    name=password.get()

    if name=='':
        password.insert(0,'Password')
def on_entercc(e):
    cpassword.delete(0,'end')
def on_leavecc(e):
    name=cpassword.get()

    if name=='':
        cpassword.insert(0,'Confirm Password')
root=Tk()
root.geometry("800x600")
root.configure(bg="#fff")
img = Image.open("newaccount.jpg")
img = img.resize((420, 500), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
Label(root,image=img,bg="white").grid(row=0,column=1)
frame=Frame(root,width=380,height=650,bg="white")
frame.grid(row=0,column=2)
Label(frame,text="Create Account",fg="dark blue",bg="white",font=("Calibri",23,'bold')).place(x=105,y=15)
#########Name
user = Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))

user.place(x=50, y=85)
user.insert(0, 'Username')  # Now this works
user.bind('<FocusIn>',on_enteru)
user.bind('<FocusOut>',on_leaveu)
Frame(frame,width=280,height=2,bg="black").place(x=52,y=109)
# user.bind('<FocusIn>',on_enter)
# user.bind('<FocusOut>',on_leave)
###Fathernane
father = Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
father.place(x=50, y=135)
father.insert(0, 'Father Name')  # Now this works
Frame(frame,width=280,height=2,bg="black").place(x=52,y=155)
father.bind('<FocusIn>',on_enterf)
father.bind('<FocusOut>',on_leavef)
###DOB
birth = Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
birth.place(x=50, y=180)
birth.insert(0, 'DOB(YYYY/MM/DD)')  # Now this works
Frame(frame,width=280,height=2,bg="black").place(x=52,y=200)
birth.bind('<FocusIn>',on_enterb)
birth.bind('<FocusOut>',on_leaveb)
##Phone number
phone= Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
phone.place(x=50, y=223)
phone.insert(0, 'Phone no')  # Now this works
Frame(frame,width=280,height=2,bg="black").place(x=52,y=243)
phone.bind('<FocusIn>',on_enterp)
phone.bind('<FocusOut>',on_leavep)
###Email
email= Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
email.place(x=50, y=265)
email.insert(0, 'Email')  # Now this works
Frame(frame,width=280,height=2,bg="black").place(x=52,y=285)
email.bind('<FocusIn>',on_entere)
email.bind('<FocusOut>',on_leavee)
###City
city= Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
city.place(x=50, y=310)
city.insert(0, 'City')  # Now this works
Frame(frame,width=280,height=2,bg="black").place(x=52,y=330)
city.bind('<FocusIn>',on_enterc)
city.bind('<FocusOut>',on_leavec)
###Password
password= Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
password.place(x=50, y=355)
password.insert(0, 'Password')  # Now this works
Frame(frame,width=280,height=2,bg="black").place(x=52,y=375)
password.bind('<FocusIn>',on_entercode)
password.bind('<FocusOut>',on_leavecode)

##confirm Password
cpassword= Entry(frame, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
cpassword.place(x=50, y=395)
cpassword.insert(0, 'Confirm Password')
cpassword.bind('<FocusIn>', on_entercc)
cpassword.bind('<FocusOut>', on_leavecc)
# Now this works
Frame(frame,width=280,height=2,bg="black").place(x=52,y=420)
Button(frame,width=30,pady=7,text="Create Account",bg="Orange",fg="white",command=signin,border=0,font=("Calibri",13,'bold')).place(x=52,y=450)
Label(frame,text="Already have an account?",fg="black",bg="white",font=("Calibri",11,'bold')).place(x=52,y=500)
signup=Button(frame,width=6,text="Sign up",border=0,bg="white",cursor='hand2',fg="#57a1f8",font=("Calibri",11,'bold'),command=openlogin).place(x=215,y=497)
# Define the Label first, without calling .place() on the same line
result1 = Label(frame, text="", font=("Calibri", 13, 'bold'), fg="red", bg="white")
result1.place(x=52, y=530)  # Call .place() separately

result2 = Label(frame, text="", font=("Calibri", 13, 'bold'), fg="red", bg="white")
result2.place(x=52, y=560)  # Call .place() separately
root.mainloop()