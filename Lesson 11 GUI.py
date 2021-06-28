"""from tkinter import *

window = Tk()
window.title("First GUI APP")

textLabel = Label(window, text="Hello, ", font=("Calibri", 20), width=30)

textLabel.grid(row=0, column=0)

textEntry = Entry(window, bg='white', fg='black', font=("Calibri", 20), width=30)
textEntry.grid(row=1, column=0)

window.mainloop()"""
"""from tkinter import *

window = Tk ()
window.title("Zadacha 1")

textLabel = Label(window, text = "GUI APPLICATION", font = ("Comic sans", 20), width = 30)

textLabel.pack(expand = True, fill = BOTH)

window.mainloop()"""

from tkinter import *
from tkinter.ttk import Combobox


def execute():
    name = nameEntry.get()
    surname = surnameEntry.get()
    city = cityBox.get()
    workplace = job.get()
    resultBox.insert(END, name + " " + surname + " - " + city + " - " + workplace)
    refresh()

def refresh():
    nameEntry.delete(0, END)
    nameEntry.insert(0, "")

    surnameEntry.delete(0, END)
    surnameEntry.insert(0, "")

    cityBox.current(0)

def clearList():
    resultBox.delete(0, END)


window = Tk()
window.title("Приложение для регистрации клиентов")

surnameLabel = Label(window, text = "Фамилия:", font = "Calibri 14")
surnameLabel.grid(row = 0, column = 0, padx = 20, pady = 20)

nameLabel = Label(window, text = "Имя:", font = "Calibri 14")
nameLabel.grid(row = 1, column = 0, padx = 20, pady = 20)

cityLabel = Label(window, text = "Родной город:", font = "Calibri 14")
cityLabel.grid(row = 2, column = 0, padx = 20, pady = 20)

workLabel = Label(window, text = "Место работы:", font = "Calibri 14")
workLabel.grid(row = 3, column = 0, padx = 20, pady = 20)

surnameEntry = Entry(window, fg = 'black', width = 17, font = "Calibri 14")
surnameEntry.grid(row = 0, column = 1, padx = 20, pady = 20)

nameEntry = Entry(window, fg = 'black', width = 17, font = "Calibri 14")
nameEntry.grid(row = 1, column = 1, padx = 20, pady = 20)

cities = ["Алматы", "Семей", "Павлодар", "Жезказган", "Талдыкорган"]

cityBox = Combobox(window, values = cities, width = 15, font = "Calibri 14")
cityBox['state'] = 'readonly'
cityBox.current(0)
cityBox.grid(row = 2, column = 1, padx = 20, pady = 20)

job = Entry(window, fg = 'black', width = 17, font = "Calibri 14")
job.grid(row = 3, column = 1, padx = 20, pady = 20)

button = Button(window, width = 20, text = "Добавить", command = execute,
                font = "Calibri 14", bg = "Green", fg = "White")
button.grid(row = 4, column = 1, padx = 20, pady = 20)

resultBox = Listbox(window, width = 35, height = 10, font = "Calibri 14")
resultBox.grid(row = 5, column = 0, columnspan = 2, padx = 20, pady = 20)

window.mainloop()


