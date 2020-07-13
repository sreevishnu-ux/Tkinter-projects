import datetime
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mai = tkinter.Tk()

mai.title("Age calculator App")
mai.geometry('620x580')
mai['padx'] = 8
label = tkinter.Label(mai, text="my second tkinter app")
# creating the labels
label.grid(row=0, column=0, columnspan=3)
name = tkinter.Label(text = "Enter your Name")
name.grid(column=0,row=1)
year = tkinter.Label(text = "Enter the Year")
year.grid(column=0,row=2)
month = tkinter.Label(text = "Enter the Month")
month.grid(column=0,row=3)
date = tkinter.Label(text = "Enter the Day")
date.grid(column=0,row=4)

nameEntry = tkinter.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tkinter.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tkinter.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tkinter.Entry()
dateEntry.grid(column=1,row=4)


def getInput():
    name = nameEntry.get()
    man= Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))

    textArea = tkinter.Text(master=mai, height=10, width=25)
    textArea.grid(column=1, row=6)
    answer = " Heyy {man}!!!. You are {age} years old!!! ".format(man=name, age=man.age())
    textArea.insert(tkinter.END, answer)


button=tkinter.Button(mai,text="Calculate Age",command=getInput,bg="blue")
button.grid(column=1,row=5)

class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age


mai.mainloop()
