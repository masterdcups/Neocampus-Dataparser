import csv
import annotationUnique

def genererDataBN(fichierE,fichierS):

    # Ouverture du fichier qui contiendra les données annotées
    fichier = open(fichierS,"w")

    # Ouverture du fichier qui contient les données non annontées
    with open(fichierE,encoding='utf-8') as f:
        reader = csv.reader(f,delimiter=';')
        
        num_ligne = 0

        for line in reader:
            # Première ligne du fichier qui contient la liste des champs
            if num_ligne == 0:
                new_line = line[1] + ";" + line[4] + ";" + line[5] + ";" + line[6] + ";" + line[7] + "\n"
                       
            else:
                if line[1] == "jour":
                    period = 1
                else:
                    period = 0
                new_line = str(period) + ";" + str(annotationUnique.temperature(float(line[4]))) + ";" + str(annotationUnique.luminosite(float(line[5]))) + ";" + str(annotationUnique.co2(float(line[6]))) + ";" + str(annotationUnique.humidite(float(line[7]))) + "\n"

            # Écriture dans le fichier de sortie    
            fichier.write(new_line)
            num_ligne += 1

    fichier.close()

genererDataBN("./dataAgregatAnnote.csv","./dataBN.csv")
