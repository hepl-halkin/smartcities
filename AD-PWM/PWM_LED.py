# # Varying LED luminosity
from machine import Pin, PWM
import utime
 
pwm = PWM(Pin(20)) #On définit la Pin D20 comme PWM
pwm.freq(500) #On définit la fréquence de la PWM
 
##linear variation
while True:
     for i in range(20): #Boucle for où i augmente de 1 à chaque boucle, jusqu'a atteindre 20
         pwm.duty_u16(i*3276) #On multiplie la valeur de i par 3276 et on envoie la valeur à la LED
         utime.sleep_ms(100) #Attente de 100 ms avant de recommencer la boucle

# # # quadratic variation
#lum=[]
#for i in range(20):
#     lum.append(i*i)

#while True:
#    for i in range(20):
#         pwm.duty_u16(i*181)
#         utime.sleep_ms(100)