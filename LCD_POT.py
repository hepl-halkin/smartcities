from lcd1602 import LCD1602
from machine import I2C, Pin, ADC
from utime import sleep

Pot = ADC(0)
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000) #Définition de la pin i2c, 1=numéro de la pin i2c, scl=pin utilisée pour l'utilisation de la serial clock, sda=pin utilisée pour l'envoie de data entre le raspberry et l'écran LCD, freq= fréquence maximum de scl.
d = LCD1602(i2c, 2, 16) # i2c=moyen de communication des datas, nombres de lignes et de caractéres.
d.display()

while True:
    sleep(1)
    d.clear()
    d.setCursor(0,0)
    d.print(str(Pot.read_u16())) # Pot.read_u16 nous retourne un nombre entier or avec la fonction print() on ne peut utiliser que des datas de type "string", on converti donc  les valeurs avec la fonction str(). 
    sleep(1)