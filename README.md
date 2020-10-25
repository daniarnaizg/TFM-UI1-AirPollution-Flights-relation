[![GitHub license](https://img.shields.io/github/license/daniarnaizg/TFM-UI1-AirPollution-Flights-relation.svg?style=popout)](https://github.com/daniarnaizg/TFM-UI1-AirPollution-Flights-relation/blob/master/LICENSE) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)

# Estudio de la relación entre tráfico aéreo y niveles de contaminación
## TFM del Master Oficial en Análisis Inteligente de Datos Masivos (Big Data) en la Universidad Isabel I de Castilla. Curso 2019-20

Realizado por:
*  Daniel Arnaiz Gutierrez

Tutor:
*  Rubén Ruiz González


### Resumen

En los últimos años, el aumento de noticias y estudios acerca de la calidad del aire o los
efectos del cambio climático ha sido constante. Ciudades como Madrid, se han visto obligadas
incluso a limitar el transporte terrestre para así tratar de regular las emisiones de contaminantes que contribuyen a la bajada de la calidad del aire. Sin embargo, las grandes ciudades cuentan con aeropuertos por los que pasan cientos de aviones cada día y para los que no parece haber una regulación en términos de emisiones de contaminantes.

El principal objetivo de este proyecto es tratar de encontrar una posible relación entre la contaminación del aire y las rutas que siguen los vuelos de aviones comerciales en una determinada zona. Para ello, tras delimitar un área y un rango de fechas determinados, y obtener los datos tanto de la contaminación del aire, como de todos los vuelos cuyas rutas han pasado por este área, se ha realizado un estudio para determinar si existe una relación entre estos dos factores.

El proceso de extracción, transformación y carga de datos seguido para realizar este estudio ha sido completado en su totalidad bajo el entorno de Amazon Web Services haciendo uso de múltiples herramientas para la extracción, almacenamiento y procesado de la información como Amazon S3, Amazon EC2 o Amazon EMR. Así mismo, se han empleado librerías de Python para tratamiento de datos como pandas y NumPy, o de visualización de datos como folium, matplotlib o seaborn.

En cuanto a los resultados obtenidos, no se ha encontrado una clara relación directa entre la contaminación del aire y el tráfico aéreo, dados los datos y limitaciones propuestas en este estudio. Sin embargo, la consistencia de los resultados obtenidos de la correlación entre ambos conjuntos de datos sugiere la posibilidad de que, al tener en cuenta contaminantes emitidos por fuentes externas, los efectos de compuestos como óxidos de nitrógeno (NOX) o materias particuladas (PM10 y PM2.5) se vean más definidos en los datos observados sobre el tráfico aéreo.

### Abstract

In recent years, the increase in news and studies about air quality or the effects of climate change has been constant. Cities like Madrid have even been forced to limit land transport in an attempt to regulate the emissions of pollutants that contribute to the decline in air quality. However, large cities have airports through which hundreds of planes pass every day and for which there seems to be no regulation in terms of pollutant emissions.

The main objective of this project is to try to find a possible relationship between air pollution and the routes followed by commercial aircraft flights in a given area. For that purpose, after defining an area and a range of specific dates, and obtaining data both on air pollution and on all flights whose routes have passed through this area, a study has been carried out to determine whether there is a relationship between these two factors.

The process of data extraction, transformation and loading carried out this study has been completed entirely under the Amazon Web Services environment making use of multiple tools for the extraction, processing and storage of data such as Amazon S3, Amazon EC2 or Amazon EMR. As well as Python libraries for data processing such as pandas and NumPy, or data visualization such as folium, matplotlib or seaborn.

As for the results obtained, no clear direct relationship has been found between air pollution and air traffic, given the data and limitations proposed in this study. However, the consistency of the results obtained from the correlation between both sets of data suggests the possibility that, when taking into account pollutants emitted by external sources, the effects of compounds such as nitrogen oxides (NOX) or particulate matter (PM10 y PM2.5) are more defined in the data observed on air traffic.
