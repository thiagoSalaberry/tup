def validar_ingrediente(ing, mls):
    """
    Valida que los mililitros del ingrediente ingresado esté en el rango correcto.
    Args: 
        ing: str => Ingrediente (A, B ó C)
        mls: float => Militros ingresados
    Retorna:
        True si el rango es correcto, False caso contrario
    """
    if ing.lower() == "a":
        return 5 <= mls <= 10
    elif ing.lower() == "b":
        return 15 <= mls <= 20
    elif ing.lower() == "c":
        return 25 <= mls <= 30
    else:
        print("¡¡Ese ingrediente no iba!! 💥 BOOM 💥")
        return False

def intentar_experimento(ing1, ing2, ing3):
    """
    Verifica que todos los ingredientes estén en el rango correcto.
    Args: 
        ing1: float => Ingrediente A
        ing2: float => Ingrediente B
        ing3: float => Ingrediente C
    Retorna:
        True si los 3 ingredientes están en rango, False caso contrario
    """
    a_en_rango = validar_ingrediente("A", ing1)
    b_en_rango = validar_ingrediente("B", ing2)
    c_en_rango = validar_ingrediente("C", ing3)

    return a_en_rango and b_en_rango and c_en_rango

def main():
    """
    La función principal del desafío. 
    Imprime un mensaje
    Pide las cantidades al usuario hasta 3 veces:
        Si los rangos ingresados son incorrectos, se pasa al siguiente intento
        Si el jugador se queda sin intentos, se avisa al usuario y el programa termina
        Si el jugador acierta en las cantidades en algún intento, se felicita al jugador y se termina el programa
    """
    print("Desafío 1 Thiago Salaberry\n🧪 El Laboratorio del Doctor Código 🧪\n")

    for intento in range(3):
        print(f"Intento {intento + 1}")
        ing_A = float(input("Ingresá la cantidad en mililitros del ingrediente A: "))
        ing_B = float(input("Ingresá la cantidad en mililitros del ingrediente B: "))
        ing_C = float(input("Ingresá la cantidad en mililitros del ingrediente C: "))

        resultado_exitoso = intentar_experimento(ing_A, ing_B, ing_C)
        if resultado_exitoso:
            print("\n¡Excelente cerebrito 🥸 ! El experimento fue exitoso 🎉!")
            return
        else:
            print("❌ Error: Las cantidades son incorrectas. 💥 BOOM 💥\n")
    print("- Doctor Código: Nos quedamos sin intentos. Mejor contrato a otra persona 😞.\nGAME OVER")

main()