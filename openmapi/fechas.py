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
						if 'Aut. city' not in row:
							if 'Notes:The' not in row:
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

		self.load()
		
		prov_indice = self.provs.index(self.key)

		return [[fecha[0], fecha[prov_indice]] for fecha in self.resultados[1:] if len(fecha) > 1]
