import csv
import annotationUnique

def parcourirFichier(fichierE,fichierS):
	
	tableauId = [ "ilot1","ilot2","ilot3","ouest","57","79" ]
	
	for value in tableauId
		nomFichier = "fichier" + value + ".csv"
		fichier = open(nomFichier,"w")
		with open(fichierE,encoding='utf-8') as f:
	 
			reader = csv.reader(f,delimiter=';')
        
			num_ligne = 0

			for line in reader:
				if num_ligne == 0:
					new_line = line[0] + ";" + line[1] + ";" + line[2] + ";" + line[3] + ";" + line[4] + ";" + line[5] + "\n"
				else:
					if line[5] == value:
						new_line = line[0] + ";" + line[1] + ";" + line[2] + ";" + line[3] + ";" + line[4] + ";" + line[5] + "\n"
						
					  
										
					
					
				fichier.write(new_line)				

		fichier.close()

    

lireFichier("./dataBrut.csv","./")

