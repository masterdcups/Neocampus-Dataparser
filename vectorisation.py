import csv
import annotationUnique
import datetime


def transformationDuTemps(date):

	numberMin1 = date[15]
	numberMin2 = date[14]
	numberHeure1 = date[12]
	numberHeure2 = date[11]
	return (int(numberMin1) + 10 * int(numberMin2) + (int(numberMin1) + 10 * int(numberMin2)) * 60 )

	
def deuxMinDEccard (date1,date2):

	temps1 = datetime.datetime(int(date1[0] + date1[1] + date1[2] + date1[3]),int(date1[5] + date1[6]),int(date1[8] + date1[9]),int(date1[11] + date1[12]),int(date1[13] + date1[14] ),int(date1[15] + date1[16]))
	temps2 = datetime.datetime(int(date2[0] + date2[1] + date2[2] + date2[3]),int(date2[5] + date2[6]),int(date2[8] + date2[9]),int(date2[11] + date2[12]),int(date2[13] + date2[14] ),int(date2[15] + date2[16]))
	return(datetime.timedelta(temps2 - temps1) < datetime.datetime.minute(2))
	
def parcourirFichier(fichierE,fichierS):
	
	
	#fichierEntre = open(fichierE,"r")
	fichierSortie = open(fichierS,"w")
	luminosity = 0
	temperature = 0
	co2 = 0
	humidity = 0
	nbluminosity = 0
	nbtemperature = 0
	nbco2 = 0
	nbhumidity = 0
	annotation = 0
	
	premiere_valeur = 0
	
	with open(fichierE,encoding='utf-8') as f:
		reader = csv.reader(f,delimiter=';')
		num_ligne = 0
		
		for line in reader:
						
			if num_ligne > 1:
				date2 = line[3]
				if deuxMinDEccard(date1,date2):
					if line[0] == "temperature":
						temperature += annotationUnique.temperature(float(line[2]))
						nbtemperature += 1
					if line[0] == "humidity":
						humidity += annotationUnique.humidite(float(line[2]))
						nbhumidity += 1
					if line[0] == "luminosity":
						luminosity += annotationUnique.luminosite(float(line[2]))
						nbluminosity += 1
					if line[0] == "co2":
						co2 += annotationUnique.co2(float(line[2]))  
						nbco2 += 1
				
				else:
					temperature = temperature / nbtemperature
					luminosity = luminosity / nbluminosity
					co2 = co2 / nbco2
					humidity = humidity / nbhumidity
					new_line = (str(temperature) + ";" +str(luminosity) + ";" + str(co2) + ";" + str(humidity) + ";" + annotationUnique.annotationCapteur(temperature,luminosity,co2,humidity) + "\n")
					fichierSortie.write(new_line)
					luminosity = 0
					temperature = 0
					co2 = 0
					humidity = 0
					nbluminosity = 0
					nbtemperature = 0
					nbco2 = 0
					nbhumidity = 0
					
					
					if line[0] == "temperature":
						temperature = annotationUnique.temperature(float(line[2]))
						nbtemperature = 1
					if line[0] == "humidity":
						humidity = annotationUnique.humidite(float(line[2]))
						nbhumidity = 1
					if line[0] == "luminosity":
						luminosity = annotationUnique.luminosite(float(line[2]))
						nbluminosity = 1
					if line[0] == "co2":
						co2 = annotationUnique.co2(float(line[2]))  
						nbco2 = 1
					
				
			else :
				if num_ligne == 0:
					new_line = "temperature" + ";" + "luminosity" + ";" + "co2" + ";" + "humidity" + ";" + "annotation" + "\n"
					fichierSortie.write(new_line)
					
				else : 
					date1 = line[3]
					date2 = line[3]
					if line[0] == "temperature":
						temperature = annotationUnique.temperature(float(line[2]))
						nbtemperature = 1
					if line[0] == "humidity":
						humidity = annotationUnique.humidite(float(line[2]))
						nbhumidity = 1
					if line[0] == "luminosity":
						luminosity = annotationUnique.luminosite(float(line[2]))
						nbluminosity = 1
					if line[0] == "co2":
						co2 = annotationUnique.co2(float(line[2]))  
						nbco2 = 1

		temperature = temperature / nbtemperature
		luminosity = luminosity / nbluminosity
		co2 = co2 / nbco2
		humidity = humidity / nbhumidity
		new_line = (str(temperature) + ";" + str(luminosity) + ";" + str(co2) + ";" + str(humidity) + ";" + annotationUnique.annotationCapteur(temperature,luminosity,co2,humidity) + "\n")
		fichierSortie.write(new_line)
		
	fichierSortie.close()			
		
		







