from machine import I2C, Pin  # Importe les classes I2C et Pin du module machine
import network, socket  # Importe les modules network et socket
import struct  # Importe le module struct pour le formatage des données
import utime  # Importe le module utime pour la gestion du temps

def get_time(offset=7200, delta=2208988800, host="pool.ntp.org"):
    # Fonction pour récupérer l'heure à partir d'un serveur NTP

    NTP_QUERY = bytearray(48)  # Crée un tableau de bytes de taille 48

    NTP_QUERY[0] = 0x1B  # Définit le premier byte comme 0x1B (correspond à la requête NTP)

    addr = socket.getaddrinfo(host, 123)[0][-1]  # Obtient l'adresse du serveur NTP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Crée un socket UDP

    try:
        s.settimeout(1)  # Définit un délai d'attente de 1 seconde pour les opérations de socket
        res = s.sendto(NTP_QUERY, addr)  # Envoie la requête NTP au serveur
        msg = s.recv(48)  # Reçoit la réponse du serveur NTP
    finally:
        s.close()  # Ferme le socket

    val = struct.unpack("!I", msg[40:44])[0]  # Extrait la valeur du timestamp de la réponse NTP

    t = val - delta  # Calcule le timestamp corrigé en utilisant le décalage et la valeur delta
    tm = utime.gmtime(t + offset)  # Convertit le timestamp en une structure de temps (heure locale)
    return tm  # Retourne la structure de temps

ssid = 'WiFi-2.4-DACA'  # Nom du réseau Wi-Fi
password = 'yeyelle2000'  # Mot de passe du réseau Wi-Fi

wlan = network.WLAN(network.STA_IF)  # Crée une interface Wi-Fi en mode station
wlan.active(True)  # Active l'interface Wi-Fi
wlan.connect(ssid, password)  # Tente de se connecter au réseau Wi-Fi

print("Connection to WiFi network")
print("------------------------------")
print("Trying to connect to WiFi")
print()

retry = 10  # Nombre de tentatives de connexion
while retry > 0:
    wlan_stat = wlan.status()  # Vérifie l'état de la connexion Wi-Fi
    if wlan_stat == 3:
        print("Got IP")  # Si une adresse IP est obtenue, affiche un message
        break
    if wlan_stat == -1:
        raise RuntimeError('WiFi connection failed')  # En cas d'échec de connexion, génère une erreur
    if wlan_stat == -2:
        raise RuntimeError('No AP found')  # Si aucun point d'accès n'est trouvé, génère une erreur
    if wlan_stat == -3:
        raise RuntimeError('Wrong WiFi password')  # Si le mot de passe Wi-Fi est incorrect, génère une erreur

    if wlan.status() < 0 or wlan.status() >= 3:
        break
    retry -= 1  # Décrémente le nombre de tentatives restantes
    utime.sleep(1)  # Attend 1