def inicializar_matriz(columnas: int, filas: int, valor_inicial: any = 0) -> list:
    matriz: list = [[valor_inicial] * columnas for _ in range(filas)]
    return matriz

def cargar_matriz(matriz: list, nombre_columnas: list) -> list:
    for i in range(len(matriz)):
        print(f"Persona {i + 1}")
        for j in range(len(matriz[i])):
            matriz[i][j] = input(f"Ingresá el valor para la columna {nombre_columnas[j]}: ")
        print("\n")
    return matriz

def ver_matriz(matriz: list, nombre_columnas: list) -> None:
    fila_nombres: str = ""
    for i in range(len(nombre_columnas)):
        fila_nombres += f"{nombre_columnas[i]}\t"
    print(fila_nombres)
    for i in range(len(matriz)):
        fila: str = ""
        for j in range(len(matriz[i])):
            fila += f"{matriz[i][j]}\t"
        print(fila)

def contar_mas_30(matriz: list) -> int:
    mayores: int = 0
    for persona in range(len(matriz)):
        edad = int(matriz[persona][1])
        if edad >= 30:
            mayores += 1
    return mayores

def main() -> None:
    columnas = 4
    filas = 3
    valor_inicial = "-"
    nombre_columnas = ["Nombre", "Edad", "Ciudad"]
    matriz = inicializar_matriz(filas, columnas, valor_inicial)
    matriz = cargar_matriz(matriz, nombre_columnas)
    # matriz = [
    #     ["Thiago", 25, "Avellaneda"],
    #     ["Esteban", 31, "Sarandi"],
    #     ["Candelaria", 25, "San Miguel del Monte"],
    #     ["Marcelo", 32, "Wilde"],
    # ]
    ver_matriz(matriz, nombre_columnas)
    mayores = contar_mas_30(matriz)
    print(f"Mayores de 30 años: {mayores}")

main()