"""
BookStore :- It's application which provide simple & easy user friendly interface to maintain books details along with various operation like insert,update,view & delete for users.
Creator  : Sunil Nishad
Date    : 10 - Jan - 2023
"""


from tkinter import *
import backend

# Function to establish connection between db and UI
def getListRow(event):
    global selectedTuple
    if listBox.size() == 0:
        return;
    index = listBox.curselection()[0]
    selectedTuple = listBox.get(index)

    entryTitle.delete(0,END)
    entryTitle.insert(END,selectedTuple[1])

    entryAuthor.delete(0, END)
    entryAuthor.insert(END, selectedTuple[2])

    entryYear.delete(0, END)
    entryYear.insert(END, selectedTuple[3])

    entryISBN.delete(0, END)
    entryISBN.insert(END, selectedTuple[4])

def addEntry():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    listBox.insert(END,title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

def viewEntry():
    listBox.delete(0,END)
    for row in backend.view():
        listBox.insert(END,row)

def searchEntry():
    listBox.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        listBox.insert(END,row)

def updateEntry():
    backend.update(selectedTuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

def deleteEntry():
    backend.delete(selectedTuple[0])

def clear():
    listBox.delete(0,END)
    entryTitle.delete(0, END)
    entryAuthor.delete(0, END)
    entryYear.delete(0, END)
    entryISBN.delete(0, END)


# Application UI code

window = Tk()
window.wm_title("Book Store")

labelTitle = Label(window,text="Title")
labelTitle.grid(row=0,column=0)

title_text = StringVar()
entryTitle = Entry(window,textvariable=title_text)
entryTitle.grid(row=0,column=1)

labelAuthor = Label(window,text="Author")
labelAuthor.grid(row=0,column=2)

author_text = StringVar()
entryAuthor = Entry(window,textvariable=author_text)
entryAuthor.grid(row=0,column=3)

labelYear = Label(window,text="Year")
labelYear.grid(row=1,column=0)

year_text = StringVar()
entryYear = Entry(window,textvariable=year_text)
entryYear.grid(row=1,column=1)

labelISBN = Label(window,text="ISBN")
labelISBN.grid(row=1,column=2)

isbn_text = StringVar()
entryISBN = Entry(window,textvariable=isbn_text)
entryISBN.grid(row=1,column=3)


listBox = Listbox(window,height=8,width=35)
listBox.grid(row=2,column=0,rowspan=6,columnspan=2)

listBox.bind('<<ListboxSelect>>',getListRow)

sb = Scrollbar(window)
sb.grid(row=2,column=2,rowspan=6)

listBox.configure(yscrollcommand=sb.set)
sb.configure(command=listBox.yview)

btnView   = Button(window,text="View All",width=12,command=viewEntry)
btnView.grid(row=2,column=3)

btnSearch = Button(window,text="Search Entry",width=12,command=searchEntry)
btnSearch.grid(row=3,column=3)

btnAdd    = Button(window,text="Add Entry",width=12,command=addEntry)
btnAdd.grid(row=4,column=3)

btnUpdate = Button(window,text="Updated Selected",width=12,command=updateEntry)
btnUpdate.grid(row=5,column=3)

btnDelete = Button(window,text="Delete Selected",width=12,command=deleteEntry)
btnDelete.grid(row=6,column=3)

btnClear  = Button(window,text="Clear",width=12,command=clear)
btnClear.grid(row=7,column=3)

btnClose  = Button(window,text="Close",fg="white", bg="black",width=12,command=window.destroy)
btnClose.grid(row=8, column=0, columnspan=2,sticky="s",pady=2)

window.mainloop()