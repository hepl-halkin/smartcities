 # Potentiometer reading    
from machine import ADC
import utime

#Connection de la pin A0 au potentiométre
pot = ADC(0)
 
while True: #Boucle while pour lire la valeur du potentiométre
    val= pot.read_u16() #Lecture de la valeur analogique du potentiométre et enregistrement de celle-ci comme val
    print(val) #Affichage de la valeur de "val" qui est donc la valeur renvoyée par la pin du potentiométre
    utime.sleep_ms(500) #attente de 500 ms avant de recommencer la boucle
