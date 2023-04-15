from ws2812 import WS2812
import utime

#on définit les différentes couleurs 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)

COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

led = WS2812(18,1)

#Fonction while True permettant de faire changer la couleur de la led toute les 0,2 secondes.
while True:
        print("fills")
        for color in COLORS:
            led.pixels_fill(color)
            led.pixels_show()
            utime.sleep(0.2)