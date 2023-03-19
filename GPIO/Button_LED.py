import machine
from machine import Pin

#On définit les pins ainsi que leurs sens d'utilisations
LED = Pin("LED", Pin.OUT)
BUTTON = machine.Pin(20,machine.Pin.IN)

#Boucle WHILE permettant d'allumer la LED lorsqu'on appuie sur le bouton-poussoir
while True:
    BUTTON_VAL = BUTTON.value()     #Valeur du bouton
    if BUTTON_VAL == 1:             #Est-on en train d'appuyer sur le bouton?
        LED.value(1)                #Si oui on allume la LED
    elif BUTTON_VAL == 0:           #Si on appuye pas sur le bouton
        LED.value(0)                #On éteint la led