# Imports go at the top
from microbit import *
x = 0
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        x= 0
    elif button_a.get_presses():
        x = x + 1
    elif button_b.get_presses():
        x = x - 1
    elif pin_logo.is_touched():
        display.scroll("Arian")
    else:
        display.show(x)
