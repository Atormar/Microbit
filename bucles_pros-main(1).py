# Imports go at the top
from microbit import *

while True:
    if button_a.was_pressed():
        for i in range(1,101,5):
            display.scroll(str(i))
            if button_b.was_pressed():
                for i in range(101,1,-1):
                    display.scroll(str(i))
                    
            


    
