![image](https://github.com/ic-222/EXAMEN-iii/assets/136537533/27136b7a-fa0b-4e41-be71-6ad28b6c7837)


Este gestor de gastos es una aplicación web simple construida con Flask, un marco de desarrollo web de Python. 
## Características

1. **Registro de Gastos:**
   - Los usuarios pueden ingresar información detallada sobre sus gastos diarios, incluyendo el nombre, cantidad gastada, descripción y elegir una categoría predefinida.

2. **Visualización de Gastos:**
   - Lista estructurada con la posiblidad de ordenar por nombre y cantidad de manera ascendente.
   - Opciones de filtrado por cada categoría.

3. **Estadísticas Básicas:**
   - Se podrá observar un total de gastos.

4. **Edición y Eliminación:**
   - Los usuarios pueden editar la información de gastos existentes y eliminar gastos no deseados.


# Requisitos
Será necesario tener instalado en el sistema pip, Python y *añadirlo al path*, git y un editor de código para poder configurar la app. (Hasta con un bloc de notas podrás llevar a cabo este paso)
Python: https://www.python.org/downloads/
![image](https://github.com/ic-222/EXAMEN-iii/assets/136537533/ec6dd1b7-0261-421e-864f-b385e69cf65d)


## Pasos para usarla

### Clonar el repositorio
Para comenzar, clona el repositorio de GitHub a tu máquina local usando el siguiente comando en una terminal o línea de comandos de git bash que abras dentro de la ubicación de tu preferencia:

```bash
git clone https://github.com/ic-222/EXAMEN-iii
```
Si no posees git en tu sistema, puedes descargar el proyecto en un archivo zip y descomprimirlo.
![image](https://github.com/ic-222/EXAMEN-iii/assets/136537533/0f240e40-e4ac-4a84-8389-88ec5289dd5c)
![image](https://github.com/ic-222/EXAMEN-iii/assets/136537533/5749a3e1-af28-415f-bec9-2b3ff30687bd)

### Instalar Requerimientos
Ubícate en la carpeta donde clonaste/descargaste el repositorio, abre una terminal y ejecuta el siguiente comando, así conseguirás todos los módulos usados para que funcione la app.
![image](https://github.com/ic-222/EXAMEN-iii/assets/136537533/358e9c06-7a59-4723-b985-4d09620cc50a)


```bash
pip install -r requirements.txt
```

## Configuración de la app
Cambia la Ruta de la Base de Datos:
Abre el archivo config.py en el directorio raíz del proyecto. Encuentra la línea que contiene DATABASE_CONNECTION_STRING y cambia la ruta del archivo .accdb para que coincida con la ubicación de tu base de datos MS Access en tu sistema local.
![image](https://github.com/ic-222/EXAMEN-iii/assets/136537533/3009c9c3-eb61-4181-b9a0-579772a07683)
Recuerda quitarle las comillas y seguir el el formato del código.

```python
DATABASE_CONNECTION_STRING = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=TU_RUTA.accdb;'
```

# Ejecutando la aplicación...

En la terminal que usaste para instalar los requerimientos ejecuta el siguiente comando:

``` bash
python app.py
```

La aplicación se ejecutará en http://localhost:5000/. Abre tu navegador web y visita esa dirección para ver la aplicación de Lista de Tareas en acción.


*Ivanna S. Cervantes A. 2023*
