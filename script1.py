from tkinter import *

#graphical user interface

window = Tk()
window.title("My American converter")

def miles_2_km():
    km = float(e1_value.get()) * 1.60934
    t1.insert(END, km)

def farenheight_2_celsius():
    celsius = (float(e2_value.get()) - 32) / 1.8
    t2.insert(END, celsius)

def ounces_2_ml():
    ml = float(e3_value.get()) * 29.5735
    t3.insert(END, ml)

def gallons_2_ml():
    ml = float(e4_value.get()) * 3785.41
    t4.insert(END, ml)

def pounds_2_kg():
    kg = float(e5_value.get()) * 0.453592
    t5.insert(END, kg)

b1 = Button(window, text = "Miles to Km", command= miles_2_km) #window to specify where
b1.grid(row = 0, column = 0) #to put widget in or pack

b2 = Button(window, text = "Farenheight to Celsius", command = farenheight_2_celsius)
b2.grid(row = 1, column = 0)

b3 = Button(window, text = "Ounces to ml", command = ounces_2_ml)
b3.grid(row = 2, column = 0)

b4 = Button(window, text = "Gallons to ml", command = gallons_2_ml)
b4.grid(row = 3, column = 0)

b5 = Button(window, text = "Pounds to kg", command= pounds_2_kg) #window to specify where
b5.grid(row = 4, column = 0) #to put widget in or pack

e1_value = StringVar() #not an actual string
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e2.grid(row = 1, column = 1)

e3_value = StringVar()
e3 = Entry(window, textvariable = e3_value)
e3.grid(row = 2, column = 1)

e4_value = StringVar()
e4 = Entry(window, textvariable = e4_value)
e4.grid(row = 3, column = 1)

e5_value = StringVar() #not an actual string
e5 = Entry(window, textvariable = e5_value)
e5.grid(row = 4, column = 1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 2)

t2 = Text(window, height = 1, width = 20)
t2.grid(row = 1, column = 2)

t3 = Text(window, height = 1, width = 20)
t3.grid(row = 2, column = 2)

t4 = Text(window, height = 1, width = 20)
t4.grid(row = 3, column = 2)

t5 = Text(window, height = 1, width = 20)
t5.grid(row = 4, column = 2)


window.mainloop() #allows u to press exit button to close
