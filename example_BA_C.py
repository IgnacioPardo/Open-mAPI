from Open_mAPI.registros import Registros

data = Registros()

fall_ba_c = data.getCasosProvincia("BA_C", "fallecidos")
dia_ba_c = data.getCasosProvinciaEnFecha("BA_C", "3 Jun")
hist_ba_c = data.getHistorialCasosProvincia("BA_C")

print('Fallecidos en BA_C: ' + fall_ba_c)
print('Fallecidos en BA_C el 3 de Junio: ' + dia_ba_c)
#print(hist_ba_c)

BA_C = data.getProvincia("BA_C")

recu_ba_c = BA_C.getCasos("recuperados")
ida_ba_c = BA_C.getFecha('18 Jul')
hist_ba_c = BA_C.getHistorial()

#print(BA_C)
print('Recuperados en BA_C: ' + recu_ba_c)
print('Recuperados en BA_C el 18 de Julio: ' + ida_ba_c)
#print(hist_ba_c)