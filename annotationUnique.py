# -*- coding: utf-8 -*-
"""
Annotation des données selon un seuil défini par les spécifications du Google doc suivant :
https://docs.google.com/document/d/1vtwxloreLhoaFz1Pv8dX8Ovy9aDcBi80iWPXRxZvmLY/edit

"""

# Annotation température
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

# Annotation luminosité
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

# Annotation Co2
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

# Annotation humidité
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

# Fonction de calcul de poids sur les différents capteurs (température, luminosité, Co2, humidité)
def annotationCapteur(valeurTemperature, valeurLuminosite, valeurCo2, valeurHumidite):
    annotationRetour = 0
    poidTemperature = 0.3
    poidLuminosite = 0.2
    poidCo2 = 0.4
    poidHumidite = 0.1
    annotationRetour += poidTemperature * temperature(valeurTemperature)
    annotationRetour += poidLuminosite * luminosite(valeurLuminosite)
    annotationRetour += poidCo2 * co2(valeurCo2)
    annotationRetour += poidHumidite * humidite(valeurHumidite)

    return str(annotationRetour);
