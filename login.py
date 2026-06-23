from tkinter import *
from tkinter import messagebox

def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "admin123":
        messagebox.showinfo("Success","Login Successful")
    else:
        messagebox.showerror("Error","Invalid Login")

root = Tk()
root.title("Campus Management System")
root.geometry("500x350")

Label(root,text="Admin Login",
font=("Arial",18,"bold")).pack(pady=20)

Label(root,text="Username").pack()

user_entry = Entry(root,width=30)
user_entry.pack()

Label(root,text="Password").pack()

pass_entry = Entry(root,width=30,show="*")
pass_entry.pack()

Button(root,text="Login",
command=login,
bg="green",
fg="white").pack(pady=20)

root.mainloop()
