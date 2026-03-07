from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='prajwal'and passwordEntry.get()=='12345':
        messagebox.showinfo('success','Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','wrong credentials')


root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('login page')
image= CTkImage(Image.open('ima3.jpg'),size=(500,370))
ImageLabel=CTkLabel(root,image=image,text='')
ImageLabel.place(x=370,y=70)
headinglabel=CTkLabel(root,text='Roll Call System',font=('Goudy Old Style',22,'bold'),text_color='black')
headinglabel.place(x=35,y=100)

usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username',width=180)
usernameEntry.place(x=80,y=150)

passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password',width=180,show='*')
passwordEntry.place(x=80,y=200)

loginButton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=100,y=250)

root.mainloop()


