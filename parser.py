import csv
import annotationUnique

def lireFichier(fichierE,fichierS):

    fichier = open(fichierS,"w")

    with open(fichierE,encoding='utf-8') as f:
        reader = csv.reader(f,delimiter=';')
        
        num_ligne = 0

        for line in reader:
            if num_ligne == 0:
                new_line = line[0] + ";" + line[1] + ";" + line[2] + ";" + line[3] + ";" + line[4] + ";" + line[5] + ";annotation\n"
            else:
                if line[0] == "temperature":
                    annotation = annotationUnique.temperature(float(line[2]))
                if line[0] == "humidity":
                    annotation = annotationUnique.humidite(float(line[2]))
                if line[0] == "luminosity":
                    annotation = annotationUnique.luminosite(float(line[2]))
                if line[0] == "co2":
                    annotation = annotationUnique.co2(float(line[2]))   
                                    
                new_line = line[0] + ";" + line[1] + ";" + line[2] + ";" + line[3] + ";" + line[4] + ";" + line[5] + ";" + str(annotation) + "\n"
                
            fichier.write(new_line)
            num_ligne += 1

    fichier.close()

    return num_ligne

res = lireFichier("C:/Users/Bastien/Desktop/ProjetM2/dataBrut.csv","C:/Users/Bastien/Desktop/ProjetM2/dataAnnote.csv")
print(res)