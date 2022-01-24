import pywhatkit as pyw
from datetime import date

date_now = date.today().day
month_now = date.today().month
birthday_list = [['Naman', '8319763511', 22, 8], ['Max', '9876862742', 2, 1]]

def checkbirthday(date, month):
    if date == date_now and month == month_now:
        return True
    else:
        return False

def sendwhatsapp(number, name):
    pyw.sendwhatmsg_instantly(number, f'Happy Birthday {name}:)', tab_close=False)

#def sendimage(number, name):
    #pyw.text_to_handwriting(f"Happy Birthday {name} :)", f"{name}.png", rgb=(200, 0, 0))
    #pyw.sendwhats_image(number, f"{name}.png", caption=f"Happy Birthday", tab_close=False)


for i in range(len(birthday_list)):
    name = birthday_list[i][0]
    number = '+91' + birthday_list[i][1]
    date = birthday_list[i][2]
    month = birthday_list[i][3]

    if checkbirthday(date, month):
        print(f"Happy Birthday {name} :)")
        choice = int(input('To send a whatsapp message, press 1 : '))
        if choice == 1:
            sendwhatsapp(number, name)


