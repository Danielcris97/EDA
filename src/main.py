import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import utils
import variables as vr
import os

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)
ruta = '../Visualizaciones'
os.makedirs(ruta, exist_ok=True)

# 1. crimen y poblacion extranjera
vr.poblacion["Español/Extranjero"] = vr.poblacion["Español/Extranjero"].str.strip().str.lower()
extranjera = vr.poblacion[vr.poblacion["Español/Extranjero"] == "nacionalidad extranjera"].copy()
extranjera["Total"] = pd.to_numeric(extranjera["Total"], errors="coerce")
poblacion_agg = (extranjera.groupby("Año")["Total"].sum().reset_index()).copy()
poblacion_agg_filtrada = poblacion_agg[poblacion_agg["Año"] >= 2015].copy()
vr.delitos["Total"] = pd.to_numeric(vr.delitos["Total"], errors="coerce")
delitos_totales = (vr.delitos.groupby("Periodo")["Total"].sum().reset_index().rename(columns={"Periodo": "Año"})).copy()
df_corr = pd.merge(poblacion_agg_filtrada.rename(columns={"Total": "PoblacionExtranjera"}),delitos_totales.rename(columns={"Total": "DelitosTotales"}),on="Año", how="inner").copy()

df_scaled = df_corr.copy()
df_scaled["PoblacionNorm"] = (df_scaled["PoblacionExtranjera"] - df_scaled["PoblacionExtranjera"].min()) / (df_scaled["PoblacionExtranjera"].max() - df_scaled["PoblacionExtranjera"].min())
df_scaled["DelitosNorm"] = (df_scaled["DelitosTotales"] - df_scaled["DelitosTotales"].min()) / (df_scaled["DelitosTotales"].max() - df_scaled["DelitosTotales"].min())
df_scaled["Año"] = df_scaled["Año"].astype(int)
correlacion = df_corr[["PoblacionExtranjera", "DelitosTotales"]].corr()
#Gráficas
utils.grafica_lineplot(poblacion_agg_filtrada,"Evolución de la Población Extranjera en España (2015–2022)","Año","Número de personas extranjeras",color='darkgreen')
utils.grafica_lineplot(delitos_totales,"Evolución de Delitos Totales en España","Año","Número de delitos",color='crimson')
utils.grafico_regresion(df_corr)
utils.grafico_comparativo_pob_crim(df_scaled)
utils.grafico_correlacion_pob_crim(correlacion)

#2 Condenados por Nacionalidad
agg = (vr.condenados.groupby("Nacionalidad")["Total"].sum().reset_index().sort_values("Total", ascending=False))
agg = agg[agg["Nacionalidad"].str.lower() != "total"]
total_general = agg["Total"].sum()
top10 = agg.sort_values("Total", ascending=False).head(10)
top10["Porcentaje"] = (top10["Total"] / total_general) * 100

utils.grafico_condenados_nacionalidad(top10,total_general)

#3 Ocupación por sector económico y Nacionalidad 
ocupados_filtrado = vr.ocupados[vr.ocupados["Sexo"] == "Ambos sexos"]
agg_ocupados = ocupados_filtrado.groupby(["Sector económico", "Nacionalidad"])["Total"].mean().reset_index()
aggf = agg_ocupados[agg_ocupados["Nacionalidad"].str.startswith("Extranjera:") & ~agg_ocupados["Sector económico"].str.lower().str.contains("total") & ~agg_ocupados["Nacionalidad"].str.contains("Total", case=False, na=False)].copy()
# Calcular porcentaje por sector (grupo vertical)
aggf["Porcentaje"] = aggf.groupby("Sector económico")["Total"].transform(lambda x: (x / x.sum()) * 100)
sectores_ocupacion = ["Agricultura", "Construcción", "Industria", "Servicios"]

utils.graficos_ocupacion_sector(sectores_ocupacion,aggf)

#4 Tasa de empleo por Nacionalidad
empleof = vr.empleo.groupby(["Nacionalidad", "Periodo"])["Total"].mean().reset_index()
comparacion = empleof[empleof["Nacionalidad"] != "Total"]
utils.grafica_empleo(comparacion)

#5 Delitos por Nacionalidad

delitos_filtrado = vr.delitos[(vr.delitos["Total"].notna()) & (vr.delitos["Total"] > 0)]
delitos_filtrado = delitos_filtrado[delitos_filtrado["Nacionalidad"].str.lower() != "total"]
top_nac = (delitos_filtrado.groupby("Nacionalidad")["Total"].sum().sort_values(ascending=False).head(5).index)
delitos_top = delitos_filtrado[delitos_filtrado["Nacionalidad"].isin(top_nac)]
del_por_año = (delitos_top.groupby(["Periodo", "Nacionalidad"])["Total"].sum().reset_index())
agg_delitos = (delitos_filtrado.groupby("Nacionalidad")["Total"].sum().reset_index().sort_values("Total", ascending=False))
agg_delitos = agg_delitos[agg_delitos["Nacionalidad"].str.lower() != "total"]
total_general = agg_delitos["Total"].sum()
top10 = agg_delitos.head(10).copy()
top10["Porcentaje"] = (top10["Total"] / total_general) * 100

utils.grafica_delitos_nacionalidad(del_por_año)
utils.grafica_delitos_nacionalidad2(top10,total_general)
#6 Salarios por tipo de jornada y Nacionalidad

salario_filtrado = vr.salario[vr.salario["Nacionalidad"].str.lower() != "total"]
agg_salario = (salario_filtrado.groupby(["Tipo de jornada", "Nacionalidad"])["Total"].mean().reset_index())
agg_salario["Porcentaje"] = agg_salario.groupby("Tipo de jornada")["Total"].transform(lambda x: (x / x.sum()) * 100)
utils.grafica_salarios(agg_salario)

#7 Delitos sexuales por nacionalidad

dsexual_filtrado = vr.delito_sexual[vr.delito_sexual["Nacionalidad"].str.lower() != "total"]
agg_dsexual = (dsexual_filtrado.groupby("Nacionalidad")["Total"].sum().reset_index().sort_values("Total", ascending=False))
agg_anual_ds = (dsexual_filtrado.groupby(["Periodo", "Nacionalidad"])["Total"].sum().reset_index())

utils.grafica_ds(agg_dsexual)
utils.grafica_ds2(agg_anual_ds)
#8 Jóvenes que no estudian ni trabajan
agg_jneet = vr.neet.groupby("Nacionalidad")["Total"].mean().reset_index()
agg_janual = vr.neet.groupby(["Periodo","Nacionalidad"])["Total"].mean().reset_index()
utils.grafica_neet2(agg_janual)
utils.grafica_neet(agg_jneet)
#9 Tasa de paro por nacionalidad
vr.paro["periodo"] = pd.to_numeric(vr.paro["periodo"], errors="coerce")
paro_anual = vr.paro.groupby(["periodo", "Nacionalidad"])["Total"].mean().reset_index().copy()
paro_filtrado = paro_anual[paro_anual["periodo"] >= 2015].copy()
paro_filtro = paro_filtrado[paro_filtrado["Nacionalidad"].str.lower() != "total"].copy()
agg_paro = paro_filtro.groupby("Nacionalidad")["Total"].mean().reset_index().copy()

utils.grafica_paro(paro_filtrado)
utils.grafica_paro2(agg_paro)

#10 Riesgo de pobreza

pobreza_filtro = vr.pobreza[vr.pobreza["Nacionalidad"].str.lower() != "total"]
agg_pobreza = pobreza_filtro.groupby("Nacionalidad")["Total"].mean().reset_index()
utils.grafica_pobreza1(agg_pobreza)
utils.grafica_pobreza2(agg_pobreza)