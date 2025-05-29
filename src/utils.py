import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def load_and_clean(path, sep=','):
    df = pd.read_csv(path, sep=sep)
    if 'Total' in df.columns:
        df['Total'] = pd.to_numeric(df['Total'].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False), errors='coerce')
        df['Total'] = df['Total'].fillna(0)
    return df

# Contador global para nombrar automáticamente las gráficas
contador_graficas_lineal = {"valor": 1}

def grafica_lineplot(data, titulo, xnombre, ynombre, color='darkgreen'):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x="Año", y="Total", marker="o", color=color)
    plt.title(titulo)
    plt.xlabel(xnombre)
    plt.ylabel(ynombre)
    plt.grid(True)
    plt.tight_layout()
    
    # Crear la carpeta si no existe
    ruta = '../Visualizaciones'
    os.makedirs(ruta, exist_ok=True)
    
    # Generar nombre automático
    numero = contador_graficas_lineal["valor"]
    nombre_archivo = f'grafica_lineplot{numero}.jpg'
    contador_graficas_lineal["valor"] += 1  # Aumenta el contador
    
    # Guardar la imagen
    plt.savefig(os.path.join(ruta, nombre_archivo))
    plt.close()

def grafico_regresion(data1):
    sns.regplot(data=data1, x="PoblacionExtranjera", y="DelitosTotales", color="teal", marker="o")
    plt.title("Correlación: Población Extranjera vs Delitos Totales (2015–2022)")
    plt.xlabel("Población Extranjera")
    plt.ylabel("Delitos Totales")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('../Visualizaciones/gráfico_regresión1.jpg')


def grafico_comparativo_pob_crim(data1):
    plt.figure(figsize=(10, 6))
    plt.plot(data1["Año"], data1["PoblacionNorm"], marker="o", label="Población Extranjera (normalizada)", color="green")
    plt.plot(data1["Año"], data1["DelitosNorm"], marker="o", label="Delitos Totales (normalizados)", color="red")
    plt.title("Población Extranjera vs Delitos (escala normalizada)")
    plt.xlabel("Año")
    plt.ylabel("Valor normalizado (0 a 1)")
    plt.ylim(0, 1)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../Visualizaciones/poblacion_vs_grafico_delitos_normalizados.jpg")
    plt.close() 
    
def grafico_correlacion_pob_crim(data):
    sns.heatmap(data, annot=True, cmap="GnBu", fmt=".2f", square=True)
    plt.title("Mapa de calor: Correlación entre Población Extranjera y Delitos")
    plt.tight_layout()
    plt.savefig("../Visualizaciones/grafico_correlacion_pob_crim.jpg")

def grafico_condenados_nacionalidad(data1,data2):
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data1, x="Total", y="Nacionalidad", color="skyblue")

    for i, (total, porcentaje) in enumerate(zip(data1["Total"], data1["Porcentaje"])):
        ax.text(total + data2 * 0.005, i, f"{porcentaje:.1f}%", va="center")

    plt.title("Total de Personas Condenadas por Nacionalidad (Top 10)")
    plt.xlabel("Número de condenados")
    plt.ylabel("Nacionalidad")
    plt.tight_layout()
    plt.savefig("../Visualizaciones/grafico_condendos_nacionalidad.jpg")

def graficos_ocupacion_sector(sector,aggf):
    for i, sector in enumerate(sector, start=1):
        data_sector = aggf[aggf["Sector económico"] == sector].copy()
        data_sector["Nacionalidad Simple"] = data_sector["Nacionalidad"].str.replace("Extranjera: ", "", regex=False)

        plt.figure(figsize=(10, 6))
        ax = sns.barplot(
            data=data_sector,
            x="Nacionalidad Simple",
            y="Total",
            hue="Nacionalidad Simple",
            palette="tab10",
            legend=False
        )

        for bar, porcentaje in zip(ax.patches, data_sector["Porcentaje"]):
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + data_sector["Total"].max() * 0.01,
                f"{porcentaje:.1f}%",
                ha="center",
                va="bottom",
                fontsize=8
            )
        plt.title(f"Ocupación en el sector {sector} por Nacionalidad Extranjera")
        plt.xlabel("Nacionalidad")
        plt.ylabel("Número medio de ocupados")
        plt.tight_layout()

        # Guardar con nombre automático
        plt.savefig(f"../Visualizaciones/grafica_ocupacion{i}.jpg")
        plt.close()  # Cerrar para evitar solapamiento

def grafica_empleo(data):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x="Periodo", y="Total", hue="Nacionalidad", marker="o", palette="Set2")

    plt.title("Tasa de Empleo por Nacionalidad (2015–2024)")
    plt.xlabel("Año")
    plt.ylabel("Tasa de empleo (%)")
    plt.xticks(data["Periodo"].unique(), rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../Visualizaciones/grafico_tasa_empleo.jpg")
def grafica_delitos_nacionalidad(data):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x="Periodo", y="Total",palette="tab10", hue="Nacionalidad", marker="o")
    plt.title("Evolución de Delitos Totales por Nacionalidad (Top 5, sin Total)")
    plt.xlabel("Año")
    plt.ylabel("Número total de delitos")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../Visualizaciones/grafico_delitos_nacionalidad.jpg")
def grafica_delitos_nacionalidad2(data,data2):
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x="Total", y="Nacionalidad", color="skyblue")
    for i, (total, porcentaje) in enumerate(zip(data["Total"], data["Porcentaje"])):
        ax.text(total + data2 * 0.005, i, f"{porcentaje:.1f}%", va="center", fontsize=9)

    plt.title("Porcentaje de delitos cometidos por nacionalidad")
    plt.xlabel("Número total de delitos")
    plt.ylabel("Nacionalidad")
    plt.tight_layout()
    plt.savefig("../Visualizaciones/grafico_delitos_nacionalidad2.jpg")

def grafica_salarios(data1,):
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=data1,
        x="Tipo de jornada",
        y="Total",
        hue="Nacionalidad",
        palette="tab10"
    )

    # 5. Añadir porcentaje como etiqueta sobre cada barra
    for container in ax.containers:
        for bar in container:
            height = bar.get_height()
            x = bar.get_x() + bar.get_width() / 2
            jornada = ax.get_xticks()[int(x)]
            ax.text(
                x,
                height + 20,  # ajusta si las cifras son pequeñas o grandes
                f"{height:.0f}€",
                ha="center",
                va="bottom",
                fontsize=8,
                rotation=0
            )

    plt.title("Salario Medio por Tipo de Jornada y Nacionalidad (con etiquetas)")
    plt.ylabel("Salario medio (€)")
    plt.xlabel("Tipo de jornada")
    plt.tight_layout()
    plt.savefig("../Visualizaciones/grafica_salarios.jpg")
def grafica_ds(data1):
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data1, x="Nacionalidad", y="Total", palette="tab10", hue="Nacionalidad", dodge=False)
    for bar in ax.patches:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + max(data1["Total"]) * 0.01,
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    # 4. Ajustes finales
    plt.title("Delitos Sexuales por Nacionalidad")
    plt.ylabel("Total de delitos sexuales")
    plt.xlabel("Nacionalidad")
    plt.legend([],[], frameon=False)  # Oculta leyenda duplicada
    plt.tight_layout()
    plt.savefig("../Visualizaciones/grafica_ds1.jpg")
def grafica_ds2(data):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x="Periodo", y="Total", hue="Nacionalidad", marker="o")
    plt.title("Evolución de Delitos Sexuales = Extranjeros vs. Españoles")
    plt.xlabel("Año")
    plt.ylabel("Número total de delitos sexuales")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../Visualizaciones/grafica_ds2.jpg")
def grafica_neet(data):
    plt.figure(figsize=(10, 6))
    plt.pie(data["Total"], labels=data["Nacionalidad"], autopct='%1.1f%%')
    plt.title("Jóvenes nini por Nacionalidad")
    plt.savefig("../Visualizaciones/grafica_neet.jpg")
def grafica_neet2(data):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x="Periodo", y="Total", hue="Nacionalidad", marker="o")
    plt.title("Jóvenes NEET por Nacionalidad")
    plt.savefig("../Visualizaciones/grafica_neet2.jpg")
def grafica_paro(data):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x="periodo", y="Total", hue="Nacionalidad", marker="o")
    plt.title("Paro anual por Nacionalidad (desde 2015)")
    plt.xlabel("Año")
    plt.ylabel("Tasa de paro (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../Visualizaciones/grafica_paro.jpg")
def grafica_paro2(data):
    plt.figure(figsize=(10, 6))
    plt.pie(data["Total"], labels=data["Nacionalidad"], autopct='%1.1f%%')
    plt.title("Paro por Nacionalidad")
    plt.savefig("../Visualizaciones/grafica_paro2.jpg")
def grafica_pobreza1(data1):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data1, x="Total", y="Nacionalidad",color='skyblue')
    plt.title("Riesgo de Pobreza por Nacionalidad")
    plt.savefig("../Visualizaciones/grafica_pobreza1.jpg")
def grafica_pobreza2(data1):
    plt.figure(figsize=(10, 6))
    plt.pie(data1["Total"], labels=data1["Nacionalidad"], autopct='%1.1f%%')
    plt.title("Riesgo de pobreza por nacionalidad")
    plt.savefig("../Visualizaciones/grafica_pobreza2.jpg")