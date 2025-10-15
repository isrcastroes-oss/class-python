print("=== EJERCICIO 1: Listas — Filtrar y ordenar ===")

numeros = [4, 7, 2, 4, 9, 2, 8, 6, 7]

# 1️ Eliminar duplicados
sin_duplicados = list(set(numeros))
print("Lista sin duplicados:", sin_duplicados)

# 2️ Ordenar de menor a mayor
ordenada = sorted(sin_duplicados)
print("Lista ordenada:", ordenada)

# 3️ Mostrar solo los números pares
pares = [num for num in ordenada if num % 2 == 0]
print("Números pares:", pares)

print("\n--------------------------------------------\n")

# ============================================
#  EJERCICIO 2: Tuplas — Operaciones básicas
# ============================================

print("=== EJERCICIO 2: Tuplas — Operaciones básicas ===")

numeros_tupla = (5, 8, 12, 3, 9, 5, 2)

# 1️ Máximo y mínimo
print("Máximo:", max(numeros_tupla))
print("Mínimo:", min(numeros_tupla))

# 2️ Calcular promedio
promedio = sum(numeros_tupla) / len(numeros_tupla)
print("Promedio:", round(promedio, 2))

# 3️ Verificar si un número está en la tupla
num_usuario = int(input("Ingrese un número: "))

if num_usuario in numeros_tupla:
    print(f"El número {num_usuario} sí está en la tupla.")
else:
    print(f"El número {num_usuario} no está en la tupla.")

print("\n--------------------------------------------\n")

# ============================================
# EJERCICIO 3: Diccionarios — Inventario de productos
# ============================================

print("=== EJERCICIO 3: Diccionarios — Inventario de productos ===")

inventario = {"manzanas": 10, "peras": 3, "naranjas": 8}

# 1️ Agregar nuevo producto
nuevo_producto = input("Ingrese el nombre del nuevo producto: ").lower()
cantidad = int(input(f"Ingrese la cantidad de {nuevo_producto}: "))
inventario[nuevo_producto] = cantidad

# 2️ Actualizar cantidad de un producto existente
producto_actualizar = input("Ingrese el producto a actualizar: ").lower()
if producto_actualizar in inventario:
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    inventario[producto_actualizar] = nueva_cantidad
else:
    print("Ese producto no existe en el inventario.")

# 3️ Mostrar productos con stock bajo (<5)
print("\nProductos con stock bajo:")
for producto, stock in inventario.items():
    if stock < 5:
        print(f"{producto} - {stock}")

print("\n=== FIN DEL PROGRAMA ===")
