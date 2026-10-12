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

## El código de producto

Cada producto tiene un **código único** que lo identifica dentro del catálogo. 
Tiene el formato **`P` seguido de 5 dígitos** (por ejemplo, `P00001`, `P00002`, ..., `P00030`). Con él se realizan las siguientes operaciones:

- **Opción 2: Buscar producto:** se consulta un producto escribiendo su código.
- **Opción 4: Modificar producto:** el código del nuevo producto no puede coincidir con el de otro ya registrado.
- **Opción 5: Eliminar producto:** se indica el código del producto que se desea cambiar o quitar.

Algunas consideraciones:

- Los códigos se guardan en mayúsculas. Al buscar, agregar o modificar puedes escribirlos en minúsculas (`p00001` equivale a `P00001`), pero al eliminar debes escribirlos en mayúsculas.
- Si el código no existe en el catálogo, el programa avisa que el producto no fue encontrado.
- El código no se puede cambiar desde la opción de modificar. Si necesitas otro código, elimina el producto y vuelve a agregarlo.
- Dentro del catálogo del producto hay registrados 30 de estos, yendo desde el P00001 hasta el P00030
*El caso de la problemática indica que hay alrededor de 1200 registros, sin embargo se colocó 30 productos para realizar las prueabs dentro del código desarrollado*

## Cómo usarlo

1. Descarga o clona este repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el programa:

```
python main.py
```

4. Elige una opción escribiendo su número y sigue las indicaciones en pantalla.

## Datos del catálogo

Los productos se guardan en el archivo `catalogo.txt`, dentro de la carpeta `data`. Si el archivo no existe, el programa lo crea al iniciar.