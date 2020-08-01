# Open mAPI (v2.0)
API COVID 19 por Provincias Argentinas

mAPI Live hosted: https://www.mapi.live/

Documentacion de mAPI Live en Postman: https://documenter.getpostman.com/view/4501185/T1DsAbwg?version=latestw

Ejemplo:

```
  from Open_mAPI.registros import Registros
  
  data = Registros()

  fall_ba_c = data.getCasosProvincia("BA_C", "fallecidos")

  dia_ba_c = data.getCasosProvinciaEnFecha("BA_C", "3 Jun")

  hist_ba_c = data.getHistorialCasosProvincia("BA_C")
```
