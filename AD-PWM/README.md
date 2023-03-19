# AD-PWM
Dans cette partie nous allons apprendre à controler différents appareils tels que: une LED, un potentiométre et un buzzer en utilisant des signaux PWM.

#PWM
PWM est le diminutif en anglais de modulation de largeur d'impulsion. L'impulsion est un signal numérique envoyé périodiquement par le microcontroleur et variant entre 2 états: on et off. Le but de la PWM est de faire varier le duty cycle, c'est à dire le temps passé en ON divisé par le temps total nécessaire passer entre le début de 2 niveaux ON, autrement dit le cycle. Le dernier paramétres est la fréquence, elle définit le nombres de cycles par secondes. En faisant varier le duty cycle, la tension moyenne varie également ce qui nous permet de controller différents appareils. 

![image](https://user-images.githubusercontent.com/125503055/226172526-3d7635ff-4b82-401c-bacd-b449c4dda4d3.png)
# Differents codes
## [Lecture de la valeur du potentiométre](Potentiometre.py)

## [Variation de la luminosité de la LED](PWM_LED.py)

## [Controler de la LED via un potentiométre] (POT_LED.py)

## [Jouer de la musique avec le buzzer] (Buzzer.py)
