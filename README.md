# Projet Smartcities
Dans le cadre du projet smartcities, nous allons apprendre à utiliser le Raspberry Pi Pico W gràce au starter kit Grove qui va nous permettre de découvrir les différentes fonctionnalités tels que:

- [GPIO](GPIO): LED simple, bouton-poussoir et interruption.
- [AD-PWM](AD-PWM): Lecture d'un potentiométre et utilisation de signaux PWM
- [LCD](LCD): documentation des fonctions de la librairie et affichage de la valeur du potentiomètre.
- [LED_NEO](LED_NEO): utilisation des LEDs néopixel, documentation des fonctions de la librairie, arc-en-ciel.
- [sensors](sensors): température et humidité, luminosité, PIR.
- [network](network): Accès réseau avec le RasPberry Pi Pico.

Le but de cette démarche est de pouvoi par la suite controller differents appareils du Smart Corridor.

# Raspberry Pi Pico W
Le microcontrôleur RP2040 intégré dans le Pico W est un processeur ARM Cortex-M0+ cadencé à 133 MHz, avec 264 Ko de mémoire flash et 32 Ko de mémoire vive (RAM). Le Pico W dispose également de 26 broches d'entrées/sorties (GPIO) qui peuvent être configurées pour différentes tâches, telles que la communication série, l'I2C, le SPI et bien d'autres.
Couplé au Raspberry, nous utiliserons les modules grooves fournit avec le shield afin de faciliter la connection entre les différents modules et la carte.
![image](https://user-images.githubusercontent.com/125503055/225649778-d0dcf8b4-b458-4cfa-b0a9-a7c24f574728.png)

# Micropython
Le Micropython est une variante de Python omptimisée et allégées pour les microcontroleurs et les systémes embarqués. Il permet aux développeurs de créer des applications embarquées en utilisant un langage de programmation familier et facile à apprendre. Il dispose d'un ensemble de modules standard, tels que les modules pour la gestion des entrées/sorties, les réseaux, le temps, les mathématiques, les chaînes de caractères, etc. qui permettent de gérer facilement les périphériques connectés.

# Thonny
Il existe de nombreux environnements pour programmer en python et micropython, dnas notre cas nous utiliserons Thonny car c'est le plus simple à utiliser.
