from tkinter import *
from tkinter import messagebox
import subprocess
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="sk270405",database='PyBank')
mycur=mydb.cursor()
from PIL import Image, ImageTk
root=Tk()
import random
import string

def generate_captcha(length=6):
    """
    Generate a random CAPTCHA text.

    Args:
        length (int): Length of the CAPTCHA. Default is 6.

    Returns:
        str: Randomly generated CAPTCHA text.
    """
    # Create a pool of characters (letters and digits)
    characters = string.ascii_letters + string.digits
    # Randomly choose characters to create the CAPTCHA
    captcha = ''.join(random.choices(characters, k=length))
    return captcha

# Example usage
captcha_text = generate_captcha()
def deposit1():
    # Ensure the transactions table exists
    mycur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            account_no VARCHAR(50),
            account_holder_name VARCHAR(100),
            description TEXT,
            amount DECIMAL(10, 2),
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    mydb.commit()

    # Fetch account number from login table
    try:
        mycur.execute("SELECT account_no FROM login LIMIT 1")  # Adjust if login table structure varies
        result = mycur.fetchone()
        if result is None:
            messagebox.showerror("Error", "No account is logged in.")
            return
        account_no = result[0]
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error fetching account number: {err}")
        return

    # Retrieve user input
    account_holder_name = user.get()
    description = dis.get()
    amount_value = amount.get()
    captcha_code = captche.get()

    # Check if any field is empty
    if (not account_holder_name or account_holder_name == "Account Holder Name" or
        not description or description == "Description" or
        not amount_value or amount_value == "Amount ( ₹ )" or
        not captcha_code or captcha_code == "Captche Code"):
        messagebox.showerror("Input Error", "All fields are required!")
        return

    # Validate CAPTCHA
    if captcha_code != captcha_text:
        messagebox.showerror("CAPTCHA Error", "Incorrect CAPTCHA. Please try again.")
        return

    try:
        amount_value = float(amount_value)
        if amount_value <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid amount!")
        return

    # Insert transaction into the database
    try:
        mycur.execute("""
            INSERT INTO transactions (account_no, account_holder_name, description, amount)
            VALUES (%s, %s, %s, %s)
        """, (account_no, account_holder_name, description, amount_value))
        mydb.commit()

        # Update the balance in the accounts table
        mycur.execute("""
            UPDATE accounts
            SET balance = balance + %s
            WHERE account_no = %s
        """, (amount_value, account_no))
        mydb.commit()

        messagebox.showinfo("Success", "Money deposited successfully!")
    except mysql.connector.Error as err:
        mydb.rollback()
        messagebox.showerror("Database Error", f"Error: {err}")

def on_entern(e):
    user.delete(0,'end')
def on_leaven(e):
    name=user.get()

    if name=='':
        user.insert(0,'Account Holder Name')
def on_enterd(e):
    dis.delete(0,'end')
def on_leaved(e):
    name=dis.get()

    if name=='':
        dis.insert(0,'Description')
def on_entera(e):
    amount.delete(0,'end')
def on_leavea(e):
    name=amount.get()

    if name=='':
        amount.insert(0,'Amount ( ₹ )')
def on_enterc(e):
    captche.delete(0,'end')
def on_leavec(e):
    name=captche.get()

    if name=='':
        captche.insert(0,'Captche Code')
def delete1():
    subprocess.Popen(["Python", "delete.py"])
    root.quit()
def update1():
    subprocess.Popen(["Python", "update.py"])
    root.quit()
def dash():
    subprocess.Popen(["Python","dashboard.py"])
    root.quit()
def profile_view():
    subprocess.Popen(["Python", "view_profile.py"])
    root.quit()
def logout():
    subprocess.Popen(["Python","login.py"])
    root.quit()
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


pic = Image.open("moneyd.jpg")
pic = pic.resize((410, 476), Image.Resampling.LANCZOS)
pic = ImageTk.PhotoImage(pic)
Label(root,image=pic,bg="white",cursor="hand2").place(x=730,y=30)
Frame(root,width=460,height=480,bg="white").place(x=320,y=30)
Label(root,text="Money Deposit",font=("Calibri",22,'bold'),fg="dark blue",bg="white").place(x=470,y=100)


user = Entry(root, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
user.place(x=420,y=170)
user.insert(0, 'Account Holder Name')  # Now this works
Frame(root,width=280,height=2,bg="black").place(x=420,y=190)
user.bind('<FocusIn>',on_entern)
user.bind('<FocusOut>',on_leaven)
dis = Entry(root, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
dis.place(x=420,y=220)
dis.insert(0, 'Discription')  # Now this works
Frame(root,width=280,height=2,bg="black").place(x=420,y=240)
dis.bind('<FocusIn>',on_enterd)
dis.bind('<FocusOut>',on_leaved)
amount = Entry(root, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
amount.place(x=420,y=270)
amount.insert(0, 'Amount ( ₹ )')  # Now this works
Frame(root,width=280,height=2,bg="black").place(x=420,y=290)
amount.bind('<FocusIn>',on_entera)
amount.bind('<FocusOut>',on_leavea)

captche = Entry(root, width=31, fg="black", border=0, bg="white", font=("Calibri", 13))
captche.place(x=420,y=320)
captche.insert(0, 'Captche Code')  # Now this works
Frame(root,width=280,height=2,bg="black").place(x=420,y=340)
captche.bind('<FocusIn>',on_enterc)
captche.bind('<FocusOut>',on_leavec)
Label(text=captcha_text,font=('Impact',20,'bold', 'italic'),fg='red',bg='light grey',width=15).place(x=450,y=360)

Button(root, width=30, pady=7, text="Deposit Money", bg="Orange", fg="white", border=0, font=("Calibri", 13, 'bold'), command=deposit1).place(x=420, y=420)
root.mainloop()