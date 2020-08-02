# Open mAPI (v2.0)
API COVID 19 por Provincias Argentinas

mAPI Live hosted: https://www.mapi.live/

Documentacion de mAPI Live en Postman: https://documenter.getpostman.com/view/4501185/T1DsAbwg?version=latestw

Ejemplo 1:

```
  from Open_mAPI.registros import Registros

  data = Registros()

  fall_ba_c = data.getCasosProvincia("BA_C", "fallecidos")

  dia_ba_c = data.getCasosProvinciaEnFecha("BA_C", "3 Jun")

  hist_ba_c = data.getHistorialCasosProvincia("BA_C")
```
Ejemplo 2

```
  from Open_mAPI.registros import Registros

  data = Registros()

  info = 'infectados'

  casos = [[str(prov), prov.getCasos(info)] for prov in data.provincias.values()]

  mas_casos = max(casos, key=lambda x:x[1])
  print('Provincia con mas casos ' + info + " es " + mas_casos[0] + ' con ' + mas_casos[1] + ' casos.')
```