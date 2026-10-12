from pathlib import Path
 
# Carpeta donde está este .py (funciona sin importar desde dónde lo ejecutes)
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

ARCHIVO = "data/catalogo.txt"
SEPARADOR = ";"

# ---------- Fucniones de Validación ----------
def es_entero(texto):
    #Si es verdadero, el texto es un número entero mayor o igual a 0.
    return texto.isdigit()
 
def es_decimal(texto):
    #Si es verdadero, el texto es un número con, como máximo, un punto decimal.
    return texto.replace(".", "", 1).isdigit()

def leer_texto(mensaje):
    #Valida que el texto ingresado no esté vacío y repite hasta que sea válido.
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: el campo no puede estar vacío.")

def leer_cantidad(mensaje):
    #Valida que el texto ingresado sea un entero mayor o igual a 0 y repite hasta que sea válido.
    while True:
        texto = input(mensaje).strip()
        if es_entero(texto):
            return int(texto)
        print("Error: ingrese un número entero mayor o igual a 0.")
 
 
def leer_precio(mensaje):
    #Valida que el texto ingresado sea un decimal mayor que 0 y repite hasta que sea válido.
    while True:
        texto = input(mensaje).strip()
        if es_decimal(texto) and float(texto) > 0:
            return float(texto)
        print("Error: ingrese un precio mayor que 0 (ejemplo: 4.50).")

# ---------- Fucniones del programa ----------
def buscar_posicion(codigo_producto, codigo):
    #Búsqueda secuencial: devuelve la posición del código o -1 si no existe.
    for i in range(len(codigo_producto)):
        if codigo_producto[i] == codigo:
            return i
    return -1

#Opción 1: Mostrar catálogo
def mostrar_catalogo(codigo_producto, descripcion, tipo_producto, cantidad, precio_venta):
    """Muestra todos los productos en formato de tabla."""
    if len(codigo_producto) == 0:
        print("El catálogo está vacío.")
        return
    print(f"\n{'CÓDIGO':<8}{'DESCRIPCIÓN':<28}{'TIPO':<18}{'CANT.':>6}{'PRECIO (S/)':>13}")
    print("-" * 73)
    for i in range(len(codigo_producto)):
        print(f"{codigo_producto[i]:<8}{descripcion[i]:<28}{tipo_producto[i]:<18}"
              f"{cantidad[i]:>6}{precio_venta[i]:>13.2f}")#2f: redondea a 2 decimales
    print(f"Total de productos: {len(codigo_producto)}")

#Opción 2: Buscar producto
def buscar_producto(codigo_producto, descripcion, tipo_producto, cantidad, precio_venta):
    codigo = leer_texto("Código a buscar: ").upper()
    posicion = buscar_posicion(codigo_producto, codigo)
    if posicion == -1:
        print("Producto no encontrado.")
    else:
        print(f"Código: {codigo_producto[posicion]} | {descripcion[posicion]} | {tipo_producto[posicion]} | "
              f"Stock: {cantidad[posicion]} | S/ {precio_venta[posicion]:.2f}")#2f: redondea a 2 decimales

#Opción 3: Agregar producto
def agregar_producto(codigo_producto, descripcion, tipo_producto, cantidad, precio_venta):
    codigo = leer_texto("Código nuevo: ").upper()
    if buscar_posicion(codigo_producto, codigo) != -1:
        print("Producto ya existe")
        return
    # Se definen variables locales para no modificar las listas hasta que todos los datos sean válidos
    nueva_descripcion = leer_texto("Descripción: ")
    nuevo_tipo = leer_texto("Tipo de producto: ")
    nueva_cantidad = leer_cantidad("Cantidad disponible: ")
    nuevo_precio = leer_precio("Precio de venta (S/): ")
    #Mediante append() se agregan los datos a las listas correspondientes
    codigo_producto.append(codigo)
    descripcion.append(nueva_descripcion)
    tipo_producto.append(nuevo_tipo)
    cantidad.append(nueva_cantidad)
    precio_venta.append(nuevo_precio)
    print("Producto agregado.")

#Opción 4: Modificar producto
def modificar_producto(codigo_producto, descripcion, tipo_producto, cantidad, precio_venta):
    """Modifica descripción, tipo, stock o precio. Enter mantiene el valor actual."""
    codigo = leer_texto("Código del producto a modificar: ").upper()
    posicion = buscar_posicion(codigo_producto, codigo)
    if posicion == -1:
        print("Producto no encontrado.")
        return
 
    print("(Deje vacío y presione Enter para mantener el valor actual)")
 
    nueva_descripcion = input(f"Descripción [{descripcion[posicion]}]: ").strip()
    if nueva_descripcion != "":
        descripcion[posicion] = nueva_descripcion
 
    nuevo_tipo = input(f"Tipo [{tipo_producto[posicion]}]: ").strip()
    if nuevo_tipo != "":
        tipo_producto[posicion] = nuevo_tipo
 
    nuevo_stock = input(f"Stock [{cantidad[posicion]}]: ").strip()
    if nuevo_stock != "":
        if es_entero(nuevo_stock):
            cantidad[posicion   ] = int(nuevo_stock)
        else:
            print("Stock inválido (entero mayor o igual a 0). Se mantiene el anterior.")
 
    nuevo_precio = input(f"Precio [{precio_venta[posicion]:.2f}]: ").strip()
    if nuevo_precio != "":
        if es_decimal(nuevo_precio) and float(nuevo_precio) > 0:
            precio_venta[posicion] = float(nuevo_precio)
        else:
            print("Precio inválido (debe ser mayor que 0). Se mantiene el anterior.")
 
    print("Producto modificado.")
 
 #Opción 5: Eliminar producto
def eliminar_producto(codigo_producto, descripcion, tipo_producto, cantidad, precio_venta):
    codigo = leer_texto("Código del producto a eliminar: ")
    posicion = buscar_posicion(codigo_producto, codigo)#posicion es la variable que almacena la posición del producto a eliminar
    if posicion == -1:
        print("Producto no encontrado.")
        return
#pop() elimina el elemento en la posición especificada de cada lista
    codigo_producto.pop(posicion)
    descripcion.pop(posicion)
    tipo_producto.pop(posicion)
    cantidad.pop(posicion)
    precio_venta.pop(posicion)
    print("Producto eliminado.")
    
# ---------- Persistencia (archivo de texto) ----------
#Carga de catalogo desde archivo de texto. Cada línea del archivo tiene 5 campos separados por ";"
def cargar_catalogo(codigo_producto, descripcion, tipo_producto, cantidad, precio_venta):
    #Lee el archivo y reparte cada línea en las cinco listas.
    archivo = open(ARCHIVO, "r", encoding="utf-8")
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            campos = linea.split(SEPARADOR)
            codigo_producto.append(campos[0])
            descripcion.append(campos[1])
            tipo_producto.append(campos[2])
            cantidad.append(int(campos[3]))
            precio_venta.append(float(campos[4]))
    archivo.close()
    print("Catálogo cargado:", len(codigo_producto), "productos.")

def guardar_catalogo(codigo_producto, descripcion, tipo_producto, cantidad, precio_venta):
    archivo = open(ARCHIVO, "w", encoding="utf-8")#definí este encoding para que no me tire error al guardar acentos usados comunmente en español
    for i in range(len(codigo_producto)):
        linea = (codigo_producto[i] + ";" + descripcion[i] + ";" + tipo_producto[i] + ";"
                 + str(cantidad[i]) + ";" + str(precio_venta[i]))
        archivo.write(linea + "\n")
    archivo.close()
    print("Catálogo guardado:", len(codigo_producto), "productos.")
 
# ---------- Menú ----------
def mostrar_menu(total_productos):
    #Lista de opciones del menú
    print("\n===== TIENDA PILOTO =====")
    print(f"Productos en catálogo: {total_productos}")
    print("1. Mostrar catálogo")
    print("2. Buscar producto")
    print("3. Agregar producto")
    print("4. Modificar producto")
    print("5. Eliminar producto")
    print("6. Guardar catálogo")
    print("0. Salir")
 
# ---------- Ejecución del programa ----------
def main():
    # Las cinco listas paralelas
    codigo_producto = []
    descripcion = []
    tipo_producto = []
    cantidad = []
    precio_venta = []
 
    cargar_catalogo(codigo_producto, descripcion, tipo_producto, cantidad, precio_venta)
 
    opcion = ""
    while opcion != "0":
        mostrar_menu(len(codigo_producto))
        opcion = input("Seleccione una opción: ").strip()
        listas = (codigo_producto, descripcion, tipo_producto, cantidad, precio_venta)
 
        if opcion == "1":
            mostrar_catalogo(*listas)
        elif opcion == "2":
            buscar_producto(*listas)
        elif opcion == "3":
            agregar_producto(*listas)
        elif opcion == "4":
            modificar_producto(*listas)
        elif opcion == "5":
            eliminar_producto(*listas)
        elif opcion == "6":
            guardar_catalogo(*listas)
        elif opcion == "0":
            guardar_catalogo(*listas)
        else:
            print("Opción inválida. Intente de nuevo.")
 
if __name__ == "__main__":
    main()