import tkinter as tk
from tkinter import messagebox
import pymysql


conn=pymysql.connect(host="localhost",user="root",password="root",db="collage")
print("o.k")

def mysave():
    cur = conn.cursor()
    cur.execute("insert into emp values(" + txt1.get() + ",'" + txt2.get() + "'," + txt3.get() + ")")
    conn.commit ()
    
    messagebox.showinfo("Title", "Saved")
    cur.close()

def clear():
    txt1.delete (0,20)
    txt2.delete (0,last=20)
    txt3.delete (0,last=20)
    txt1.focus()
    
def cancel():
    root.destroy()

def find():
    try:
        cur= conn.cursor()
        n=txt1.get()
        clear()
        cur.execute("select * from emp where eno=" + n)
        r=cur.fetchall()
        txt1.insert(0,r[0][0])
        txt2.insert(0,r[0][1])
        txt3.insert(0,r[0][2])
    except Exception as err:
        messagebox.showinfo("Error","Number Not Found ")

def edit():
    cur = conn.cursor()
    cur.execute("update emp set esal=" + txt3.get() + " where eno=" + txt1.get() )
    conn.commit()
    messagebox.showinfo("Title","Updated")
    cur.close()
def delete():
    cur = conn.cursor()
    cur.execute("delete from emp where eno=" + txt1.get() )
    conn.commit()
    messagebox.showinfo("Title","Deleted")
    cur.close()
    clear()
        

 
root = tk.Tk()
root.title("Emp Form")    
w = 400
h = 400
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

labe = tk.Label(root, text="EMP DATA FORM ", font=("Arial Bold",15)   )
labe.place(x=130, y=20)

label = tk.Label(root, text="Enter Emp Number  : ")
label.place(x=20, y=60)

labe2 = tk.Label(root, text="Enter Emp Name    : ")
labe2.place(x=20, y=130)

labe3 = tk.Label(root, text="Enter Emp Salalry : ")
labe3.place(x=20, y=200)

txt1 = tk.Entry(root,width=20)
txt1.place(x=180, y=60)

txt2 = tk.Entry(root,width=20)
txt2.place(x=180, y=130)

txt3 = tk.Entry(root,width=20)
txt3.place(x=180, y=200)

button1 = tk.Button(root, text="New",width=15,height=2,command=clear)
button1.place(x=30, y=250)

button2 = tk.Button(root, text="Save", width=15,height=2,command=mysave)
button2.place(x=150, y=250)


button3 = tk.Button(root, text="Cancel", width=15,height=2,command=cancel)
button3.place(x=280, y=250)


button4 = tk.Button(root, text="Find",width=15,height=2,command=find)
button4.place(x=30, y=300)

button5 = tk.Button(root, text="Edit", width=15,height=2,command=edit)
button5.place(x=150, y=300)


button6 = tk.Button(root, text="Delete", width=15,height=2,command=delete)
button6.place(x=280, y=300)
  
txt1.focus ()

root.mainloop()
