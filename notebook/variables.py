import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import utils
base_path = "../datos"
activos = utils.load_and_clean(f"{base_path}/activos_nacionalidad_sexo_edad.csv")
empleo = utils.load_and_clean(f"{base_path}/tasa_de_empleo_anual.csv", sep=';')
delitos = utils.load_and_clean(f"{base_path}/delitos_nacionalidad.csv")
condenados = utils.load_and_clean(f"{base_path}/condenados_sexo_nacionalidad_numero_delitos.csv")
ocupados = utils.load_and_clean(f"{base_path}/ocupados_nacionalidad_sector.csv")
poblacion = utils.load_and_clean(f"{base_path}/poblacion_pais_nacimiento.csv")
salario = utils.load_and_clean(f"{base_path}/salarios_jornada_nacionalidad_decil.csv")
delito_sexual = utils.load_and_clean(f"{base_path}/delitos_sexuales_nacionalidad.csv", sep=';')
paro = utils.load_and_clean(f"{base_path}/paro_por_nacionalidad.csv", sep=';')
paro["periodo"] = pd.to_numeric(paro["periodo"].astype(str).str.replace('*', '', regex=False), errors="coerce")
neet = utils.load_and_clean(f"{base_path}/no_estudian_ni_trabajan_por_nacionalidad.csv", sep=';')
pobreza = utils.load_and_clean(f"{base_path}/riesgo_de_pobreza_nacionalidad.csv", sep=';')

