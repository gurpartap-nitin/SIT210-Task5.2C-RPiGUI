from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


win = Tk()
win.title("Task 5.2C");
font_var = tkinter.font.Font(family = "Aerial", size = 14, weight = "bold")

led1 = LED(17)
led2 = LED(27)
led3 = LED(4)
value = IntVar()

def toggle():
    value1 = value.get()
    if value1 == 1:
        led1.on()
        led2.off()
        led3.off()
        
    if value1 == 2:
        led1.off()
        led2.on()
        led3.off()

    if value1 == 3:
        led1.off()
        led2.off()
        led3.on()
    else:
        led1.off()
        led2.off()
        led3.off()

def programclose():
    win.destroy()
    GPIO.cleanup()

button1 = Radiobutton( win, text = "TURN ON LED 1", font = font_var, variable = value, value = 1, command = toggle, height = 2, width = 20)
button1.grid( row = 0, column = 1)

button2 = Radiobutton( win, text = "Turn ON LED 2 ", font = font_var, variable = value, value = 2, command = toggle, height = 2, width = 20)
button2.grid( row = 1, column = 1)

button3 = Radiobutton( win, text = "Turn ON LED 3", font = font_var, variable = value, value = 3, command = toggle, height = 2, width = 20)
button3.grid( row = 2, column = 1)

close_button = Button(win, text = "FINISH", font = font_var, command = programclose,height = 1, width = 10)
close_button.grid( row = 3, column = 1)
win.mainloop()