productos = [
    ["Leche", 34, 87, 12, 95, 58],
    ["Queso", 6, 45, 78, 23, 91],
    ["Azúcar", 100, 15, 63, 4, 72],
    ["Harina", 28, 51, 99, 18, 163],
    ["Galletitas", 75, 39, 55, 1, 20]
]

cantidad_de_productos = 5
cantidad_de_sucursales = 5

def inicializar_array(largo: int) -> list:
    return [0] * largo

def cargar_array(largo: int) -> list:
    array = inicializar_array(largo)
    for i in range(len(array)):
        array[i] = input("Agregá un dato a la lista: ")
    return array

def inicializar_matriz(columnas: int, filas: int) -> list:
    matriz: list = [[0] * (columnas + 1) for _ in range(filas)]
    return matriz

def definir_nombres(matriz: list) -> list:
    for row_index in range(len(matriz)):
        for col_index in range(len(matriz[row_index])):
            if col_index == 0:
                matriz[row_index][col_index] = input(f"Ingresá el nombre del producto {row_index + 1}: ")
    return matriz

def cargar_matriz(matriz: list) -> list:
    for row_index in range(len(matriz)):
        print(f"Cargá el stock para el producto {matriz[row_index][0]}")
        for col_index in range(len(matriz[row_index])):
            if col_index > 0:
                matriz[row_index][col_index] = int(input(f"Ingresá el stock para el producto {matriz[row_index][0]} en la sucursal {col_index}: "))
        print("\n")
    return matriz

def calcular_stock_total(matriz: list) -> list:
    stocks = []
    for row in range(len(matriz)):
        total = 0
        for col in range(len(matriz[row])):
            if col > 0:
                total += matriz[row][col]
        total_producto = [matriz[row][0], total]
        stocks.append(total_producto)
    return stocks

def calcular_stock_menor(matriz: list) -> list:
    min_stock: int = matriz[0][1]
    min_prod: list = []
    for row_index in range(len(matriz)):
        for col_index in range(len(matriz[row_index])):
            if col_index > 0:
                if matriz[row_index][col_index] < min_stock:
                    min_stock = matriz[row_index][col_index]
                    min_prod = matriz[row_index]
    return min_prod

def mostrar_matriz(matriz: list) -> list:
    for i in range(len(matriz)):
        print(matriz[i][0])
        for j in range(len(matriz[i])):
            if j > 0:
                print(matriz[i][j])
        print("\n")

matriz = inicializar_matriz(cantidad_de_sucursales - 2, cantidad_de_productos - 2)
matriz = definir_nombres(matriz)
matriz = cargar_matriz(matriz)
mostrar_matriz(matriz)
stocks = calcular_stock_total(matriz)
mostrar_matriz(stocks)
stock_menor = calcular_stock_menor(stocks)
print(f"El producto con menor stock total es {stock_menor[0]} con {stock_menor[1]} unidades.")