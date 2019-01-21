import csv
import annotationUnique
import datetime


def deuxMinDEccard (date1,date2):

	temps1 = datetime.datetime(int(date1[0] + date1[1] + date1[2] + date1[3]),int(date1[5] + date1[6]),int(date1[8] + date1[9]),int(date1[11] + date1[12]),int(date1[14] + date1[15] ),int(date1[17] + date1[18]))
	temps2 = datetime.datetime(int(date2[0] + date2[1] + date2[2] + date2[3]),int(date2[5] + date2[6]),int(date2[8] + date2[9]),int(date2[11] + date2[12]),int(date2[14] + date2[15] ),int(date2[17] + date2[18]))
	return((temps2 - temps1) < datetime.timedelta(minutes = 2 ))


def jourNuit(date):
	temps = datetime.datetime(int(date[0] + date[1] + date[2] + date[3]),int(date[5] + date[6]),int(date[8] + date[9]),int(date[11] + date[12]),int(date[14] + date[15] ),int(date[17] + date[18]))
	return temps.hour > 6 and temps.hour < 20
	
def parcourirFichier(fichierE,fichierS):
	
	#fichierEntre = open(fichierE,"r")
	fichierSortie = open(fichierS,"a")
	luminosity = 0
	temperature = 0
	co2 = 0
	humidity = 0
	nbluminosity = 0
	nbtemperature = 0
	nbco2 = 0
	nbhumidity = 0
	#annotation = 0
	date1 = ""
	
	#premiere_valeur = 0 
	valeursSauvegrade = [0,0,0,0]
	
	with open(fichierE,encoding='utf-8') as f:
		reader = csv.reader(f,delimiter=';')
		num_ligne = 0
		
		for line in reader:
						
			if num_ligne > 1:
				date2 = line[3]
				if deuxMinDEccard(date1,date2):
					if line[0] == "temperature":
						temperature += float(line[2]) 
						nbtemperature += 1
					if line[0] == "humidity":
						humidity +=  float(line[2]) 
						nbhumidity += 1
					if line[0] == "luminosity":
						luminosity += float(line[2])
						nbluminosity += 1
					if line[0] == "co2":
						co2 += float(line[2])  
						nbco2 += 1
					num_ligne += 1
				
				else:
					if nbtemperature != 0:
						temperature = temperature / nbtemperature
						valeursSauvegrade[0] = temperature
					else :
						temperature = valeursSauvegrade[0] 					
					if nbluminosity != 0:
						luminosity = luminosity / nbluminosity
						valeursSauvegrade[1] = luminosity
					else :
						luminosity = valeursSauvegrade[1]
					if nbco2 != 0:
						co2 = co2 / nbco2
						valeursSauvegrade[2] = co2
					else :
						co2 = valeursSauvegrade[2]
					if nbhumidity != 0:
						humidity = humidity / nbhumidity
						valeursSauvegrade[3] = humidity
					else :
						humidity = valeursSauvegrade[3] 
					
					if jourNuit(date1):
						period = "jour"
					else:
						period = "nuit"
					new_line = date1 + ";" + period + ";" + line[1] +  ";" + line[5] + ";" + str(temperature) + ";" +str(luminosity) + ";" + str(co2) + ";" + str(humidity) + ";" + annotationUnique.annotationCapteur(temperature,luminosity,co2,humidity) + "\n"
					fichierSortie.write(new_line)
					luminosity = 0
					temperature = 0
					co2 = 0
					humidity = 0
					nbluminosity = 0
					nbtemperature = 0
					nbco2 = 0
					nbhumidity = 0
					date1 = date2
					num_ligne += 1

					if line[0] == "temperature":
						temperature = float(line[2])
						nbtemperature = 1
					if line[0] == "humidity":
						humidity = float(line[2])
						nbhumidity = 1
					if line[0] == "luminosity":
						luminosity = float(line[2])
						nbluminosity = 1
					if line[0] == "co2":
						co2 = float(line[2])  
						nbco2 = 1
					
				
			else :
				if num_ligne == 0:
					new_line ="date;period;uri;subId;temperature;luminosity;co2;humidity;annotation\n"
					fichierSortie.write(new_line)
					num_ligne += 1
					
				else :
					date1 = line[3]
					date2 = line[3]
					if line[0] == "temperature":
						temperature = float(line[2])
						nbtemperature = 1
					if line[0] == "humidity":
						humidity = float(line[2])
						nbhumidity = 1
					if line[0] == "luminosity":
						luminosity = float(line[2])
						nbluminosity = 1
					if line[0] == "co2":
						co2 = float(line[2])  
						nbco2 = 1
					num_ligne += 1

		if nbtemperature != 0:
			temperature = temperature / nbtemperature
			valeursSauvegrade[0] = temperature
		else :
			temperature = valeursSauvegrade[0] 					
		if nbluminosity != 0:
			luminosity = luminosity / nbluminosity
			valeursSauvegrade[1] = luminosity
		else :
			luminosity = valeursSauvegrade[1]
		if nbco2 != 0:
			co2 = co2 / nbco2
			valeursSauvegrade[2] = co2
		else :
			co2 = valeursSauvegrade[2]
		if nbhumidity != 0:
			humidity = humidity / nbhumidity
			valeursSauvegrade[3] = humidity
		else :
			humidity = valeursSauvegrade[3]

		if jourNuit(date1):
			period = "jour"
		else:
			period = "nuit"

		new_line = date1 + ";" + period + ";" + line[1] +  ";" + line[5] + ";" + str(temperature) + ";" + str(luminosity) + ";" + str(co2) + ";" + str(humidity) + ";" + annotationUnique.annotationCapteur(temperature,luminosity,co2,humidity) + "\n"
		fichierSortie.write(new_line)
		
	fichierSortie.close()			

listeE = [ "ilot1.csv","ilot2.csv","ilot3.csv","ouest.csv","57.csv","79.csv" ]
fichierS = "./dataAgregatAnnote.csv"

for nomCapteur in listeE:
	fichierE = "./fichier" + nomCapteur
	parcourirFichier(fichierE,fichierS)

