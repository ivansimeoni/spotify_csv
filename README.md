# 🎧 Análisis Estratégico de la Música con Datos de Spotify

Este proyecto no nace del azar. Surge de una intención clara: observar el cambio en la música desde un lugar de control y diseño.

Tomé un dataset de más de 1,2 millones de canciones para responder preguntas que muchos se hacen y pocos resuelven con datos:
¿Las canciones son más cortas? ¿Más explícitas? ¿Qué patrones marcan los lanzamientos cada año?

Pero no me interesaba un simple análisis.
Quería construir una herramienta que hablara por mí. Un informe automático, visual y profesional. Un entregable que pudiera generar en segundos y compartir con impacto.

Con solo ejecutar python main.py, obtengo un archivo Excel con gráficos embebidos que revela tendencias, decisiones de la industria, y cambios culturales, año tras año.

Por limitaciones de GitHub, el dataset completo (345 MB) no se incluye, pero el análisis fue realizado localmente sobre el conjunto completo.

📁 Puede descargarse el dataset completo desde: [Spotify Tracks Dataset (Kaggle)](https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs?resource=download)


## 🔍 Características destacadas

* Análisis cronológico de métricas musicales clave: duración, energía, valence, acústica, y letras explícitas.

* Identificación de patrones de lanzamiento por mes.

* Exportación automática a Excel, con gráficos embebidos y listos para presentación.

* Resultados visuales en alta calidad, generados en segundos desde consola.

* Código modular, reutilizable y fácil de escalar para nuevos análisis.


## ⚙️ Cómo funciona

El proyecto está diseñado para ejecutarse con un solo comando:

    ```bash
    python main.py
    ```

Este proceso realiza automáticamente:

Limpieza y depuración del dataset original (más de 1,2 millones de canciones).

Cálculo de estadísticas anuales para cada métrica clave.

Generación de gráficos en formato PNG para cada análisis.

Exportación a un archivo Excel con tablas y visualizaciones incrustadas.

El resultado final es un informe automatizado, claro y visualmente profesional, listo para compartir.


## Salidas

- **Gráficos**: Se generan imágenes en formato PNG para cada análisis en `resultados/graficos/`.
- **Reporte Excel**: Se crea un archivo Excel con tablas y gráficos incrustados en `resultados/tablas/analisis_spotify.xlsx`.


## 📦 Requisitos

* Python 3.11+
* pandas
* matplotlib
* seaborn
* openpyxl

Instalación de dependencias:

```bash
pip install pandas matplotlib seaborn openpyxl
```


## 🚀 Instrucciones para ejecutar la aplicación

1. Clonar el repositorio:

```bash
git clone https://github.com/ivansimeoni/spotify_csv.git
cd spotify_csv
```

2. Ejecutar el script principal:

```bash
python main.py
```

3. Ver los resultados en la carpeta `resultados/tablas/analisis_spotify.xlsx`

## 🧪 Ejemplo de uso

Este es un ejemplo real del funcionamiento completo del proyecto:

```bash
python main.py
```

Este comando realiza automáticamente:

* Limpieza del dataset completo de más de 1,2 millones de canciones.
* Cálculo de estadísticas anuales de duración, energía, valence, características acústicas, y canciones explícitas.
* Detección de los meses con mayor cantidad de lanzamientos musicales.
* Generación de gráficos para cada análisis.
* Exportación de todos los resultados en un archivo Excel con tablas y gráficos embebidos.

El resultado final es un informe listo para compartir, con insights como:

📉 Las canciones actuales son más cortas que hace 30 años.
🎶 Aumentó la proporción de canciones explícitas.
📈 La música ha ganado energía pero perdió duración.
📅 Enero, octubre, septiembre son los meses con más lanzamientos.


## 📊 Ejemplo visual

![Gráfico de canciones explicitas](img/grafico.png)


## 🗂️ Estructura del proyecto

```
spotify_csv/
├── main.py                  # Análisis y exportación
├── tracks_features.csv      # Dataset de entrada
├── resultados/
│   ├── graficos/            # PNGs de los gráficos
│   └── tablas/              # Excel con tablas + gráficos
├── img/                     # Imágenes usadas en el README
├── README.md
```


## 🔐 Consideraciones de seguridad

Este proyecto no maneja datos sensibles ni personales. Está pensado únicamente para fines educativos.


## 👨‍💼 Autor

[Iván Simeoni](https://github.com/ivansimeoni) | [LinkedIn](https://www.linkedin.com/in/ivansimeoni)

