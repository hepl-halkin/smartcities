# Introduction
Le but de ctte partie est d'apprendre à realiser une connexion WiFi afin de pouvoir aller chercher des informations tels que lamétéo via OpenWeathermap et l'heure via NTP pour les affichers tout les 2 sur un écran LCD. Pour ce faire on utlise les modules network, socket et urequests.

## Les différents modules
Ces modules contiennent de nombreuses fonctions, je vais vous présenter ceux que j'ai utilisé dans le cadre de ce chapitre.

### Module network
- ```WLAN.active(True)``` est utilisée pour activer l'interface WLAN (Wi-Fi) sur le périphérique. En appelant cette fonction avec le paramètre True, l'interface WLAN sera activée, permettant au périphérique de se connecter à des réseaux Wi-Fi disponibles.

- ```WLAN.connect(ssid, password)```: Cette fonction est utilisée pour se connecter à un réseau Wi-Fi spécifié. Elle prend en paramètres le nom du réseau (SSID) et le mot de passe associé. En appelant cette fonction avec les informations d'identification appropriées, le périphérique tentera de se connecter au réseau Wi-Fi spécifié.

- ```network.WLAN(network.STA_IF)```: Cette ligne de code crée une instance de l'objet WLAN (Wi-Fi) en mode client (STA_IF). Cela permet d'interagir avec l'interface WLAN en tant que client, ce qui inclut des fonctionnalités telles que la connexion à un réseau Wi-Fi, la déconnexion, la vérification de l'état de la connexion, etc.

- ```WLAN.isconnected()```: Cette fonction est utilisée pour vérifier si le périphérique est actuellement connecté à un réseau Wi-Fi. Elle renvoie généralement une valeur booléenne (True ou False) pour indiquer si la connexion Wi-Fi est active ou non. Cette fonction est utile pour vérifier l'état de la connexion avant d'effectuer des opérations dépendantes de la connectivité réseau.

### Module socket
- ```socket.getaddrinfo()``` effectue une résolution DNS (Domain Name System) pour traduire un nom d'hôte en une adresse IP. En spécifiant le nom d'hôte et le numéro de port, la fonction renvoie une liste de tuples contenant différentes informations sur les adresses IP disponibles pour le nom d'hôte et le port spécifiés.
- 

### Module urequests
- ```urequest.get(url)``` est utilisée pour effectuer une requête GET HTTP vers une URL spécifiée. Elle prend en paramètre l'URL cible vers laquelle la requête GET doit être envoyée.

## [NTP](NTP.py)
Le Network Time Protocol permet de synchroniser l'horloge d'un appareilavec l'heure UTC en se servant des portocols UDP et IP. Grâce à ce protocol et à une connexion WiFi on affiche la date et l'heure dans le fuseau horaire de notre choix sur l'ecran LCD.

## [OpenWeatherMap](NTP_OWM_WiFi.py)
Il s'agit d'un site permettant de voir et recevoir les conditions méteorologiques de la terre entiere via un API. Gràce à la connexion WiFi et en modifiant l'URL de base du site avec les coordonnées de la ville choisie, dans l'unitée choisie et avec notre clé API. Il suffit ensuite d'envoyer une requete via l'URL et d'afficher les informations recues sur l'ecran LCD.
![7l51rn](https://github.com/hepl-halkin/smartcities/assets/125503055/33f1cb77-c33f-4aee-892a-0ede4eeb189d)
