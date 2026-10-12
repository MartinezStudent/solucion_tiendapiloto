# Tienda Piloto

Programa de consola para administrar el catálogo de productos de una tienda. Permite consultar, registrar, actualizar y eliminar productos desde un menú sencillo, y guarda la información para usarla la próxima vez que se abra el programa.

## Funcionalidades

| Opción | Funcionalidad | Descripción |
|:------:|---------------|-------------|
| 1 | Mostrar catálogo | Muestra todos los productos en una tabla con su código, descripción, tipo, cantidad disponible y precio de venta. |
| 2 | Buscar producto | Permite consultar un producto escribiendo su código. |
| 3 | Agregar producto | Registra un nuevo producto. No permite repetir códigos ni dejar datos vacíos o inválidos. |
| 4 | Modificar producto | Actualiza la descripción, el tipo, el stock o el precio de un producto. Si dejas un dato en blanco, se mantiene el valor actual. |
| 5 | Eliminar producto | Quita un producto del catálogo. |
| 6 | Guardar catálogo | Guarda en el archivo todos los cambios realizados. |
| 0 | Salir | Guarda automáticamente los cambios y cierra el programa. |

Al iniciar, el programa carga los productos existentes y muestra en el menú cuántos hay en el catálogo.

## Cómo usarlo

1. Descarga o clona este repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecuta el programa:

```
python main.py
```

4. Elige una opción escribiendo su número y sigue las indicaciones en pantalla.

## Datos del catálogo

Los productos se guardan en el archivo `catalogo.txt` creado