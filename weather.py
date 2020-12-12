from tkinter import *
from tkinter.messagebox import *
import pyowm
from datetime import *


class weather:
    def report(self):
        owm = pyowm.OWM("0972367af178c7e06d0cb660554537c9")
        location = owm.weather_at_place("amritsar")
        weather = location.get_weather()
        temp = weather.get_temperature('celsius')
        self.lb2=Label(self.root,text="temperature: "+str(temp["temp"]))
        self.lb3 = Label(self.root, text="temp_max: "+str(temp["temp_max"]))
        self.lb4 = Label(self.root, text="temp_min "+str(temp["temp_min"]))
        humidity = weather.get_humidity()
        self.lb5=Label(self.root, text="Humidity "+str(humidity))




        self.lb2.pack()
        self.lb3.pack()
        self.lb4.pack()
        self.lb5.pack()

    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x300")
        self.date=datetime.now()

        self.lb1=Label(self.root, text="Enter Location")
        self.tx1=Entry(self.root)

        self.b1=Button(self.root,text="Search", command=self.report)
        self.lb1.pack()
        self.tx1.pack()
        self.b1.pack()
        self.root.mainloop()
owm=weather()