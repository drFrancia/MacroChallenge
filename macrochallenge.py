import time
import tracemalloc

def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)

def quickSortHelper(arr, low, high):
    if low < high:
        # Umbral para usar Insertion Sort en sublistas pequeñas
        if high - low < 10:
            insertionSort(arr, low, high)
        else:
            pi = partition(arr, low, high)
            quickSortHelper(arr, low, pi - 1)
            quickSortHelper(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = medianOfThree(arr, low, high)
    arr[pivot], arr[high] = arr[high], arr[pivot]
    pivot = high
    i = low - 1
    for j in range(low, high):
        if arr[j] < arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]
    return i + 1

def medianOfThree(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return mid

def insertionSort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generar_datos(tamaño):
    from random import randint
    return [randint(0, 10000) for _ in range(tamaño)]

def medir_rendimiento(datos):
    tracemalloc.start()
    tiempo_inicio = time.time()
    quickSort(datos)
    tiempo_fin = time.time()
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return {
        'tiempo': tiempo_fin - tiempo_inicio,
        'memoria_actual': memoria_actual,
        'memoria_pico': memoria_pico,
        'correctitud': datos == sorted(datos)
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
