# AD-PWM
Dans cette partie nous allons apprendre à controler différents appareils tels que: une LED, un potentiométre et un buzzer en utilisant des signaux PWM.

#PWM
PWM est le diminutif en anglais de modulation de largeur d'impulsion. L'impulsion est un signal numérique envoyé périodiquement par le microcontroleur et variant entre 2 états: on et off. Le but de la PWM est de faire varier le duty cycle, c'est à dire le temps passé en ON divisé par le temps total nécessaire passer entre le début de 2 niveaux ON, autrement dit le cycle. Le dernier paramétres est la fréquence, elle définit le nombres de cycles par secondes. En faisant varier le duty cycle, la tension moyenne varie également ce qui nous permet de controller différents appareils. 

![image](https://user-images.githubusercontent.com/125503055/226172526-3d7635ff-4b82-401c-bacd-b449c4dda4d3.png)
# Differents codes
## [Lecture de la valeur du potentiométre](Potentiometre.py)
![pot_lect](https://user-images.githubusercontent.com/125503055/226173950-e18c0e54-1c8b-4dbc-8b7c-a2b6da9af846.gif)

## [Variation de la luminosité de la LED](PWM_LED.py)
### Linéaire
![lineaire](https://user-images.githubusercontent.com/125503055/226174325-a3ff8c48-6f2d-4923-a6d8-3be313f46c31.gif)
### Quadratique
![quadratique](https://user-images.githubusercontent.com/125503055/226174330-f328e2d7-24e1-48ba-988a-d20448506d0f.gif)
## [Controle de la LED via un potentiométre](POT_LED.py)
![pot_led](https://user-images.githubusercontent.com/125503055/226173958-ab89537d-0721-4f51-8a08-2183bb9793af.gif)

## [Jouer de la musique avec le buzzer](Buzzer.py)
![image](https://user-images.githubusercontent.com/125503055/226174530-6bbdd6b1-1f5a-45ac-9e6f-4365e38f70fc.png)
