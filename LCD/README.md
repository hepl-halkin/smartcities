# LCD
Nous allons apprendre maintenant comment utiliser l'écran LCD pour afficher différents types d'informations.
## Principes de fonctionnement
Un écran LCD utilise la technologie des cristaux liquides, ces derniers sont capables de modifier leurs indices de réfraction en fonction de l'intensité des champs électriques qui leurs sont appliqués. Cela permet, en faisant passer une source de lumiére sur les cristaux, d'afficher divers messages et informations.

![image](https://user-images.githubusercontent.com/125503055/226176159-108087a2-de94-4d46-887e-c1ec8d03510c.png)
## Librairies utilisées
Afin de se simplifier la tache on telechrage une librairie destinée à utiliser un ecran LCD1602, celle ci permet de crée un objet LCD1602 dont on aura besoind pour interagir avec l'écran.
### Les différentes commandes présente dans la librairie que nous utilisons
- d.display() Permet d'allumer l'écran
- d.clear() Permet d'effacer les eventuelles informations affichées sur l'écran
- d.print() Permet d'afficher des informations
- d.setCursor(,) Permet de choisir la lignes et colognes où on veut afficher des informations
# Les différents codes
## [Affichage d'un message](LCD_HELLOTHERE.py)
![20230319_141433](https://user-images.githubusercontent.com/125503055/226177617-3eff2a5b-044d-4722-a155-e2b0605c217c.gif)
## [Affichage de la valeur d'un potentiométre](LCD_POT.py)
![20230319_141957](https://user-images.githubusercontent.com/125503055/226177817-b31d349f-127d-46ed-9980-3b80309cc90a.gif)
## [Affichage de la valeur d'un potentiométre et variation de la luminosité d'une LED](LCD_POT_LED.py)
![20230319_142303](https://user-images.githubusercontent.com/125503055/226177951-241b249e-2519-460d-ae6d-a7a232e49b78.gif)
