# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def temperature(valeur):
    if(valeur < 23.2 and valeur > 20.8):
        return 5
    elif(valeur < 24.5 and valeur > 19.5):
        return 4
    elif(valeur < 26 and valeur > 18):
        return 3
    elif(valeur < 27 and valeur > 17):
        return 2
    elif(valeur < 28 and valeur > 16):
        return 1
    else:
        return 0

def luminosite(valeur):
    if(valeur > 600 and valeur < 900):
        return 5
    elif(valeur > 550 and valeur < 950):
        return 4
    elif(valeur > 500 and valeur < 1000):
        return 3
    elif(valeur > 400 and valeur < 1100):
        return 2
    elif(valeur > 200 and valeur < 1300):
        return 1
    else:
        return 0

def co2(valeur):
    if(valeur<400):
        return 5
    elif(valeur<600):
        return 4
    elif(valeur<800):
        return 3
    elif(valeur<1000):
        return 2
    elif(valeur<1200):
        return 1
    else:
        return 0
    
def humidite(valeur):
    if(valeur < 55 and valeur > 45):
        return 5
    elif(valeur < 58 and valeur > 42):
        return 4
    elif(valeur < 63 and valeur > 37):
        return 3
    elif(valeur < 70 and valeur > 30):
        return 2
    elif(valeur < 80 and valeur > 20):
        return 1
    else:
        return 0

def annotationCapteur(valeurTemperature, valeurLuminosite, valeurCo2, valeurHumidite):
    annotationRetour = ""
    annotationRetour += str(temperature(valeurTemperature))
    annotationRetour += str(luminosite(valeurLuminosite))
    annotationRetour += str(co2(valeurCo2))
    annotationRetour += str(humidite(valeurHumidite))

    return annotationRetour;
