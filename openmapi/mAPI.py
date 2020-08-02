import requests
from bs4 import BeautifulSoup

class Fechas():
	
	provs = ['Date', 'BA_C', 'BA_P', 'CA', 'CH', 'CB', 'CD', 'CR', 'ER', 'FO', 'JY', 'LP', 'LR', 'MD', 'MI', 'NE', 'RN', 'SA', 'SJ', 'SL', 'SC', 'SF', 'SE', 'TF', 'TU', 'Total', 'D', 'NC', 'ND']
	resultados = []
	resultados.append(provs)
	fechas = ['-']
	def __init__(self):
		None

	def getReferences(self):
		url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Argentina_medical_cases"

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')
		sup = soup.find_all("sup")
		for s in sup:
			s.decompose()
		refs = soup.find_all("ol", class_="references")

		return str('<a href="'+url+'">Wikipedia</a>\n<p>Notes:</p>'+str(refs[0])+'\n'+'<p>References:</p>'+str(refs[1])).replace('^','').replace('<i>','').replace('</i>','').replace('<cite>','').replace('</cite>','').replace('(in Spanish)', '')


	def load(self):

		url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Argentina_medical_cases"

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		table = soup.find_all("table", class_="wikitable")[0]

		noise = table.find_all('a')
		for a in noise:
			a.decompose()

		for tr in table.find_all('tr'):
			row = [''.join(cell.stripped_strings) for cell in tr.find_all(['td', 'th'])]
			if 'Date' not in row:
				if 'Total' not in row:
					if 'Cml' not in row:
						csvline = []
						for elem in row:
							if '(' in elem:
								if ' ' in elem:
									elem = elem.split(' ')[0]
								else:	
									elem = elem.split('(')[0]
							csvline.append(elem)
						self.fechas.append(csvline[0])
						self.resultados.append(csvline)
		self.fechas = self.fechas[:-2]
		self.resultados = self.resultados[:-2]


	def getFecha(self, date):

		if len(self.resultados) == 1:
			self.load()

		fecha_indice = self.fechas.index(date)
		prov_indice = self.provs.index(self.key)
		return self.resultados[fecha_indice][prov_indice]
		
	def getHistorial(self):

		if len(self.resultados) == 0:
			self.load()
		
		prov_indice = self.provs.index(self.key)

		return [[fecha[0], fecha[prov_indice]] for fecha in self.resultados[1:]]


class Provincia(Fechas):

	apiEquiv = {
		'BA_C': 'Buenos-Aires-Autonomous-City',
		'BA_P': 'Buenos-Aires-Province',
		'CA': 'Catamarca',
		'CH': 'Chaco',
		'CB': 'Chubut',
		'CD': 'Córdoba',
		'CR': 'Corrientes',
		'ER': 'Entre-Ríos',
		'FO': 'Formosa',
		'JY': 'Jujuy',
		'LP': 'La-Pampa',
		'LR': 'La-Rioja',
		'MD': 'Mendoza',
		'MI': 'Misiones',
		'NE': 'Neuquén',
		'RN': 'Río-Negro',
		'SA': 'Salta',
		'SJ': 'San-Juan',
		'SL': 'San-Luis',
		'SC': 'Santa-Cruz',
		'SF': 'Santa-Fe',
		'SE': 'Santiago-del-Estero',
		'TF': 'Tierra-del-Fuego',
		'TU': 'Tucumán'
	}

	data = {}
	endpoints = ['infectados', 'fallecidos', 'recuperados']
	provincia = ''
	informacion = ''
	key = ''

	def __init__(self, prov=None):
		self.key = prov
		self.provincia = self.apiEquiv[prov]

	def loadAllData(self):

		url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Argentina_medical_cases_by_province"

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		noise = soup.find_all('td', attrs={'style':'padding:0px 2px;'})

		for td in noise:
			td.decompose()

		noise = soup.find_all('img')
		for img in noise:
			img.decompose()
		noise = soup.find_all('a')
		for a in noise:
			a.decompose()

		table = soup.find("table", class_="wikitable")
		trs = table.find_all('tr', class_="")

		html_table = '<table><tbody>'
		for tr in trs:
			html_table += str(tr)
		html_table += '</tbody></table>'

		soup = BeautifulSoup(html_table, 'html.parser')
		indices = ['Provincia', 'infectados', 'fallecidos', 'recuperados']
		resultados = []
		for table_num, table in enumerate(soup.find_all('table')):
			for tr in table.find_all('tr'):
				row = [''.join(cell.stripped_strings) for cell in tr.find_all(['td', 'th'])]
				resultados.append(row[1:])
		resultados = resultados[1:]

		for row in resultados:
			provKey = row[0].replace(' ', '-').replace('(', '').replace(')', '')
			self.data[provKey] = {
						indices[1]: row[1],
						indices[2]: row[2],
						indices[3]: row[3]
					}
		
	def newProvincia(self, prov):
		self.key = prov
		self.provincia = self.apiEquiv[prov]

	def __str__(self):
		return self.provincia

	def getCasos(self, info):

		if len(self.data.keys()) == 0:
			self.loadAllData()

		return self.data[self.provincia][info]


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