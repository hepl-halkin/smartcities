from ws2812 import WS2812
from machine import I2C,Pin,ADC
from utime import sleep

led = WS2812(18,1)
LIGHT_SENSOR = ADC(0)
SOUND_SENSOR = ADC(1)

while True:
    average = 0
    light = LIGHT_SENSOR.read_u16()/256 #Permet de lire la valeur envoyée par le light sensor, celle ci est divisée par 256 pour la mettre à l'echelle de la LED RGB.
    for i in range (1000): #Permet de lire la valeur envoyée par le sound sensor, cependant cette valeur varie tout le temps, il est donc necessaire de faire la moyenne pour la stabiliser
        noise = SOUND_SENSOR.read_u16()/256
        average += noise
    noise = average/1000
    print(noise)
    
    if light < 80: #Si la valeur envoyée par le light sensor est inférieur à 80, la LED s'allume en blanc
        led.pixels_fill((255,255,255))
        led.pixels_show()
        sleep(0.1)
    else:
        if noise < 40: #Si la valeur envoyée par le sound sensor est inférieur à 40, la LED s'allume en vert
            led.pixels_fill((0,255,0))
            led.pixels_show()
            sleep(1)   
        if noise >= 40 and noise < 50: #Si la valeur envoyée par le sound sensor est comprise entre 40 et 50, la LED s'allume en jaune
            led.pixels_fill((255,150,0))
            led.pixels_show()
            sleep(1)
        if noise >= 50:
            led.pixels_fill((255,0,0)) #Si la valeur envoyée par le sound sensor est supérieur ou égale à 50, la LED s'allume en rouge
            led.pixels_show()
            sleep(1)