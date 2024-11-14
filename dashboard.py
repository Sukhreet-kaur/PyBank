from tkinter import *
from tkinter import messagebox
import subprocess
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="sk270405",database='PyBank')
mycur=mydb.cursor()
from PIL import Image, ImageTk
root=Tk()
root.geometry("1200x550")
# root.configure(bg="#fff")
def profile_view():
    subprocess.Popen(["Python", "view_profile.py"])
    root.quit()
def update1():
    subprocess.Popen(["Python", "update.py"])
    root.quit()
def dash():
    subprocess.Popen(["Python","dashboard.py"])
    root.quit()
def delete1():
    subprocess.Popen(["Python", "delete.py"])
    root.quit()
def cardinfo():
    mycur.execute("SELECT * FROM login")
    a = mycur.fetchone()
    if a is None:
        messagebox.showinfo("Info", "No login information found.")
        return
    account_no = a[0]

    # Fetch the account information from the Accounts table based on account_no
    mycur.execute("SELECT * FROM Accounts WHERE account_no=%s", (account_no,))
    data = mycur.fetchone()  # Fetch the first row from Accounts table

    if data is not None:
        # Display the account and balance information
        account.config(text=data[4])  # Assuming the first column is account info
        balance.config(text=data[8])
        name.config(text=data[0])# Assuming the 9th column is the balance
    else:
        messagebox.showinfo("Info", "No account information found.")

def logout():
    subprocess.Popen(["Python","login.py"])
    root.quit()
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
##Credit Card
img5 = Image.open("credit.jpg")
img5 = img5.resize((30, 30), Image.Resampling.LANCZOS)
img5 = ImageTk.PhotoImage(img5)
Label(frame,image=img5,bg="white",cursor="hand2").place(x=30,y=330)
credit=Label(frame,text="Credit Card",cursor="hand2",font=("Calibri",14),fg="dark blue",bg="white")
credit.place(x=110,y=330)
##update
img6 = Image.open("update.jpg")
img6 = img6.resize((25, 25), Image.Resampling.LANCZOS)
img6 = ImageTk.PhotoImage(img6)
Label(frame,image=img6,bg="white",cursor="hand2").place(x=30,y=380)
update=Label(frame,text="Update Profile",cursor="hand2",font=("Calibri",14),fg="dark blue",bg="white")
update.place(x=110,y=380)
update.bind("<Button-1>", lambda e: update1())
##loan
# img7 = Image.open("loan.jpg")
# img7 = img7.resize((25, 25), Image.Resampling.LANCZOS)
# img7 = ImageTk.PhotoImage(img7)
# Label(frame,image=img7,bg="white",cursor="hand2").place(x=30,y=430)
# loan=Label(frame,text="Loan",cursor="hand2",font=("Calibri",14),fg="dark blue",bg="white")
# loan.place(x=110,y=430)
##delete
img8 = Image.open("delete.jpg")
img8 = img8.resize((25, 25), Image.Resampling.LANCZOS)
img8 = ImageTk.PhotoImage(img8)
Label(frame,image=img8,bg="white",cursor="hand2").place(x=30,y=430)
delete=Label(frame,text="Delete Account",cursor="hand2",font=("Calibri",14),fg="dark blue",bg="white")
delete.place(x=110,y=430)
delete.bind("<Button-1>", lambda e: delete1())
##logout
img9 = Image.open("logout.jpg")
img9 = img9.resize((22, 22), Image.Resampling.LANCZOS)
img9 = ImageTk.PhotoImage(img9)
Label(frame,image=img9,bg="white",cursor="hand2").place(x=30,y=480)
delete=Label(frame,text="Logout",cursor="hand2",font=("Calibri",14),fg="dark blue",bg="white")
delete.place(x=110,y=480)
delete.bind("<Button-1>", lambda e: logout())
##navbar
nav=Frame(root,width=1200,height=70,bg="white").place(x=260,y=0)
Label(nav,text="Dashboard",font=("Calibri",22,'bold'),fg="dark blue",bg="white").place(x=300,y=20)
##card
Label(nav,text="My Card",font=("Calibri",16,'bold'),fg="dark blue").place(x=310,y=90)
card=Frame(root,width=430,height=230,bg="#F3C623").place(x=310,y=130)
chip = Image.open("chip.jpg")
chip = chip.resize((50, 40), Image.Resampling.LANCZOS)
chip = ImageTk.PhotoImage(chip)
Label(card,image=chip,bg="#F3C623").place(x=670,y=150)
Label(card,text="Balance",font=("Calibri",13),fg="black",bg="#F3C623").place(x=340,y=150)
card1=Frame(root,width=430,height=70,bg="orange").place(x=310,y=290)
Label(card,text="Rs.",font=("Calibri",17,'bold'),fg="black",bg="#F3C623").place(x=340,y=180)
balance=Label(card,text="0",font=("Calibri",17,'bold'),fg="black",bg="#F3C623")
balance.place(x=380,y=180)
Label(card,text="Card Holder",font=("Calibri",13),fg="black",bg="#F3C623").place(x=340,y=220)
Label(card,text="Valid till",font=("Calibri",13),fg="black",bg="#F3C623").place(x=620,y=220)
name=Label(card,text="ABC",font=("Calibri",17,'bold'),fg="black",bg="#F3C623")
name.place(x=340,y=250)
Label(card,text="12/27",font=("Calibri",17,'bold'),fg="black",bg="#F3C623").place(x=620,y=250)
account = Label(card, text="", font=("Calibri", 17, 'bold'), fg="white", bg="orange")
account.place(x=340, y=310)  # Place the label
cardinfo()  # Bind the event
fp=Frame(root,width=390,height=400,bg="white").place(x=790,y=130)
Frame(fp,width=390,height=70,bg="orange").place(x=790,y=130)
Label(fp,text="Recent Transactions",font=("Calibri",20,'bold'),fg="white",bg="orange").place(x=870,y=140)
Frame(fp,width=390,height=25,bg="#F3C623").place(x=790,y=200)
Label(fp,text="Description",font=("Calibri",11,'bold'),fg="black",bg="#F3C623").place(x=790,y=200)
Label(fp,text="Amount",font=("Calibri",11,'bold'),fg="black",bg="#F3C623").place(x=1114,y=200)
Label(fp,text="Date",font=("Calibri",11,'bold'),fg="black",bg="#F3C623").place(x=1000,y=200)
f1=Frame(fp,width=390,height=60,bg="white").place(x=790,y=220)
Label(root,text="No Transaction Yet!!",font=("Calibri",16,'bold'),fg="black",bg="white").place(x=830,y=250)
f2=Frame(fp,width=390,height=60,bg="white").place(x=790,y=280)
f3=Frame(fp,width=390,height=60,bg="white").place(x=790,y=340)
f4=Frame(fp,width=390,height=60,bg="white").place(x=790,y=400)
f5=Frame(fp,width=390,height=60,bg="white").place(x=790,y=460)

Label(root,text="We believe in your",font=('Calibri',30,'bold','italic')).place(x=330,y=400)
Label(root,text="trust and support!!",font=('Calibri',30,'bold','italic'),fg="dark blue").place(x=350,y=460)
root.mainloop()