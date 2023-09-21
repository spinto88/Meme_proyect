

Dentro de la carpeta Extraccion de datos hacer lo siguiente:

- Primero corre Extraction_data_leskovec (python Extraccion...py) para aislar las series en una carpeta que es Data Disgregada.
Necesita data_original_leskovec.txt (si el archivo tiene extension .txt.zst, primero descomprimir este archivo. Descargar de https://nube.df.uba.ar/index.php/s/Dx2pk7rJ96CTq8s).

- Después cortamos las series hasta 3 días antes del pico y 21 despues con python Corte...py (esto hace el corte + suavizado). La integracion despues se hace hasta una semana desde algun pico.

- Series_analizadas tiene el id de las 200 series a las que se le realizo el ajuste.

- Estadistica hace sobre las series completas. Ya hay datos preprocesados. 

Dentro de la carpeta Integracion y analisis:

- Integracion modelo ajuste muestra como se hace el ajuste para una serie.
- Los mejores ajustes encontrados estan dentro de Analisis como Parametros_finales.csv
- Integracion_modelo_parametros hace las figuras finales en base al archivo anterior.
- Dentro de analisis está Clustering que representa las series ajustas en el espacio de parametros y ademas está el archivo con Clasificacion_series que fueron etiquetadas a mano (que es cada etiqueta esta dentro de la Clustering).


Edited_images:

- Tiene los .odg para editar para figuras finales del paper. Exportar a pdf una vez terminado de editar.   
