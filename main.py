from pathlib import Path
 
# Carpeta donde está este .py (funciona sin importar desde dónde lo ejecutes)
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

ARCHIVO = "data/catalogo.txt"
SEPARADOR = ";"

# ---------- Fucniones de Validación ----------
def leer_texto(mensaje):
    #Valida que el texto ingresado no esté vacío y repite hasta que sea válido.
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: el campo no puede estar vacío.")
        
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

# ---------- Persistencia (archivo de texto) ----------
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
        elif opcion in ("3", "4", "5", "6"):
            print("Opción aún no implementada.")
        elif opcion == "0":
            print("Hasta luego.")
        else:
            print("Opción inválida. Intente de nuevo.")
 
 
if __name__ == "__main__":
    main()
 