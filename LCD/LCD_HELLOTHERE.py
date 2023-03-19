from lcd1602 import LCD1602
from machine import I2C, Pin
from utime import sleep

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000) #Définition de la pin i2c, 1=numéro de la pin i2c, scl=pin utilisée pour l'utilisation de la serial clock, sda=pin utilisée pour l'envoie de data entre le raspberry et l'écran LCD, freq= fréquence maximum de scl.
d = LCD1602(i2c, 2, 16) # i2c=moyen de communication des datas, nombres de lignes et de caractéres.

d.display()
sleep(1)
d.clear
d.print('Hello there')

sleep(2)
d.setCursor(0,1) #Permet d'écrire sur la 2eme ligne
d.print('General Kenobi')