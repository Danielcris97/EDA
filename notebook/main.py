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

#Gráficas
utils.grafica_lineplot(poblacion_agg_filtrada,"Evolución de la Población Extranjera en España (2015–2022)","Año","Número de personas extranjeras",color='darkgreen')
utils.grafica_lineplot(delitos_totales,"Evolución de Delitos Totales en España","Año","Número de delitos",color='crimson')
utils.grafico_regresion(df_corr)
utils.grafico_comparativo_pob_crim(df_scaled)
