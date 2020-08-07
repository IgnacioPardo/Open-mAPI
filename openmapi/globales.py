import requests
from bs4 import BeautifulSoup
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

class Globales:

	results = {}
	registers_label = 'Empty'

	def __init__(self):
		self.results = {}

	def count(self):
		self.registers_label = len(self.results.keys())+' registros.'

	def __str__(self):
		return self.registers_label

	def __repr__(self):
		return self.registers_label

	def load(self):
		url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory"
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		noise = soup.find('caption')
		noise.decompose()


		noise = soup.find_all('td', attrs={'style':'padding:0px 2px;'})
		for td in noise:
			td.decompose()

		noise = soup.find_all('img')
		for img in noise:
			img.decompose()
		
		noise = soup.find_all("tr", class_="sortbottom")
		for tr in noise:
			tr.decompose()

		table = soup.find("table", class_="wikitable")

		rows = table.find_all('tr')

		cases, deaths, recov = [title.text.replace('\n', '').replace(',', '.') for title in rows[1].find_all('th')[1:6]][1:4]
		active = int(cases.replace('.', '')) - (int(deaths.replace('.', ''))+int(recov.replace('.', '')))

		self.results['world'] = 	{
								'infectados':cases,
								'fallecidos':deaths,
								'recuperados':recov,
								'activos': active
							}

		rows = rows[2:]

		for row in rows:
			country = row.find_all('th')[1].text.replace('\n', '')
			if '[' in country:
				country = country.split('[')[0]
			res = [title.text.replace('\n', '') for title in row.find_all('td')[0:3]]

			done = False
			for i in range(len(res)):
				if res[i] == 'No data':
					self.results[country] = 	{
											'infectados':cases,
											'fallecidos':deaths,
											'recuperados':recov,
											'activos': '-'
										}
					done = True
				if ',' in res[i]:
					res[i] = res[i].replace(',', '.')
			if not done:
				done = False
				cases, deaths, recov = res
				active = int(cases.replace('.', '')) - (int(deaths.replace('.', ''))+int(recov.replace('.', '')))
				if active > 999:
					active = '{:,}'.format(active).replace(',', '.')
				self.results[country] = 	{
										'infectados':cases,
										'fallecidos':deaths,
										'recuperados':recov,
										'activos': active
									}
	def getCountry(self, country):
		self.load()
		return self.results[country]

	def getCountryInfo(self, country, info):
		self.load()
		return self.results[country][info]

	def getCountryKeys(self):
		self.load()
		return list(self.results.keys())

	def getInfoKeys(self):
		return ['infectados', 'fallecidos', 'recuperados', 'activos']