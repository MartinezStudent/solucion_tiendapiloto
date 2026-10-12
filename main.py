from pathlib import Path
 
# Carpeta donde está este .py (funciona sin importar desde dónde lo ejecutes)
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
 
ARCHIVO = "data/catalogo.txt"
SEPARADOR = ";"
 
 
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
 
        if opcion in ("1", "2", "3", "4", "5", "6"):
            print("Opción aún no implementada.")
        elif opcion == "0":
            print("Hasta luego.")
        else:
            print("Opción inválida. Intente de nuevo.")
 
if __name__ == "__main__":
    main()