# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *
 
# Create Object
clock = Tk()
 
# set name
clock.title=("Xtra-laj")
# Set geometry
clock.geometry("600x300")
 
# Use Threading
def original_time():
    t1=Thread(target=alarm)
    t1.start()
 
def alarm():
    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
 
        # Wait for one seconds
        time.sleep(1)
 
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
 
# Add Labels, Frame, Button, Optionmenus
Label(clock,text="Alarm Clock",font=("Helvetica 20 bold"),fg="olive").pack(pady=10)
Label(clock,text="Set Time",fg="navyblue",font=("Helvetica 15 bold")).pack()
 
frame = Frame(clock)
frame.pack()
 
hour = StringVar(clock)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(clock)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 
second = StringVar(clock)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
 
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)
 
Button(clock,text="Set Alarm",fg="lightgreen",font=("Helvetica 15 italic bold"),command=original_time).pack(pady=20)
 
# Execute Tkinter
clock.mainloop()