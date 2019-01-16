# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def temperature(valeur):
    if(valeur < 24.2 and valeur > 19.8):
        return 0
    elif(valeur > 24.2):
        return 1
    else:
        return -1

def luminosite(valeur):
    if(valeur > 500 and valeur < 1000):
        return 0
    elif(valeur < 500):
        return -1
    else:
        return 1

def co2(valeur):
    if(valeur<1200):
        return 0
    else:
        return 1
    
def humidite(valeur):
    if(valeur < 60 and valeur > 40):
        return 0
    else:
        return 1

def annotationCapteur(valeurTemperature, valeurLuminosite, valeurCo2, valeurHumidite):
    annotationRetour = ""
    
    #Température
    if(temperature(valeurTemperature) == 0):
        annotationRetour += "0"
    elif(temperature(valeurTemperature) == -1):
        annotationRetour += "-1"
    else:
        annotationRetour += "1"
    
    #Luminosité
    if(luminosite(valeurLuminosite) == 0):
        annotationRetour += "0"
    elif(luminosite(valeurLuminosite) == -1):
        annotationRetour += "-1"
    else:
        annotationRetour += "1"

    #Co2
    if(co2(valeurCo2) == 0):
        annotationRetour += "0"
    else:
        annotationRetour += "1"

    #Humidité
    if(humidite(valeurHumidite) == 0):
        annotationRetour += "0"
    else:
        annotationRetour += "1"

    return annotationRetour;
