from tkinter import*
from datetime import date
root=Tk()
root.title=('Getting stared with Widgets')
root.geometry('400x300')
lbl=Label(text="Hey There",fg="white",bg="purple",height=1,width=300)
name_lbl=Label(text="Full name",bg="red")
name_entry=Entry()
def display():
    name=name_entry.get()
    global message
    message="Welcome to the Aplllication!\n Today's date is:"
    greet="hello " +name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END, date.today())
text_box =Text(height=3)
btn=Button(text="Begin", command=display, height=1,bg="orange")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()