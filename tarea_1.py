# -*- coding: utf-8 -*-
"""Tarea_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aUDoYem4g6xj1WfyEhSKFGPmRHHdlXSC

EAE3709 APLICACIONES DE  MACHINE LEARNING EN ECONOMÍA <br>
1ER SEMESTRE 2025 <br>
INSTITUTO DE ECONOMÍA <br>
PONTIFICIA UNIVERSIDAD CATÓLICA DE CHILE


# **TAREA 1**


---


Profesor:
- Joaquín Pérez Lapillo

Ayudantes:

- Luis García B.
- Sebastián Hernández B.
- Oscar Herrera G.

**Complete sus datos:**

- Nombre y apellido:
  - `# Completar`
  - `# Completar`
- Usuario de GitHub (opcional):  `# Completar`

## Instrucciones

- Descargue el notebook y cárguelo en su Drive.
- Todas las preguntas deben ser contestadas en su notebook.
- Para que una pregunta esté correcta el código debe correr.
- Si es necesario, realice comentarios breves en su código explicando lo que está realizando o sus resultados.
- Una vez culminada su tarea, suba su notebook al buzón de tareas de Canvas.
- La fecha y hora límite de esta tarea es el _**viernes 4 de abril a las 18:00 hrs**_.

### Distribución de puntaje


| Pregunta                        | Puntaje |
|--------------------------------|---------|
| Pregunta 1.0                   |    1    |
| Pregunta 1.1                   |    3    |
| Pregunta 1.2                   |    3    |
| Pregunta 1.3                   |    2    |
| Pregunta 1.4                   |    2    |
| Pregunta 1.5                   |    5    |
| Pregunta 1.6                   |    2    |
| Pregunta 1.7                   |    5    |
| Pregunta 1.8                   |   7    |
| Pregunta 1.9                   |   5    |
| Pregunta 1.10                  |   5    |
| Pregunta 1.11                  |   6    |
| Pregunta 1.12                  |    2    |
| Pregunta 1.13                  |    5    |
| Pregunta 1.14                  |   10    |
| Pregunta 1.15                  |    5    |
| Pregunta 1.16                  |    5    |
| Pregunta 2.0                   |    2    |
| Pregunta 2.1                   |    5    |
| Pregunta 2.2                   |    5    |
| Pregunta 2.3                   |    5    |
| Pregunta 2.4                   |    3    |
| Pregunta 2.5                   |    3    |
| Pregunta 2.6                   |    2    |
| Pregunta 2.7                   |    2    |

Total: 100 pts.

### Sobre el Bonus

- La entrega, por defecto, es a través de Canvas. Sin embargo, puede escoger voluntariamente entregar la tarea en su GitHub personal.

- Si usted realiza la entrega en GitHub antes de la **fecha y hora indicada**, entonces tendrá una bonificación de 0.3 en su nota final de tarea. Es decir, si usted obtuvo una nota de 6.5, pero entregó en su GitHub, entonces su calificación en esta tarea será de 6.8.

- Si **además** de realizar la entrega a través de GitHub, usted logra crear `branches` (ramas) y realizar un `merge` entre ramas, entonces se le bonificará con 0.5 en su nota de tarea. Es decir, si usted obtuvo una nota de 6.5, pero entregó en su GitHub e hizo el trabajo de ramas, entonces su calificación en esta tarea será de 7.0.

  - Se valora capacidad autodidacta.
  - Sólo serán considerados los archivos contenidos en su rama principal a la fecha y hora indicada.

## Exploratory data analysis (EDA)

Para esta tarea se utilizará como principal fuente de información un dataset con una serie de características económicas, demográficas y de desarrollo humano de distintos países a la fecha de 2007 (corte transversal). El dataset está disponible en el siguiente [Github](https://raw.githubusercontent.com/lfgarcia-1/EAE3709-1-2025/refs/heads/main/economic_dataset.csv).<br>

Descripción del dataset:

Variables:

*   date: Fecha en la que se actualizó la data.
*   Population, Area (sq. mi.) Pop. Density (per sq. mi.), Coastline (coast/area ratio), Net migration, Infant mortality (per 1000 births), GDP ($ per capita, Literacy (%), Phones (per 1000), Arable (%), Crops (%), Other (%), Climate, Birthrate, Deathrate, Agriculture, Industry, Service: Características del país.
*   source: fuente de los datos.
*   Region: Región (grupo de países).
*   Country: País.

### Pregunta 1.0

Importe las librerías que usará en su tarea.
"""

# Librerías manejo de datos
import pandas as pd
import numpy as np
# Librerías para graficar
import matplotlib.pyplot as plt
import seaborn as sns

# Librería que filtra warnings innecesarios
import warnings
warnings.filterwarnings("ignore")

"""### Pregunta 1.1

Importe el dataset como un DataFrame (df) directamente desde Github (es decir, no descargue el archivo manualmente). A lo largo de la tarea este df se denominará como `df`.

"""

url = 'https://raw.githubusercontent.com/lfgarcia-1/EAE3709-1-2025/refs/heads/main/economic_dataset.csv'

#Se leen los datos
df = pd.read_csv(url)

"""### Pregunta 1.2

Utilice las funciones de Pandas `head()`, `tail()`, `info()` y la propiedad (o atributo) `.dtypes` para describir el `df`. Explique brevemente para qué sirve cada función.
"""

df.head() #Visualización de los primeras 5 filas

df.tail() #Visualización de los ultimas 5 filas

df.info() #Información de los "tipos" de datos de la tabla, mas detallado que dtypes

df.dtypes #muestra el tipo de dato de cada columna en un DataFrame.

"""### Pregunta 1.3

La variable `source` es innecesaria debido que contiene el mismo valor para todas las observaciones. Elimine esta variable de su `df`.
"""

#Borramos
df = df.drop(columns=['source'])

df.head()

"""### Pregunta 1.4

Transforme el tipo de la variable `date` a `datetime` _datatype_.
"""

df["date"] = pd.to_datetime(df["date"])

df.info()

"""### Pregunta 1.5

Para determinar si las variables son "útiles" y sus valores son "correctos" es necesario comprender cada uno de los atributos del dataset.
Investigue y explique brevemente la relación **teórica** entre el `GDP (% per capita)` y cada una de las variables denominadas como "Características del país" en la introducción.

Ejemplo: Existe una variable denominada `Coastline (coast/area ratio)`. Coastline es una medida de la cantidad de costa (acceso a mar) del país normalizada al área total del país para no beneficiar a países más grandes pero con la misma proporción de costa. A mayor "Costline" aumenta la capacidad portuaria per capita del país, más puertos facilita el comercio y podría aumentar el GDP per cápita.

---
**Pop:** Una mayor población puede significar más mano de obra, pero sin educación o empleo adecuado, su impacto en el PIB per cápita puede ser negativo.


**Density (per sq. mi.):** Puede generar economías de aglomeración y mayor productividad.


**Net migration:** Un saldo migratorio positivo indica que el país es atractivo económicamente, lo que suele estar correlacionado con un PIB per cápita alto.


**Infant mortality (per 1000 births)**: Altos valores reflejan problemas en salud pública y desarrollo, lo que frena el crecimiento del pib per capita.


**Literacy (%):** Un mayor nivel de alfabetización implica un capital humano más calificado, lo que incrementa la productividad y el PIB per cápita.


**Area (sq. mi.)**: Un país grande puede tener más recursos naturales, pero el tamaño por sí solo no garantiza un PIB per cápita alto sin una explotación eficiente.


**Arable (%):** Puede impulsar la economía agrícola, pero una alta dependencia de la agricultura de baja productividad limita el crecimiento.


**Crops (%):** Similar a Arable %, una economía demasiado centrada en la agricultura puede presentar menor PIB per cápita.


**Climate:** Factores climáticos pueden afectar la productividad agrícola y la calidad de vida.


**Industry, Service**: Países con un alto PIB per cápita dependen más de estos sectores, ya que generan mayor valor agregado que la agricultura.


**Agriculture:** Una alta participación de la agricultura en la economía suele estar asociada con menor desarrollo y menor PIB per cápita.


**Phones (per 1000)**: Mayor acceso a telecomunicaciones refleja mejor desarrollo tecnológico y económico.


**Coastline (coast/area ratio)**:  A mayor "Costline" aumenta la capacidad portuaria per capita del país, más puertos facilita el comercio y podría aumentar el GDP per cápita.


***Deathrate***: Altos valores suelen estar relacionados con menor desarrollo económico, reflejando problemas de salud.


**Birthrate**: Altos niveles son necesarios para generar mayor capital humano futuro, lo que impulsa el crecimiento del pais. Aunque no necesariamente aumenta el GDP per capita. Si la poblacion crece al mismo nivel que el capital, el Pib per capita no tendra cambios.

---

### Pregunta 1.6

Calcule estadísticas descriptivas para cada variable numérica.
"""

df.describe()

"""### Pregunta 1.7

Según corresponda, realice un gráfico de distribución de densidad o histograma para describir 3 variables del `df` que usted crea más relevantes.

¿Por qué es importante analizar las distribuciones de las variables a utilizar en su modelo? Ejemplifique su respuesta con al menos una de las variables del df`.
"""

# Distribución de densidad de la variable objetivo
sns.distplot(df['GDP ($ per capita)'])

# Aplicar transformación logarítmica a Population
df['LnPopulation'] = np.log(df['Population'])

# Variables relevantes
variables = ["LnPopulation", "Birthrate", "Literacy (%)"]

# Crear gráficos de distribución
plt.figure(figsize=(25, 8))
for i, var in enumerate(variables):
    plt.subplot(1, 3, i + 1)
    sns.histplot(df[var], kde=True, bins=30)
    plt.title(f'Distribución de {var}')
plt.tight_layout()
plt.show()

"""---

Analizar las distribuciones permite identificar sesgos, valores atípicos y patrones en los datos. Por ejemplo, si la variable Population está fuertemente sesgada a la derecha (distribución altamente asimétrica), el modelo puede verse afectado por la presencia de países con poblaciones extremadamente altas, o bajas como es el caso,  lo que requiere una transformación logarítmica para mejorar la representación de los datos.

---

### Pregunta 1.8

El df contiene variables con missing values (`NaN`). Impute los `NaN` con el método que estime conveniente, justificando su decisión.

¿Es pertinente eliminar alguna de estas variables? Hágalo si es el caso.
"""

df.isnull().sum()

df.isnull().sum().sort_values(ascending=False)  # Se ordena de manera descendente

# Guardamos un Ranking de missings
total_missings = df.isnull().sum().sort_values(ascending=False)  # Total missings por columna ordenados del mayor al menor
total_missings

# Cantidad de filas totales de todas las columnas se guarda en la variable total_datos
total_datos = df.isnull().count()
total_datos

# Porcentaje de missings con respecto al total
percent_missings = (total_missings/total_datos).sort_values(ascending=False)*100
percent_missings  # Observamos

# Unimos tablas de Nro. de *missings* y su *porcentaje* respectivo
# a través de la columnas (axis = 1), y las nombramos "Total" y "Percent"
missing_data = pd.concat([total_missings, percent_missings], axis=1, keys=['Total', 'Percent'])
missing_data

"""---


*Escriba* su respuesta y **justificación** en esta celda...


---

### Pregunta 1.9

¿Cómo distribuye el `GDP ($ per capita)` en diferentes **regiones**? Defina una forma ilustrativa de gráficar el `GDP ($ per capita)` para todas las regiones en un mismo gráfico. Interprételo.
"""

# Creamos el boxplot de GDP per capita por región
plt.figure(figsize=(30,15))
sns.boxplot(data=df, x='Region', y='GDP ($ per capita)', palette='Set2')

# Agregamos título y etiquetas
plt.title('Distribución del GDP per capita por Región', fontsize=20)
plt.xlabel('Región', fontsize=20)
plt.ylabel('GDP per capita ($)', fontsize=20)
plt.xticks(rotation=90)  # Rotamos las etiquetas de las regiones para mejor visibilidad

# Mostrar el gráfico
plt.tight_layout()
plt.show()

"""---


*Escriba* su interpretación en esta celda...


---

### Pregunta 1.10

Supongamos que `GDP ($ per capita)` es su variable objetivo. Estudie la correlación de esta variable con el resto de las variables del `df`. ¿Por qué es importante analizar la correlación entre las variables?
"""

df[df.dtypes[df.dtypes != "object"].index].corr()["GDP ($ per capita)"]

corr = df[df.dtypes[df.dtypes != "object"].index].corr()  # Matriz de correlación en variables numéricas
corr_abs = corr.abs()  # Valor abosluto a todos los elementos de la tabla

GDP_sorted_corr = corr_abs["GDP ($ per capita)"].sort_values(ascending=False) #ordenamos de mayor a menor

corr

GDP_sorted_corr

"""---


*Escriba* su respuesta en esta celda...


---

### Pregunta 1.11

Realice tres _scatterplots_ (uno por variable) de las tres variables con la mayor correlación con la variable objetivo.

Utilizando los parámetros de la función con la que hizo los _scatterplots_, coloque un título a cada gráfico y agregue colores a los _data points_ del _scatterplot_- Use colores diferentes por cada gráfico.
"""

# Graficaremos scatterplots
var = ['Phones (per 1000)', 'Birthrate', 'Infant mortality (per 1000 births)']

for variable in var:
  df.plot.scatter(x=variable, y="GDP ($ per capita)")

"""### Pregunta 1.12

Cree una nueva columna `GDP (%)` que represente el GDP total de cada pais (no per capita) y agreguela al dataframe.
"""

df['GDP (%)'] = df['GDP ($ per capita)'] * df['Population']

df.head()

"""### Pregunta 1.13

Repita el análisis de correlaciones para `GDP ($)` excluyendo `GDP ($ per capita)` del análisis. ¿Cambian las variables que más correlacionan? Justifique.
"""

# Excluir 'GDP ($ per capita)' de las variables numéricas
df_corr = df.drop(columns=['GDP ($ per capita)', 'date', 'Country', 'Region'])  # Excluimos otras no numéricas

# Calcular la correlación entre 'GDP (%)' y las demás variables numéricas
corr_gdp_total = df_corr.corr()['GDP ($)'].sort_values(ascending=False)

# Mostrar el resultado
print(corr_gdp_total)

"""[texto del enlace](https://)


---
La correlación entre GDP total (GDP (%)) y Population (0.639) se debe a que países con más habitantes tienden a generar un PIB más alto, ya que hay más personas contribuyendo a la economía. De manera similar, la correlación con Area (sq. mi.) (0.556) refleja que los países más grandes en territorio tienen más recursos y sectores económicos, lo que también impulsa su PIB. En cambio, variables como Infant mortality y Deathrate muestran correlaciones negativas con el PIB, ya que países con mejores condiciones de salud y menores tasas de mortalidad suelen tener un nivel de vida más alto y una mayor productividad económica. Excluyendo el PIB per cápita, las variables demográficas y geográficas, como la población y el área, se presentan como factores más relevantes para el PIB total.

---

### Pregunta 1.14

Detecte las observaciones outliers de las tres variables seleccionadas en la pregunta anterior. Además, impute estas observaciones si usted lo considera necesario. Justifique su decisión.
"""



"""---


*Escriba* su **justificación** en esta celda...


---

### Pregunta 1.15

En los ejemplos anteriores calculamos correlaciones para `GDP ($ per capita)` y `GDP ($)`. Genere un nuevo dataframe que tenga le variación porcentual de la correlación absoluta para cada una de las columnas de características, e.g., si la correlación en valor absoluto de `GDP ($ per capita)` vs `Industry` es 0.1 y la correlación `GDP ($)` vs `Industry` es 0.5, la variación deberá ser +500%. Dicha variación porcentual puede ser positiva o negativa, pero ordene los el dataframe de tal manera que la variación de correlación absoluta sea desendiente.
"""



"""### Pregunta 1.16

Del resultado anterior, ¿qué caracerística del país tuvo una mayor diferencia absoluta el medir su correlación versus `GDP ($)` en vez de `GDP ($ per capita)`'. Interprete.

---


*Escriba* su respuesta e interpretación en esta celda...

---

## EDA con diferentes fuentes de **información**

Una situación habitual en _Data Science: es el manejo de información de múltiples fuentes para un mismo propósito. En este sentido, de ahora en adelante agregaremos un dataframe adicional a nuestro set de información, disponible en [Github](https://raw.githubusercontent.com/datasets/gini-index/refs/heads/main/data/gini-index.csv). Lo llamaremos `df_gini`.

Este dataset contiene información histórica del Índice de Gini (economía), el cual captura la desigualdad económica entre los quintiles de cada país. A mayor índice Gini, más desigual es un país en términos de ingresos. Para mayor información sobre los datos, puede dirigirse al [Repositorio](https://github.com/datasets/gini-index) completo. Para conocer más sobre el índice, una navegación por [Wikipedia](https://en.wikipedia.org/wiki/Gini_coefficient) debería ser suficiente.

### Pregunta 2.0

Cargue la base datos, asegúrese de que la variable de año esté en un formato de "fecha", y usando el diccionario de mapeo por inconsistencias de nombres, `country_name_mapping`, encuentre la forma de realizar un INNER JOIN entre ambas tablas, usando el nombre del país y el año de la observación como variables por las cuales hacer el JOIN. En el diccionario `country_name_mapping`, _keys_ corresponden a los valores de la tabla `df_gini` y _values_ a los de `df`.

Llame al dataframe resultante `df_merged`.

Si usted no se ha percatado, los nombres en la columna `Country` de `df` poseen espacios al final de estos. Elimine los espacios antes de realizar el INNER JOIN de interés (Hint: existe una función propia de las variables tipo `string` que realiza la labor de eliminar espacios al final de la palabra).
"""

# NO MODIFICAR, pero sí ejecutar
country_name_mapping = {
    "Bahamas": "Bahamas, The",
    "Bosnia and Herzegovina": "Bosnia & Herzegovina",
    "Myanmar": "Burma",
    "Cape Verde": "Cabo Verde",
    "Central African Republic": "Central African Rep.",
    "Congo, Rep.": "Congo, Repub. of the",
    "Czechia": "Czech Republic",
    "Timor-Leste": "East Timor",
    "Egypt, Arab Rep.": "Egypt",
    "West Bank and Gaza": "Gaza Strip",
    "Iran, Islamic Rep.": "Iran",
    "Korea, Dem. People's Rep.": "Korea, North",
    "Korea, Rep.": "Korea, South",
    "Kyrgyz Republic": "Kyrgyzstan",
    "Lao PDR": "Laos",
    "North Macedonia": "Macedonia",
    "Micronesia, Fed. Sts.": "Micronesia, Fed. St.",
    "Russian Federation": "Russia",
    "St. Kitts and Nevis": "Saint Kitts & Nevis",
    "St. Lucia": "Saint Lucia",
    "St. Vincent and the Grenadines": "Saint Vincent and the Grenadines",
    "Slovak Republic": "Slovakia",
    "Eswatini": "Swaziland",
    "Syrian Arab Republic": "Syria",
    "Trinidad and Tobago": "Trinidad & Tobago",
    "Turkiye": "Turkey",
    "Venezuela, RB": "Venezuela",
    "Viet Nam": "Vietnam",
    "Yemen, Rep.": "Yemen"
}







"""### Pregunta 2.1

Repita el ejercicio de la obtención de un ranking para las correlaciones absolutas, tal como lo hizo para el GDP per cápita. ¿Cuáles son las relaciones que más le sorprenden? ¿Cuáles son las que están en línea con lo que esperaba? Justifique para ambos casos.




"""



"""---


*Escriba* su respuesta y justificación en esta celda...

---

Finalmente, agregaremos una tercera base de datos al análisis, también disponible en [Github](https://raw.githubusercontent.com/datasets/co2-fossil-by-nation/refs/heads/main/data/fossil-fuel-co2-emissions-by-nation.csv) con su repectivo
[Repositorio](https://github.com/datasets/co2-fossil-by-nation). Esta contiene emisiones de dióxido de carbono (CO2) total y por fuentes, desagregado por país. La base de datos contiene datos desde el siglo XVI y la frecuencia es anual.

### Pregunta 2.2

Cargue la base de datos llamándola `df_co2`. Asegúrese de que todas las variables estén en su correcto formato (años deben estar en un formato de fecha). ¿Qué cuidados identifica usted que debiésemos tener al momento de observar valores nulos en esta base de datos?

Adicionalmente, para cada palabra en la columna `Country`, asegúrese de que la primera letra siempre sea mayúscula y que el resto de letras sean minúsculas (Hint: revise `methods` propios de las variables tipo `string`).

Luego, reemplace valores en `df_co2["Country"]` según el mapping otorgado. En el diccionario `country_name_mapping_co2`, _keys_ corresponden a los valores de la tabla `df_co2` y _values_ a los de `df`.
"""

# NO MODIFICAR, pero sí ejecutar
country_name_mapping_co2 = {
    "United States Of America": "United States",
    "France (Including Monaco)": "France",
    "Italy (Including San Marino)": "Italy",
    "Plurinational State Of Bolivia": "Bolivia",
    "Federal Republic Of Germany": "Germany",
    "Former German Democratic Republic": "Germany",
    "Republic Of Moldova": "Moldova",
    "United Republic Of Tanzania": "Tanzania",
    "Japan (Excluding The Ruyuku Islands)": "Japan",
    "Hong Kong Special Adminstrative Region Of China": "Hong Kong",
    "Peninsular Malaysia": "Malaysia",
    "Democratic Republic Of The Congo (Formerly Zaire)": "Congo, Dem. Rep.",
    "Brunei (Darussalam)": "Brunei",
    "Myanmar (Formerly Burma)": "Burma",
    "Syrian Arab Republic": "Syria",
    "Islamic Republic Of Iran": "Iran",
    "Republic Of Korea": "Korea, South",
    "Democratic People S Republic Of Korea": "Korea, North",
    "Russian Federation": "Russia",
    "Viet Nam": "Vietnam",
    "Yemen": "Yemen, Rep.",
    "Trinidad And Tobago": "Trinidad & Tobago",
    "Bahamas": "Bahamas, The",
    "Micronesia": "Micronesia, Fed. St.",
    "Slovakia": "Slovakia",
    "St. Vincent & The Grenadines": "Saint Vincent and the Grenadines",
    "Saint Lucia": "Saint Lucia",
    "Antigua & Barbuda": "Antigua & Barbuda",
    "Saint Kitts-Nevis-Anguilla": "Saint Kitts & Nevis",
    "Netherland Antilles And Aruba": "Netherlands Antilles",
    "Timor-Leste (Formerly East Timor)": "East Timor",
    "Macau Special Adminstrative Region Of China": "Macau",
    "Republic Of Cameroon": "Cameroon",
    "Republic Of Sudan": "Sudan",
    "Lao People S Democratic Republic": "Laos",
    "Libyan Arab Jamahiriyah": "Libya",
    "Cote D Ivoire": "Cote d'Ivoire",
    "British Virgin Islands": "British Virgin Is.",
    "Faeroe Islands": "Faroe Islands",
    "China (Mainland)": "China",
}



"""---


*Escriba* su respuesta y justificación en esta celda...

---

### Pregunta 2.3

En un mismo gráfico, grafique las series de emisiones totales de CO2 para los siguientes países:

- Reino Unido
- Canadá
- Alemania
- Francia
- Estados Unidos
- Brasil
- China
- Japón
- India


Para cada serie, añada una leyenda con el nombre del país.
"""



"""### Pregunta 2.4

Para el año 2007, por cada país realice un ranking de las fuentes con más emisiones de CO2 excluyendo las variables `Per Capita` y `Bunker fuels (Not in Total)`. Es decir, asigne un número de 1 a 5 a $\{$ `Solid Fuel`, `Liquid Fuel`, `Gas Fuel`, `Cement`, `Gas Flaring` $\}$, donde 1 es la mayor fuente de emisión de ese país en aquel año, y 5 indica que fue la menor; así para todos los países.

Si en 2007 no se reporta una fuente de emisión para un país, por ejemplo, si emisiones de `Gas Flaring` no se reportara, entonces asigne números de 1 a 4 a las fuentes restantes. Análogo para un menor número de datos.

Luego, por cada variable grafique un histograma de frecuencias del ranking que obtuvo la fuente emisión a lo largo de todos los países.

¿Cuál fue la fuente más contaminante en la mayoría de países en 2007?

"""





"""---


*Escriba* su respuesta y justificación en esta celda...

---

### Pregunta 2.5

Para cada serie de total de emisiones por país, calcule el cambio porcentual a través del tiempo. Realice imputación de missings si considera necesario, justificando su imputación. Si no lo considera necesario, también justifique (se evaluará un buen criterio fundamentado).

Repita el ejercicio del gráfico de series de tiempo anterior, pero graficando los **cambios porcentuales** para años mayores o iguales a 1995. ¿Cómo interpretaría económicamente el shock sobre las emisiones de CO2 tanto en la crisis subprime como en la crisis del Covid-19?
"""





"""---


*Escriba* su justificación e interpretación en esta celda...



---

### Pregunta 2.6

Calcule el promedio a lo largo de toda la muestra ($\mathbb{E}[\cdot]$) para el cambio porcentual de cada país y genere una nueva serie con la resta entre el cambio porcentual del país $i$ en el año $t$, y el promedio del cambio porcentual del país $i$. En otras palabras, genere una serie con _**desvíos del cambio porcentual promedio**_ $\forall i,t$:

$$Nueva Serie_i = \Delta \% TotalCO2_{i,t} - \mathbb{E}[{\Delta \% TotalCO2_{i,t}}]$$

Luego, para los siguientes países:

- Reino Unido
- Canadá
- Alemania
- Francia
- Estados Unidos
- Japón
- Italia
- España


grafique en un panel _1x2_ la desviación del cambio porcentual respecto al promedio entre 2007 y 2010 en lado izquierdo, y entre 2017 y 2020 en el lado derecho (Hint: Hay comandos que facilitan esta labor. Puede intentar con `fig, axes = plt.subplots(1, 2, figsize=(18, 6), sharey=True)`, por ejemplo).

¿Existe algún país en particular que mostró mayores desviaciones atípicas de emisión de CO2 durante el periodo de la crisis sub-prime? ¿Cómo es el comportamiento de las desviaciones atípicas de CO2 de este país durante la crisis del Covid-19?
"""



"""---


*Escriba* su respuesta en esta celda...



---

### Pregunta 2.7

Genere un nuevo dataframe llamado `df_final`. Para esto, realice un INNER JOIN entre el dataframe `df_co2` y `df_merged` por "año y país" (debería terminar sólo con valores de 2007 si usted realiza un INNER JOIN).

Finalmente, grafique un mapa de calor de correlaciones (_heatmapt_) entre las variables numéricas ,excluyendo fechas.

¿Qué variables económicas, demográficas y de desarrollo humano muestran relación más importante con las emisiones de CO2? Interprete estas relaciones.
"""



"""---


*Escriba* su respuesta e interpretación en esta celda...



---

"""