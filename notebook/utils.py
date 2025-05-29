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
    plt.savefig("../Visualizaciones/poblacion_vs_delitos_normalizados.jpg")
    plt.close() 