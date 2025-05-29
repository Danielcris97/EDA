### ¿Es el crecimiento de la tasa de criminalidad en España por causa de los inmigrantes?: Un Análisis Exploratorio de Datos (EDA) 
🧠 Hipótesis
El aumento de la tasa de criminalidad en España no está causado por los inmigrantes, sino que sugiere una asociación más compleja relacionada con factores sociales y económicos.

❓Preguntas de investigación
Este proyecto busca responder con datos a una narrativa muy presente en el debate público y mediático:

¿Han aumentado los crímenes en España en los últimos años?

¿Cuál es la nacionalidad de los condenados por delitos?

¿Por qué se culpa a los inmigrantes de los delitos?

¿En qué sectores trabajan los inmigrantes?

¿Son los migrantes un peso o un aporte a la economía?


🗂️ Dataset
He utilizado y limpiado datos públicos de organismos oficiales como el INE (Instituto Nacional de Estadística) y el Ministerio del Interior, con variables desde 2015 hasta 2023.
Las categorías analizadas incluyen:

Criminalidad por nacionalidad y tipo de delito

Ocupación por sector y nacionalidad

Tasa de empleo, paro, NEET y pobreza

Salarios por tipo de jornada

Población por origen (españoles vs extranjeros)

📊 Visualizaciones generadas
El proyecto genera automáticamente más de 15 gráficas desde main.py, entre ellas:

📈 Evolución de delitos totales por año

📉 Comparación entre delitos y crecimiento de población extranjera

🔍 Regresión y correlación entre delitos, empleo, paro y pobreza

🧩 Heatmaps de variables absolutas y tasas relativas

👮‍♂️ Top 10 nacionalidades con más delitos y delitos sexuales

🧑‍🌾 Ocupación por sector: ¿a qué se dedican los inmigrantes?

💼 Comparación de salario medio por tipo de jornada y nacionalidad

📉 Tasa de paro por nacionalidad desde 2015

🔥 Jóvenes que no estudian ni trabajan (NEET)

⚖️ Porcentaje de personas condenadas por nacionalidad

🧠 Principales hallazgos
La criminalidad total ha aumentado ligeramente, pero también lo ha hecho la población y el empleo. Ambas variables evolucionan juntas.

Los inmigrantes no representan la mayoría de los delitos, y la mayoría de los condenados siguen siendo ciudadanos españoles.

Sectores como la agricultura, la construcción y los servicios dependen en gran parte de inmigrantes.

El empleo y los salarios han mejorado para muchos colectivos migrantes, aunque sigue habiendo desigualdad.

El heatmap de correlaciones con tasas relativas muestra que la pobreza y el desempleo están más relacionados con los delitos que la migración en sí.

🛡️ Contexto y reflexión
España ha sido históricamente un país receptor de migración, especialmente en la última década. En un contexto de inseguridad percibida, auge del discurso político antiinmigrante y medios sensacionalistas, este análisis busca aportar un enfoque basado en evidencia y datos reales.

La narrativa de que los inmigrantes son responsables del aumento de la criminalidad no se sostiene estadísticamente. El verdadero foco debería estar en la inclusión social, la calidad del empleo y la lucha contra la pobreza, no en el origen de las personas.

🧪 Metodología
Proyecto realizado en Python con pandas, seaborn y matplotlib

Limpieza exhaustiva de valores nulos, errores de codificación y formatos

Visualizaciones exportadas automáticamente a /visualizaciones/

Modularización del código: main.py, utils.py, variables.py

🧩 ¿Cómo explorar?
Clona el repo o descomprime el ZIP

Ejecuta main.py y se generarán todas las gráficas

Analiza los resultados en /visualizaciones/

(Opcional) Modifica los filtros para explorar otras variables

📬 ¿Te interesa el tema?
Estoy abierto a feedback, mejoras y colaboraciones.
Este análisis es un punto de partida para un debate más informado sobre inmigración, seguridad y políticas públicas.

✍️ ¿Qué opinas de los resultados? ¿Has visto discursos similares en medios o política?