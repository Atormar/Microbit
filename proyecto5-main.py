# Imports go at the top
from microbit import *
i=0
amigos=["a","am","ami","amig","amigo","migo","igo","go","o"]

while True:
    if button_a.get_presses():
        i=i+1
        sleep(500)
    elif button_b.get_presses():
        i=i-1
        sleep(500)

    if i>len(amigos)-1:
        i=0
    elif i<0:
        i=len(amigos)-1
    else:
        display.show(i)
        sleep(500)
        display.show(amigos[i])
        sleep(500)