from Open_mAPI.registros import Registros

data = Registros()

info = 'infectados'

casos = [[str(prov), prov.getCasos(info)] for prov in data.provincias.values()]

mas_casos = max(casos, key=lambda x:x[1])
print('Provincia con mas casos ' + info + " es " + mas_casos[0] + ' con ' + mas_casos[1] + ' casos.')