from machine import Pin
import utime

led = Pin("LED", Pin.OUT) #Configuration de la LED integrée comme étant une sortie

#while True:      #Dans ce cas, on utilise la fonction toggle afin d'activer/désactiver la LED avec entre une pause 500 ms grâce à la fonction ultime.sleep
#    led.toggle()
#    utime.sleep_ms(500)

while True:    #Ici on choisit de faire varier la valeur de la LED manuellement avec une pause de 500 ms entre chaque changement de valeur
    led.value(1)
    utime.sleep_ms(500)
    led.value(0)
    utime.sleep_ms(500)    