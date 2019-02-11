import csv
import annotationUnique
import vectorisation
import datetime

def lireFichier(fichierE,fichierS):

    # Ouverture du fichier qui contiendra les données annotées
    fichier = open(fichierS,"w")

    # Ouverture du fichier qui contient les données non annontées
    with open(fichierE,encoding='utf-8') as f:
        reader = csv.reader(f,delimiter=';')
        
        num_ligne = 0

        for line in reader:
            # Première ligne du fichier qui contient la liste des champs
            if num_ligne == 0:
                new_line = line[0] + ";" + line[1] + ";" + line[2] + ";" + line[3] + ";period;" + line[4] + ";" + line[5] + ";annotation\n"
            
            # Création de l'annotation            
            else:
                if line[0] == "temperature":
                    annotation = annotationUnique.temperature(float(line[2]))
                if line[0] == "humidity":
                    annotation = annotationUnique.humidite(float(line[2]))
                if line[0] == "luminosity":
                    annotation = annotationUnique.luminosite(float(line[2]))
                if line[0] == "co2":
                    annotation = annotationUnique.co2(float(line[2]))   
                
                if (vectorisation.jourNuit(line[3])):
                    period = "jour"
                else:
                    period = "nuit"
                new_line = line[0] + ";" + line[1] + ";" + line[2] + ";" + line[3] + ";" + period + ";" + line[4] + ";" + line[5] + ";" + str(annotation) + "\n"

            # Écriture dans le fichier de sortie    
            fichier.write(new_line)
            num_ligne += 1

    fichier.close()

    return num_ligne

res = lireFichier("./dataBrut.csv","./dataAnnote.csv")
print(res)