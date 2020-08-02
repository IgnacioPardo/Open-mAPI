import requests
from bs4 import BeautifulSoup
from openmapi.provincia import Provincia

class Registros():

	#Provincias de Argentina y sus Keys dentro de la API
	provincias = {
						'BA_C': None,
						'BA_P': None,
						'CA': None,
						'CH': None,
						'CB': None,
						'CD': None,
						'CR': None,
						'ER': None,
						'FO': None,
						'JY': None,
						'LP': None,
						'LR': None,
						'MD': None,
						'MI': None,
						'NE': None,
						'RN': None,
						'SA': None,
						'SJ': None,
						'SL': None,
						'SC': None,
						'SF': None,
						'SE': None,
						'TF': None,
						'TU': None
					}

	def __init__(self):
		for key in self.provincias.keys():
			self.provincias[key] = Provincia(key)
		self.casos = {
			'infectados': None, 
			'recuperados': None,
			'fallecidos': None, 
			'activos': None,
		}

	#Devuelve objeto Provincia de la Provincia especificada
	def getProvincia(self, key):
		return self.provincias[key]

	#Devuelve el nombre de la Provincia especificada
	def getNombreProvincia(self, key):
		return str(self.getProvincia(key))

	#Actualiza la informacion de todas las provincias
	def loadAllProvincias(self):
		for prov in self.provincias.values():
			prov.loadAllData()
		return self.provincias

	#Actualiza la informacion de la Provincia especificada
	def reloadProvincia(self, key):
		self.getProvincia(key).loadAllData()
		return self.getProvincia(key)

	#Devuelve todas los casos de la Provincia especificada
	def getCasosProvincia(self, key, info):
		if not self.provincias[key]:
			self.provincias[key] = Provincia(key)
			self.loadProvincias(key)
		return self.getProvincia(key).getCasos(info)

	#Devuelve los casos en una Fehca de la Provincia especificada
	def getCasosProvinciaEnFecha(self, key, fecha):
		if not self.provincias[key]:
			self.provincias[key] = Provincia(key)
			self.loadProvincias(key)
		return self.getProvincia(key).getFecha(fecha)

	#Devuelve el historial por fecha de la Provincia especificada
	def getHistorialCasosProvincia(self, key):
		return self.getProvincia(key).getHistorial()
	
	#Devuelve el Total de casos en el Pais al dia de hoy.
	def getTotal(self):
		url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		table = soup.find_all("table", class_="wikitable")[0]

		infectados = None
		recuperados = None
		activos = None
		fallecidos = None


		for tr in table.find_all('tr'):
			row = [''.join(cell.stripped_strings) for cell in tr.find_all(['td', 'th'])]
			if 'Argentina[n]' in row:
				infectados = int(row[2].replace(',','')) if ',' in row[2] else int(row[2])
				fallecidos = int(row[3].replace(',','')) if ',' in row[3] else int(row[3])
				recuperados = int(row[4].replace(',','')) if ',' in row[4] else int(row[4])
				activos = infectados-(recuperados+fallecidos)

		self.casos = {
			'infectados': infectados, 
			'recuperados': recuperados,
			'fallecidos': fallecidos, 
			'activos': activos,
		}

		return self.casos