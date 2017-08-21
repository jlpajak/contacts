from tkinter import * 
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(name_text.get(), address_text.get(), mobile_text.get(),mail_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(name_text.get(), address_text.get(), mobile_text.get(),mail_text.get())
    list1.delete(0,END)
    list1.insert(END,(name_text.get(), address_text.get(), mobile_text.get(),mail_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], name_text.get(), address_text.get(), mobile_text.get(), mail_text.get())

window=Tk()

window.wm_title("Contacts")

label1=Label(window, text="Name")
label1.grid(row=0, column=0)

label2=Label(window, text="Address")
label2.grid(row=0, column=2)

label3=Label(window, text="Mobile")
label3.grid(row=1, column=0)

label4=Label(window, text="e-mail")
label4.grid(row=1, column=2)

name_text=StringVar()
e1=Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

address_text=StringVar()
e2=Entry(window, textvariable=address_text)
e2.grid(row=0, column=3)

mobile_text=StringVar()
e3=Entry(window, textvariable=mobile_text)
e3.grid(row=1, column=1)

mail_text=StringVar()
e4=Entry(window, textvariable=mail_text)
e4.grid(row=1, column=3)

list1=Listbox(window, height=6, width=40)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll1=Scrollbar(window)
scroll1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window,text="Search", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window,text="Add", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window,text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window,text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()
