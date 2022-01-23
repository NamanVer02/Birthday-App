import pywhatkit as pyw
import tkinter as tk
from datetime import date

date_now = date.today().day
month_now = date.today().month
year_now = date.today().year
month_full = date.today().strftime('%B')
people = [['Naman', '8219763511', 22, 8], ['Mehak', '7876862742', 2, 1]]
birthday_babies = []

for i in range(len(people)):
    name = people[i][0]
    number = '+91' + people[i][1]
    date = people[i][2]
    month = people[i][3]

    if date == date_now and month == month_now:
        birthday_babies.append(people[i])

window = tk.Tk()

def sendwhatsapp(number, name):
    pyw.sendwhatmsg_instantly(number, f'Happy Birthday {name}:)', tab_close=False)

def takeinput():
    inpname = inputname.get()
    inpphone = inputphone.get()
    inpdate = inputdate.get()
    people.append([inpname, inpphone, inpdate.split(' ')])

    print(people)

window_title = tk.Label(master=window,
                        text=f"Today is {date_now} {month_full}, {year_now}",
                        anchor='center',
                        bg='black',
                        fg='white'
                        )
window_title.configure(anchor='center',
                       font=('default', 20)
                       )
window_title.pack()

inputname = tk.Entry(window, width=20)
inputphone = tk.Entry(window, width=20)
inputdate = tk.Entry(window, width=20)
inputname.pack()
inputphone.pack()
inputdate.pack()

inputbutton = tk.Button(window, text='Log', command=takeinput)
inputbutton.pack()

window.title('Sending Birthday Wishes')
window.geometry('500x500')
window.config(bg='black')
window.mainloop()









