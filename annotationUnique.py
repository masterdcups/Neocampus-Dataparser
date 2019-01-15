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
    if(valeur > 500 and valeur < 2000):
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