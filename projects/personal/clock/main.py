from datetime import datetime
import tkinter as tk
from tkinter import ttk
import webbrowser

root = tk.Tk()
frame = ttk.Frame(root)
frame.pack(padx=20,pady=20)

class Clock:
    def __init__(self):
        self.current_time = datetime.now().strftime("%I:%M %p")
        self.text = tk.Label(root,text= self.current_time,font=("Arial", 48))
        self.text.pack()

        self.alarms = []

    def update_clock(self):
        self.current_time = datetime.now().strftime("%I:%M %p")
        self.text.config(text=self.current_time)
        if self.current_time in self.alarms:
            webbrowser.open_new("https://www.youtube.com/watch?v=TWrULS-yweQ&t=1888s")
            self.alarms.remove(self.current_time)
        root.after(200,self.update_clock)

class Alarm:
    def __init__(self):
        self.alarm_text = tk.Label(root,text="hold",font=("Arial", 16))
        self.alarm_text.pack()

        #add the drop downs for hr min and am or pm
        self.hours_box = ttk.Combobox(frame,values =[f"{i:02d}" for i in range(1,13)],)
        self.minutes_box = ttk.Combobox(frame,values = [f"{i:02d}" for i in range(61)])
        self.am_pm_box = ttk.Combobox(frame,values = ["AM","PM"])

        #setting default values 
        self.hours_box.set("00")
        self.minutes_box.set("00")
        self.am_pm_box.set("AM")

        #getting the new stuff on the screen
        self.hours_box.grid(row=0,column=0,padx=5)
        self.minutes_box.grid(row=0,column=1,padx=5)
        self.am_pm_box.grid(row=0,column=2,padx=5)

    def add_alarm(self):
        hour,min,am_pm = self.hours_box.get(),self.minutes_box.get(),self.am_pm_box.get()
        if hour.isdigit() and min.isdigit() and (am_pm == "AM" or am_pm == "PM"):
            clock.alarms.append(f"{hour}:{min} {am_pm}")
            self.alarm_text = tk.Label(root,text=f"{hour}:{min} {am_pm}",font=("Arial", 16))
            self.alarm_text.pack()
        else:
            print("failed to add")

    
clock = Clock()
alarm = Alarm()
root.title("Brycen's Clock")

adding_button = ttk.Button(frame,text= "Add Alarm",command=alarm.add_alarm)
adding_button.grid(row=1, column=0, columnspan=3, pady=10)

clock.update_clock()
#this is at the end nothing past this point
root.mainloop()
