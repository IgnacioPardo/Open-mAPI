import requests
from bs4 import BeautifulSoup
from openmapi.fechas import Fechas

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