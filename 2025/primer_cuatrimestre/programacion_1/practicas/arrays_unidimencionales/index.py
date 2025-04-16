def crear_array(largo: int) -> list:
    # Punto 1
    return [0] * largo

def cargar_array(largo: int) -> list:
    # Punto 2
    array = crear_array(largo)
    for i in range(largo):
        array[i] = int(input("Ingresá un número entero: "))
    return array

def promedio(array: list) -> float:
    # Punto 3
    acumulador = 0
    for n in array:
        acumulador += n
    return acumulador / len(array)

def promedio_de_positivos(array: list) -> float:
    # Punto 4
    acumulador = 0
    positivos = 0
    for n in array:
        if n < 0:
            continue
        acumulador += n
        positivos += 1
    return acumulador / positivos

def producto_total(array: list) -> int:
    # Punto 5
    producto = 1
    for n in array:
        producto *= n
    return producto

def max_pos(array: list) -> int:
    # Punto 6
    max = 0
    for i in range(len(array)):
        if array[i] > array[max]:
            max = i
    return max

def max_posis(array: list) -> list:
    # Punto 7
    poses = []
    max = 0
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    for i in range(len(array)):
        if array[i] == max:
            poses.append(i)
    return poses

def reemp_nombres(lista_nombres: list, nombre_antiguo: str, nombre_nuevo: str) -> int:
    # Punto 8
    n_reemplazos = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            n_reemplazos += 1
    print(lista_nombres)
    return n_reemplazos

def interseccion(array_1: list, array_2: list) -> list:
    interseccion_list = []
    for e_1 in range(len(array_1)):
        if array_1[e_1] in array_2:
            interseccion_list.append(array_1[e_1])
            
    return interseccion_list

def union(array_1: list, array_2: list) -> list:
    union_list = []
    for e_1 in range(len(array_1)):
        if array_1[e_1] not in union_list:
            union_list.append(array_1[e_1])

    for e_2 in range(len(array_2)):
        if array_2[e_2] not in union_list:
            union_list.append(array_2[e_2])
    
    return union_list

def dif(array_1: list, array_2: list) -> list:
    dif_list = []
    for e_1 in range(len(array_1)):
        if array_1[e_1] not in array_2:
            dif_list.append(array_1[e_1])

    for e_2 in range(len(array_2)):
        if array_2[e_2] not in array_1:
            dif_list.append(array_2[e_2])

    return dif_list

def main():
    p1 = crear_array(5)
    print(f"Crear array por cantidad: {p1}\n")

    p2 = cargar_array(5)
    print(f"Cargar array: {p2}\n")

    p3 = promedio(p2)
    print(f"Promedio general: {p3}\n")

    p4 = promedio_de_positivos(p2)
    print(f"Promedio de positivos: {p4}\n")

    p5 = producto_total(p2)
    print(f"Producto total: {p5}\n")

    p6 = max_pos(p2)
    print(f"Posición del número máximo: {p6}\n")

    p7 = max_posis(p2)
    print(f"Posiciones del número máximo: {p7}\n")

    lista_de_nombres = ["Thiago", "Samay", "Samay", "Mario", "Franco"]

    p8 = reemp_nombres(lista_de_nombres, "Samay", "Novia")
    print(f"Cantidad de reemplazos: {p8}\n")

    conjunto_1 = [1,2,3,4,5]
    conjunto_2 = [3,4,5,6,7]
    p9 = interseccion(conjunto_1, conjunto_2)
    print(f"Intersección de conjuntos: {p9}\n")

    p10 = union(conjunto_1, conjunto_2)
    print(f"Unión de conjuntos: {p10}\n")

    p11 = dif(conjunto_1, conjunto_2)
    print(f"Diferencia de conjuntos: {p11}\n")
    
    
main()

