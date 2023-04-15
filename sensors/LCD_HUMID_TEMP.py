from lcd1602 import LCD1602
from dht11 import *
from machine import I2C, Pin, ADC
from utime import sleep

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000) #Parametrage du bus I2C
d = LCD1602(i2c, 2, 16)
d.display()
dht = DHT(18)

while True: #Boucle while True permettant d'afficher les valeurs envoyées par le capteur sur l'ecran LCD
    temp,humid = dht.readTempHumid()
    d.setCursor(0,0)
    d.print("Temp:"+str(temp))
    d.setCursor(0,1)
    d.print("Humid:"+str(humid))
    sleep(5) 