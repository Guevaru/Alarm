# Import Required Library
from tkinter import *
import datetime 
import time 
import winsound

#definig a function for the actual time
def original_time():
    set_alarm_timer=f"{hours.get()}:{minutes.get()}:{seconds.get()}"
    alarm(set_alarm_timer)
    
#defining a function for the module of setting  the alarm    
def alarm(set_alarm_timer):
    #infinite loop
    while True:
         # Set Alarm
        set_alarm=f"{hours.get()}:{minutes.get()}:{seconds.get()}"
        
        # Wait for one seconds
        time.sleep(1)
        
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
         
         # Check whether set alarm is equal to current time or not
        if current_time == set_alarm:
            print('Time to wake up')
            
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
     
     
#for the GUI
# Create Object
clock = Tk()
#set name
clock.title("Xtra-laj")
# Set geometry
clock.geometry("600x300")
# Add Labels and placeholders
time_format =Label(clock,text = "Enter time in 24:00 hour format!!", fg="skyblue", bg="black",font=("Helvetica" ,20, "italic bold")).place(x=70,y=150)
addTime = Label(clock,text = "hrs            min                sec",font=60).place(x=110)
setYourAlarm=Label(clock,text = "Set time",fg="Olive",relief="solid", font=("Helvetica",17,"bold")).place(x=0, y=29)

frame = Frame(clock)
frame.pack()

     
hours = StringVar(clock)
hour=  ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hours.set(hour[0])
 

 

minutes= StringVar(clock)
minute= ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minutes.set(minute[0])
 


seconds=StringVar(clock)
second= ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
seconds.set(second[0])
 


hourTime= Entry(clock,textvariable=hours,bg="Beige", width=30).place(x=100,y=30)
minutesTime= Entry(clock,textvariable=minutes,bg="Beige", width=35).place(x=200,y=30)
secondsTime= Entry(clock,textvariable=seconds,bg="Beige", width=40).place(x=300,y=30)  

submit = Button(clock,text="Set Alarm",fg="beige", width=20, command = original_time).place(x=150,y= 70)  
     
# Execute Tkinter     
clock.mainloop()

     
     
            
            
        