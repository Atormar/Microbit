# Imports go at the top
from microbit import *
import music
import radio



'''

configuracion RADIO

'''
musica=['a5:8', 'b5:8', 'c5:8', 'd5:8', 'c5:8', 'b5:8', 'a5:8', 'b5:8', 'c5:8', 'd5:8', 'c5:8', 'b5:8', 'a5:8', 'b5:8', 'c5:8', 'd5:8', 'c5:8', 'b5:8', 'a5:8']
radio.on()
radio.config(channel=3)
def listransformacion(musica):
    for i in musica:
        mensaje=""
        mensaje=mensaje+i+","
        return mensaje
while True:
    if button_a.was_pressed():
        mensaje="caca"
        radio.send(mensaje)
        display.show(mensaje)
        sleep(1000)
    elif button_b.was_pressed():
        mensaje="de"
        radio.send(mensaje)
        display.show(mensaje)
        sleep(1000)
    elif button_a and button_b:
        mensaje="vaca"
        radio.send(mensaje)
        display.show(mensaje)
        sleep(1000)
    elif accelerometer.was_gesture('shake'):
        radio.send()
    else:
        display.show("?")
        sleep(1000)