from machine import ADC,Pin
from time import sleep

#Définition des pins
LED = Pin("LED", Pin.OUT)
Potentiometre = ADC(0)

#Boucle while infinie
while True:
    print(Potentiometre.read_u16()) #Affichage de la valeur du potentiométre
    if Potentiometre.read_u16() > 30000: #Est ce que la valeur lue est supérieur à 30000
        LED.value(1) #Si oui on allume la LED puis on attend 1 seconde avant de recommencer la boucle
        sleep(1)
    else:
        LED.value(0) #Si non on éteint la LED puis on attend 1 seconde avant de recommencer la boucle
        sleep(1)