def inicializar_mtz(cols: int, filas: int, valor_inicial: any = 0) -> list:
    """
    Crea una matriz vacía con un valor inicial o por defecto.
    Recibe una cantidad de columnas y una cantidad de filas.
    Devuelve una matriz con el valor inicial, o 0 si no se pasa un valor inicial.
    """
    # Le sumamos 1 a las columnas para poder mostrar el ID
    return [[valor_inicial] * (cols + 1) for _ in range(filas)]


def cargar_mtz(mtz: list, nombres_cols: list) -> list:
    """
    Carga datos en una matriz previamente inicializada con datos ingresados por el usuario.
    Recibe una matriz inicializada con un valor por defecto y una lista de nombres de columnas para ayudar al usuario a cargar los datos.    
    Devuelve la matriz llena con los valores cargados por el usuario.
    """
    for fila_i in range(len(mtz)):
        for col_i in range(len(mtz[fila_i])):
            if col_i == 0:
                # Le cargamos el ID a la fila empezando por el 1
                mtz[fila_i][col_i] = str(fila_i + 1)
            elif col_i == 3 or col_i == 5:
                # Verificamos que el dato sea correcto para las columnas de edad y goles
                while True:
                    valor_ingresado = int(
                        input(f"Ingresá {nombres_cols[col_i]} del jugador: "))
                    if valor_ingresado < 0:
                        print(
                            "❌ Error: tanto la edad como la cantidad de goles debe ser un número mayor o igual que 0.")
                    else:
                        mtz[fila_i][col_i] = valor_ingresado
                        break
            else:
                mtz[fila_i][col_i] = input(
                    f"Ingresá {nombres_cols[col_i]} del jugador: ")
        print("\n")
    return mtz


def mostrar_mtz(mtz: list, nombres_cols: list) -> None:
    """
    Muestra la matriz en la consola de manera legible.
    Recibe la matriz y los nombres de las columnas.
    No devuelve nada.
    """
    num_cols = len(nombres_cols)

    # Tenemos que conseguir el ancho de las columnas para que la tabla no tenga filas desalineadas
    ancho_cols = [0] * num_cols
    for i in range(num_cols):
        ancho_cols[i] = len(str(nombres_cols[i]))

    # Ahora tenemos que calcular la columna más ancha para que todas las filas tomen su ancho en ese valor
    for fila_i in range(len(mtz)):
        for col in range(num_cols):
            valor = str(mtz[fila_i][col])
            if len(valor) > ancho_cols[col]:
                ancho_cols[col] = len(valor)

    # Ahora creamos el encabezado de la matriz
    encabezado = ""
    for i in range(num_cols):
        espacio = ancho_cols[i] + 3
        encabezado += f"{nombres_cols[i]:<{espacio}}"
    print(encabezado)

    # Agregamos una línea separadora
    largo = 0
    for i in range(num_cols):
        largo = largo + ancho_cols[i] + 3
    print("-" * largo)

    # Imprimimos cada fila de la matriz
    for fila_i in range(len(mtz)):
        fila = ""
        for col_i in range(num_cols):
            valor = str(mtz[fila_i][col_i])
            espacio = ancho_cols[col_i] + 3
            fila += f"{valor:<{espacio}}"
        print(fila)


def mod_mtz(mtz: list, nombres_cols: list) -> list:
    """
    Modifica el dato de una celda en particular elegida por el usuario de una matriz.
    Recibe una matriz cargada y los nombres de las columnas para ayudar al usuario a modificar los datos.
    Devuelve la matriz actualizada.
    """
    print("Matriz actual")
    mostrar_mtz(mtz, nombres_cols)

    cols = ""
    for col_i in range(len(nombres_cols)):
        if col_i == 0:
            continue
        cols += f"{nombres_cols[col_i]}({col_i}) "
    print(cols)
    while True:
        col = int(
            input("Ingresá el dato a modificar mediante el número de columna: "))
        if col not in range(len(nombres_cols)) or col == 0:
            print(
                f"❌ Error: el número ingresado no está en el rango permitido. Intentá de nuevo ingresando un número del 1 al {len(nombres_cols) - 1}")
            continue
        else:
            break
    while True:
        fila = int(
            input("Ingresá el jugador a modificar mediante el número de la fila: "))
        if fila not in range(len(mtz) + 1) or fila == 0:
            print(
                f"❌ Error: el número ingresado no está en el rango permitido. Intentá de nuevo ingresando un número del 1 al {len(mtz)}")
            continue
        else:
            break

    print(
        f"Cambiaremos el dato {nombres_cols[col]} para el jugador {fila}")
    if col == 3 or col == 5:
        while True:
            valor_ingresado = int(
                input(f"Ingresá el nuevo dato para {nombres_cols[col]} del jugador {fila}: "))
            if valor_ingresado < 0:
                print(
                    "❌ Error: tanto la edad como la cantidad de goles debe ser un número mayor o igual que 0.")
            else:
                mtz[fila - 1][col] = valor_ingresado
                break
    else:
        mtz[fila - 1][col] = input(
            f"Ingresá el nuevo dato para {nombres_cols[col]} del jugador {fila}: ")
    return mtz
