import time
import tracemalloc

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivote]
    medio = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    return quickSort(izquierda) + medio + quickSort(derecha)

def generar_datos(tamaño):
    from random import randint
    return [randint(0, 10000) for _ in range(tamaño)]

def medir_rendimiento(datos):
    tracemalloc.start()
    tiempo_inicio = time.time()
    datos_ordenados = quickSort(datos)
    tiempo_fin = time.time()
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return {
        'tiempo': tiempo_fin - tiempo_inicio,
        'memoria_actual': memoria_actual,
        'memoria_pico': memoria_pico,
        'correctitud': datos_ordenados == sorted(datos)
    }

# Generar conjuntos de datos
datos_pequeños = generar_datos(100)
datos_medianos = generar_datos(300)
datos_grandes = generar_datos(500)

# Medir rendimiento
rendimiento_pequeño = medir_rendimiento(datos_pequeños)
rendimiento_mediano = medir_rendimiento(datos_medianos)
rendimiento_grande = medir_rendimiento(datos_grandes)

# Resultados
print("Rendimiento Datos Pequeños:", rendimiento_pequeño)
print("Rendimiento Datos Medianos:", rendimiento_mediano)
print("Rendimiento Datos Grandes:", rendimiento_grande)
