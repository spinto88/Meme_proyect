- Primero corre Extraction_data_leskovec para aislar las series en una carpeta que es Data Disgregada.
Necesita data_original_leskovec.txt

- Después cortamos las series hasta 3 días antes del pico y 21 despues con corte y rolling (corte + suavizado). La integracion despues se hace hasta una semana desde algun pico creo pero las decisiones de que series tomar son con este corte.
