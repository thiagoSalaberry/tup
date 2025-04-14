def clasificar_n(n: int) -> str:
    if n == 0:
        return ""
    elif n % 2 == 0 and n % 3 == 0:
        return "A"
    elif n % 2 != 0 and n > 50:
        return "B"
    else:
        return "C"

def contar(cantidad: int):
    contador_A = 0
    contador_B = 0
    contador_C = 0

    while cantidad > 0:
        n = int(input("Ingresá un número entero positivo: "))
        if n < 0:
            print("🚫 Error: Ingresá un número entero positivo.")
            continue

        clasificacion = clasificar_n(n)
        if clasificacion == "A":
            contador_A += 1
        elif clasificacion == "B":
            contador_B += 1
        elif clasificacion == "C":
            contador_C += 1

        cantidad -= 1
    
    return contador_A, contador_B, contador_C

def calcular_porcentaje(total: int, n: int) -> float:
    return (100 * n) / total

def bienvenida() -> None:
    print("⚙️ La Máquina Clasificadora de Números")
    print("---------------------------------------\n")

def mostrar_resultado(total: int, contador_A: int, contador_B: int, contador_C: int) -> None:
    if total == 0:
        print("Todos los números ingresador fueron 0.")
        return
    print(f"""\nResultado final
Tipo A: {contador_A} ({calcular_porcentaje(total, contador_A):.2f}%)
Tipo B: {contador_B} ({calcular_porcentaje(total, contador_B):.2f}%)
Tipo C: {contador_C} ({calcular_porcentaje(total, contador_C):.2f}%)
""")