# Open mAPI

[![N|Solid](https://www.mapi.live/static/poweredby.png)](https://www.mapi.live)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/IgnacioPardo/Open-mAPI)

Open mAPI brinda registros actualizados sobre el estado de la pandemia actual de COVID-19 en Argentina.

  - Casos por Provincias
  - Distinción entre casos:
    - Infectados
    - Recuperados
    - Fallecidos

### Nuevas Features!

  - Historial de registros en el pais, desde el 3 de Marzo de 2020 hasta la fecha.
  - Casos totales

> El objetivo de mAPI es poder fomentar el 
> desarrollo de proyectos educativos y sociales
> para apoyar al estudio y el entendimiento
> de la pandemia de COVID-19 en Argentina.

### mAPI Live
[mAPI Live] se encuentra hosted para uso gratis e ilimitado.

La [Documentacion] de mAPI Live se encuentra en en Postman

### Tech

Open mAPI utiliza la menor cantidad de librerías para que sea de facil implementación. Para poder alcanzarlo, utilizamos Beautiful Soup.

* [bs4] - Beautiful Soup es una biblioteca que facilita la búsqueda de información en las páginas web. Se sitúa encima de un analizador HTML o XML, proporcionando expresiones de Python para iterar, buscar y modificar el árbol de análisis.

Y por supuesto Open mAPI es Open Source y el [repositorio publico][dill] se encuentra en GitHub.

### Installacion

Open mAPI requiere de  [Python3](https://www.python.org/).

Para installar 

```sh
$ pip3 install openmapi
```

### Ejemplos de Uso
Ejemplo 1:

```
  from openmapi.registros import Registros

  data = Registros()

  fall_ba_c = data.getCasosProvincia("BA_C", "fallecidos")

  dia_ba_c = data.getCasosProvinciaEnFecha("BA_C", "3 Jun")

  hist_ba_c = data.getHistorialCasosProvincia("BA_C")
```
Ejemplo 2

```
  from openmapi.registros import Registros

  data = Registros()

  info = 'infectados'

  casos = [[str(prov), prov.getCasos(info)] for prov in data.provincias.values()]

  mas_casos = max(casos, key=lambda x:x[1])
  print('Provincia con mas casos ' + info + " es " + mas_casos[0] + ' con ' + mas_casos[1] + ' casos.')
```

### Development

¿Te gustaria contribuir? ¡Genial!

Nos encanta recibir el apoyo de cualquiera dispuesto a ofrecerlo.
Envianos un mail a
info.creativityhub@gmail.com

### License
----

MIT


   [dill]: <https://github.com/IgnacioPardo/Open-mAPI/>
   [git-repo-url]: <https://github.com/IgnacioPardo/Open-mAPI.git>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [mAPI Live]: <https://www.mapi.live/api>
   [Documentacion]: <https://documenter.getpostman.com/view/4501185/T1DsAbwg?version=latestw>
