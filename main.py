from provincia import Provincia

prov = Provincia("BA_C")
cantidad = prov.getInfo("fallecidos")
print(cantidad)
cantidad_fecha = prov.getFecha('3 Jun')
print(cantidad_fecha)
historial = prov.getAllHistory()
print(historial)