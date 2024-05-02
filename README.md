# Trabajo Práctico Integrador (PreParcial)

## Instrucciones para hacer funcionar el proyecto
Una vez descargado el proyecto se debe proceder a instalar el entorno virtual con el siguiente comando:

```bash
virtualenv my-env
```

Las librerias utilizadas son Pandas y Matplotlib por lo cual procedemos a instalar las mismas

```bash
pip install pandas
```

```bash
pip install matplotlib
```

Una vez realizadas estas acciones ya podras ejecutar el proyecto, estando posicionado en el directorio correcto y mediante el comando

```bash
python index.py
```

Cuando termines de usar el proyecto no olvides de cerrar el entorno virtual mediante el comando

```bash
deactivate
```

## ¿Qué realiza este proyecto?

En primera instancia leemos el archivo csv y lo transformamos en un DataFrame.

Luego creamos una lista que contenga las fechas de la columna "age". Ya teniendo dichas fechas, las comparamos con la fecha del día de hoy y realizamos las operaciones necesarias para obtener una nueva lista, pero en este caso, contendra las edades en valores numéricos.

Agregamos una columna a nuestro DataFrame con la última lista de edades.

Creamos un nuevo DataFrame ordenado ascendentemente por edad y filtrando a los que son mayores de 25 años.

Ahora creamos una lista pero tomando las edades numéricas de nuestro ultimo DataFrame, en base a esta, creamos un diccionario que contenga como claves las edades y como valores sus respectivas frecuencias (un diccionario de contadores).

En base al diccionario informamos la cantidad de edades existentes y sus respectivas frecuencias.

Por último, tambien usamos el diccionario para crear un DataFrame más comprimido que tendra solo las edades mayores a 25 y sus respectivas frecuencias (cantidad de personas que tiene dicha edad). 

Terminamos este proyecto realizando un polígono de frecuencias del ultimo DataFrame.

