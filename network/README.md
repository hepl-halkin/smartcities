# Network
Le but de ctte partie est d'apprendre à realiser une connexion WiFi afin de pouvoir aller chercher des informations tels que lamétéo via OpenWeathermap et l'heure via NTP pour les affichers tout les 2 sur un écran LCD. Pour ce faire on utlise les modules network, sockets et urequests.

## [NTP](NTP_OWM_WiFi.py)
Le Network Time Protocol permet de synchroniser l'horloge d'un appareilavec l'heure UTC en se servant des portocols UDP et IP. Grâce à ce protocol et à une connexion WiFi on affiche la date et l'heure dans le fuseau horaire de notre choix sur l'ecran LCD.

## [OpenWeatherMap](NTP_OWM_WiFi.py)
Il s'agit d'un site permettant de voir et recevoir les conditions méteorologiques de la terre entiere via un API. Gràce à la connexion WiFi et en modifiant l'URL de base du site avec les coordonnées de la ville choisie, dans l'unitée choisie et avec notre clé API. Il suffit ensuite d'envoyer une requete via l'URL et d'afficher les informations recues sur l'ecran LCD.
