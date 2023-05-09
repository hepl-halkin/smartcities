import network
import ntptime
import urequests
from lcd1602 import LCD1602 
from machine import I2C, Pin
from utime import sleep, localtime

# Informations de connexion Wi-Fi
ssid = 'AndroidAP' 
password = '12345678' 

# Connexion au Wi-Fi
wlan = network.WLAN(network.STA_IF) #On crée l'objet WLAN et on l'initialise
wlan.active(True) #Active la capacité de se connecter
wlan.connect(ssid, password) #Connexion à un réseau wifi en fonction des informations de connexions
while not wlan.isconnected(): #Ne passe à l'étape suivant que si la connexion est réussie
    pass


ntptime.settime() #Permet de recuperer la date et l'heure à partir du serveur NTP

#Informations relatives à l'utilisations d'OpenWeathermap
api_key = '8046f2244685304eea10b4b26d379757' 
ville = 'Liege' 
pays = 'BE'
key = {'lat': '50.6337',
       'lon' : '5.5675',
       'appid' : '8046f2244685304eea10b4b26d379757',
       'units' : 'metric'}
url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + key['lat'] + '&lon=' + key['lon'] + '&appid=' + key['appid'] +'&units=' + key['units']
print(url)

#Permet de récuperer les données météorologiques grâce l'API OpenWeatherMap
def get_weather_data():
    try:
        response = urequests.get(url)
        data = response.json()
        return data
    except:
        return None

#Parametrage de l'écran LCD1602
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
lcd = LCD1602(i2c, 2, 16)

#Boucle while permettant d'afficher les différentes informations de maniére succesive
while True:
    #Ici on affiche le pays et la ville choisie   
    lcd.clear()    
    lcd.print("Pays: {}".format(pays))    
    lcd.setCursor(0, 1)
    lcd.print("Ville: {}".format(ville))
    sleep(2)
    
    current_time = localtime()
    adjusted_hour = (current_time[3] + 2) % 24

    #Affichage de la date et de l'heure est paramettrant le fuseau horaire correspond à la ville choisie
    lcd.clear()
    lcd.print("Date: {:02d}-{:02d}-{:02d}".format(current_time[2], current_time[1], current_time[0]))
    lcd.setCursor(0, 1)
    lcd.print("Heure: {:02d}:{:02d}:{:02d}".format(adjusted_hour, current_time[4], current_time[5]))
    sleep(2)
    
    
    weather_data = get_weather_data()
    #Affichage de la météo de la ville choisie
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        lcd.clear()
        lcd.print("Temp: {:.1f}".format(temperature))
        lcd.write(0b11011111) 
        lcd.print("C") 
        lcd.setCursor(0, 1)
        lcd.print("humidite: {}%".format(humidity))
        sleep(2)
