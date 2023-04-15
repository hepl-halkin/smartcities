from ws2812 import WS2812
from machine import Pin
from utime import sleep

Pir = Pin(20, Pin.IN)
led = WS2812(18,1)

while True:
    if Pir.value()==1: #Lorsque le capteur detecte du mouvement la LED s'allume en rouge, dans le cas contraire est reste allumée en vert
        led.pixels_fill((255, 0, 0))
        led.pixels_show()
        sleep(0)
    else:
        led.pixels_fill((0, 255, 0))
        led.pixels_show()