from tkinter import *
import datetime
import time
from threading import *
from playsound import playsound

def Threading():
    t1=Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        global cnt
        set_alarm_time = f"{hour.get()}:{minute.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M")
        if cnt==0:
            t="waiting for "+set_alarm_time+" alarm"
            Label(root,text=t,font=("Gothic 15 bold")).pack()
            cnt+=1
        if current_time == set_alarm_time:
            cnt-=1
            Label(root,text="time to wake up\'⏰\'",font=("Gothic 15 bold")).pack()
            playsound(r'C:\\Users\\siddh\\Music\\alarm.mp3')
            break
         
def clock():
    hour=time.strftime("%H")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    my_label.config(text=hour+":"+minute+":"+second)
    my_label.after(1000,clock)

#main
cnt=0
root = Tk()
root.title("Alarm Clock")
root.geometry("600x500")
my_label=Label(root,text="",font=("Gothic",48),fg="dark red",bg="black")
my_label.pack(pady=20)
Label(root,text="Alarm Clock",font=("Century 20 bold underline"),fg="green").pack(pady=10)
Label(root,text="Set Time",font=("Corbel 15")).pack()
Label(root,text="hour   min",font=("Consolas 12")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23'
        )
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

Button(root,text="Set Alarm",font=("Consolas 12"),command=Threading).pack(pady=20)
Button(root,text="Exit",font=("Consolas 12"),command=exit).pack(side=LEFT)
clock()
root.mainloop()