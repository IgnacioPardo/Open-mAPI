from open_mapi.registros import Registros

data = Registros()

fall_ba_c = data.getCasosProvincia("BA_C", "fallecidos")
dia_ba_c = data.getCasosProvinciaEnFecha("BA_C", "3 Jun")
hist_ba_c = data.getHistorialCasosProvincia("BA_C")

print(fall_ba_c)
print(dia_ba_c)
print(hist_ba_c)

BA_C = data.getProvincia("BA_C")

recu_ba_c = BA_C.getCasos("recuperados")
ida_ba_c = BA_C.getFecha('18 Jul')
hist_ba_c = BA_C.getHistorial()

print(BA_C)
print(recu_ba_c)
print(ida_ba_c)
print(hist_ba_c)