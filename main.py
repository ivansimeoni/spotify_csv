# Importamos las librerías necesarias para análisis y visualización de datos
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from openpyxl.drawing.image import Image as Img
from openpyxl import load_workbook

def limpieza_datos(df):
    
    # Eliminamos las filas donde el año es menor o igual a 0 (datos inválidos)
    df = df[df["year"]>0]
    
    # Eliminamos las filas donde la duración es menor o igual a 0 (datos inválidos)
    df = df[df["duration_ms"]>0]
    
    # Convertimos la columna de fecha de lanzamiento a tipo datetime, forzando errores a NaT
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    
    # Eliminamos filas con valores nulos en las columnas clave: álbum, nombre y fecha de lanzamiento
    df = df.dropna(subset=["album", "name", "release_date"])
    
    # Seleccionamos solo las columnas relevantes para el análisis y creamos una copia
    df_limpio = df[['id', 'name', 'album', 'artists', 'track_number', 'disc_number', 'explicit', 'danceability', 
                      'energy', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 
                      'duration_ms', 'time_signature', 'year', 'release_date']].copy()
    return df_limpio

# ¿Las canciones actuales son más cortas que antes?
def duracion_canciones(df_filtrado):
    
    # Convertimos la duración de milisegundos a minutos y redondeamos a 2 decimales
    df_filtrado["duration_min"] = (df_filtrado["duration_ms"] / 60000).round(2)

    # Eliminamos la columna de duración en milisegundos, ya que ahora tenemos la duración en minutos
    df_filtrado.drop(columns=["duration_ms"], inplace=True)

    # Calculamos la duración promedio de las canciones por año
    duracion_por_anio = df_filtrado.groupby("year")["duration_min"].mean().reset_index()

    # Graficamos la duración promedio de las canciones por año
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=duracion_por_anio, x="year", y="duration_min", marker="o")
    plt.title("Duración promedio de canciones por año")
    plt.xlabel("Año")
    plt.ylabel("Duración promedio (minutos)")
    plt.grid(True)
    plt.tight_layout()

    # Guardamos el gráfico como imagen
    plt.savefig("resultados/graficos/duracion_canciones.png")
    plt.close()  # Cerramos para liberar memoria

    return duracion_por_anio

# ¿La música es más alegre o triste con el tiempo?
def animo(df_filtrado):

    # Calculamos el valence promedio (alegría/tristeza) por año
    valence = df_filtrado.groupby("year")["valence"].mean().reset_index()

    # Graficamos el valence promedio
    plt.figure(figsize=(12, 6))
    plt.bar(valence["year"], valence["valence"], color='skyblue')
    plt.title("Valence promedio")
    plt.xlabel("Año")
    plt.ylabel("valence")
    plt.grid(axis="y", linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Guardamos el gráfico como imagen
    plt.savefig("resultados/graficos/valence.png")
    plt.close()
    
    return valence
    
# ¿Qué tan acústica, instrumental o hablada es la música actual?
def acustica(df_filtrado):

    # Definimos las características acústicas a analizar
    caracteristicas = ['danceability', 'energy', 'acousticness',
                    'instrumentalness', 'liveness', 'speechiness', 'valence']

    # Calculamos el promedio anual de cada característica acústica
    caracteristicas_acusticas = df_filtrado.groupby("year")[caracteristicas].mean().reset_index()

    # Graficamos la evolución de las características acústicas por año usando un gráfico de área apilado
    plt.figure(figsize=(14, 7))

    plt.stackplot(caracteristicas_acusticas["year"],
                [caracteristicas_acusticas[col] for col in caracteristicas],
                labels=caracteristicas, alpha=0.8)

    plt.title("Distribución de características acústicas por año")
    plt.xlabel("Año")
    plt.ylabel("Proporción promedio")
    plt.legend(loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    
        # Guardamos el gráfico como imagen
    plt.savefig("resultados/graficos/caracteristicas_acusticas.png")
    plt.close()

    return caracteristicas_acusticas

# ¿Las canciones ahora suenan con más fuerza?
def energia(df_filtrado):

    # Calculamos la energía promedio de las canciones por año
    energia = df_filtrado.groupby("year")['energy'].mean().reset_index()

    # Graficamos la energía promedio por año
    plt.figure(figsize=(12, 6))
    plt.bar(energia["year"], energia["energy"], color='skyblue')
    plt.title("Energía promedio por año")
    plt.xlabel("Año")
    plt.ylabel("Energía")
    plt.grid(axis="y", linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Guardamos el gráfico como imagen
    plt.savefig("resultados/graficos/energia.png")
    plt.close()

    return energia

# ¿Cuáles son los meses con más lanzamientos?

def lanzamientos_canciones(df_filtrado):

    # Extraemos el número y nombre del mes de la fecha de lanzamiento
    df_filtrado["mes_numero"] = df_filtrado["release_date"].dt.month
    df_filtrado["mes_nombre"] = df_filtrado["release_date"].dt.month_name()

    # Calculamos la cantidad de canciones lanzadas por mes
    lanzamientos = df_filtrado.groupby(["mes_numero", "mes_nombre"]).size().reset_index(name="cantidad")

    # Ordenamos los lanzamientos por el número de mes para graficar correctamente
    lanzamientos = lanzamientos.sort_values("mes_numero")

    # Graficamos la cantidad de canciones lanzadas por mes
    plt.figure(figsize=(12, 6))
    plt.bar(lanzamientos["mes_nombre"], lanzamientos["cantidad"], color="mediumseagreen")

    plt.title("Cantidad de canciones lanzadas por mes")
    plt.xlabel("Mes")
    plt.ylabel("Cantidad de canciones")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    
    plt.savefig("resultados/graficos/lanzamientos.png")
    plt.close()

    # Seleccionamos los 3 meses con más lanzamientos de canciones
    tres_meses = lanzamientos.nlargest(3, "cantidad")

    # Ordenamos los 3 meses de menor a mayor para graficar horizontalmente
    tres_meses = tres_meses.sort_values("cantidad", ascending=True)

    # Graficamos los 3 meses con más lanzamientos de canciones
    plt.figure(figsize=(8, 5))
    plt.barh(tres_meses["mes_nombre"], tres_meses["cantidad"], color="lightgreen")

    plt.title("Top 3 meses con más lanzamientos de canciones")
    plt.xlabel("Cantidad de canciones")
    plt.ylabel("Mes")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()

    # Guardamos el gráfico como imagen
    plt.savefig("resultados/graficos/tres_meses.png")
    plt.close()

    return lanzamientos, tres_meses

# ¿Hay más letras explícitas en la música de hoy?
def canciones_explicitas(df_filtrado):
    # Calculamos la cantidad de canciones explícitas por año
    explicitas = df_filtrado[df_filtrado["explicit"] == True].groupby("year").size()

    # Calculamos el total de canciones por año (explícitas + no explícitas)
    total_año = df_filtrado.groupby("year").size()

    # Calculamos el porcentaje de canciones explícitas por año
    porcentaje_explicitas = (explicitas / total_año) * 100

    # Calculamos la cantidad de canciones no explícitas por año
    no_explicitas = total_año - explicitas.fillna(0)

    # Creamos el DataFrame combinado de explícitas y no explícitas
    df_completo = pd.DataFrame({
        "explícitas": explicitas,
        "no_explícitas": total_año - explicitas.fillna(0)
    })

    # Limpiamos los NaN si hay
    df_completo = df_completo.fillna(0)

    # Convertimos a enteros para graficar correctamente
    df_completo = df_completo.astype(int)

    # Filtramos años a partir de 1990 para mejor visualización
    df_completo = df_completo[df_completo.index >= 1990]

    # Graficamos la comparación de canciones explícitas vs no explícitas por año
    plt.figure(figsize=(12, 6))

    # Creamos el eje x (años)
    años = df_completo.index.astype(str)
    x = range(len(años))

    # Ancho de cada barra
    ancho = 0.4

    # Dibujamos ambas barras (lado a lado)
    plt.bar(x, df_completo["explícitas"], width=ancho, label="Explícitas", color="crimson")
    plt.bar([i + ancho for i in x], df_completo["no_explícitas"], width=ancho, label="No explícitas", color="skyblue")

    # Ejes y títulos
    plt.xticks([i + ancho / 2 for i in x], años, rotation=45)
    plt.xlabel("Año")
    plt.ylabel("Cantidad de canciones")
    plt.title("Canciones explícitas vs no explícitas por año")
    plt.legend()
    plt.tight_layout()
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    
    # Guardamos el gráfico como imagen
    plt.savefig("resultados/graficos/canciones_explicitas.png")
    plt.close()

    return df_completo

def exportar_excel(df_duracion, df_animo, df_acustica, df_energia, df_lanzamientos, df_top3, df_explicitas, carpeta_graficos, carpeta_tablas):

    # Ruta del archivo Excel
    archivo_excel = carpeta_tablas / "analisis_spotify.xlsx"

    # Guardamos todas las tablas en distintas hojas del mismo archivo
    with pd.ExcelWriter(archivo_excel, engine="openpyxl") as writer:
        df_duracion.to_excel(writer, sheet_name="Duracion", index=False)
        df_animo.to_excel(writer, sheet_name="Valence", index=False)
        df_acustica.to_excel(writer, sheet_name="Acusticas", index=False)
        df_energia.to_excel(writer, sheet_name="Energia", index=False)
        df_lanzamientos.to_excel(writer, sheet_name="Lanzamientos", index=False)
        df_top3.to_excel(writer, sheet_name="Top 3 Meses", index=False)
        df_explicitas.to_excel(writer, sheet_name="Explicitas", index=False)
    
    # Insertamos los graficos en cada hoja
    wb = load_workbook(archivo_excel)
    graficos = {
        "Duracion": carpeta_graficos / "duracion_canciones.png",
        "Valence": carpeta_graficos / "valence.png",
        "Acusticas": carpeta_graficos / "caracteristicas_acusticas.png",
        "Energia": carpeta_graficos / "energia.png",
        "Lanzamientos": carpeta_graficos / "lanzamientos.png",
        "Top 3 Meses": carpeta_graficos / "tres_meses.png",
        "Explicitas": carpeta_graficos / "canciones_explicitas.png"
    }

    for hoja, ruta_img in graficos.items():
        if ruta_img.exists():
            ws = wb[hoja]
            img = Img(str(ruta_img))
            img.anchor = "H2"
            ws.add_image(img)

    wb.save(archivo_excel)
    print(f"Archivo guardado en: {archivo_excel}")



if __name__ == "__main__":

    # Leemos el archivo CSV con los datos de las canciones
    dataframe = pd.read_csv("tracks_features.csv")

    # Definimos la ruta base donde vamos a guardar todo
    ruta_resultados = Path("resultados")
    carpeta_graficos = ruta_resultados / "graficos"
    carpeta_tablas = ruta_resultados / "tablas"
    archivo_excel = carpeta_tablas / "analisis_spotify.xlsx"

    # Creamos las carpetas si no existen
    carpeta_graficos.mkdir(parents=True, exist_ok=True)
    carpeta_tablas.mkdir(parents=True, exist_ok=True)

    df_copia = limpieza_datos(dataframe)
    df_duracion = duracion_canciones(df_copia)
    df_animo = animo(df_copia)
    df_acustica = acustica(df_copia)
    df_energia = energia(df_copia)
    df_lanzamiento, df_top3 = lanzamientos_canciones(df_copia)
    df_explicitas = canciones_explicitas(df_copia)

    exportar_excel(df_duracion, df_animo, df_acustica, df_energia, df_lanzamiento, df_top3, df_explicitas, carpeta_graficos, carpeta_tablas)

