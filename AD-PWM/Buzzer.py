from machine import Pin,PWM
from utime import sleep

#On déclare le buzzer comme étant connecté à la pin D20
buzzer = PWM(Pin(20))

#Choix du volume
vol = 500

#Définition des fonctions des différentes notes dont nous aurons besoin plus tard
def DO(time):
    #Joue la note au volume définit précedemment 
    buzzer.duty_u16(vol)
    #Fréquence de la note
    buzzer.freq(1046)
    #Durée de la note
    sleep(time)
def RE(time):
    buzzer.duty_u16(vol)
    buzzer.freq(1175)
    sleep(time)
def MI(time):
    buzzer.duty_u16(vol)
    buzzer.freq(1318)
    sleep(time)
def FA(time):
    buzzer.duty_u16(vol)
    buzzer.freq(1397)
    sleep(time)
def SOL(time):
    buzzer.duty_u16(vol)
    buzzer.freq(1568)
    sleep(time)
def LA(time):
    buzzer.duty_u16(vol)
    buzzer.freq(1760)
    sleep(time)
def SI(time):
    buzzer.duty_u16(vol)
    buzzer.freq(1967)
    sleep(time)
def N(time):
    buzzer.duty_u16(0)
    sleep(time)

while True:
    #Utilisation des notes définies
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    N(0.01)

    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)

    MI(0.25)
    FA(0.25)
    SOL(0.5)

    MI(0.25)
    FA(0.25)
    SOL(0.5)
    N(0.01)

    SOL(0.125)
    LA(0.125)
    SOL(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)

    SOL(0.125)
    LA(0.125)
    SOL(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)

    RE(0.25)
    SOL(0.25)
    DO(0.5)
    N(0.01)

    RE(0.25)
    SOL(0.25)
    DO(0.5)
    N(5)