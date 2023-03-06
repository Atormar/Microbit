# Imports go at the top
from microbit import *
import music

while True:
    if button_a.was_pressed():
        display.show(Image.HEART)
        music.play(music.NYAN)
    elif button_b.was_pressed():
        display.show(Image.HEART_SMALL)
        music.play(music.DADADADUM)
        