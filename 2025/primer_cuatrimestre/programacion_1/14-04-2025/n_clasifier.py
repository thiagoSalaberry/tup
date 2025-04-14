from funcs import *

def main():
    bienvenida()
    cantidad_de_n = int(input("Ingresá la cantidad de números a clasificar: "))
    
    while cantidad_de_n < 1:
        print("🚫 Error: Ingresá un número mayor que 0.")
        cantidad_de_n = int(input("Ingresá la cantidad de números a clasificar: "))
    
    contador_A, contador_B, contador_C = contar(cantidad_de_n)

    total = contador_A + contador_B + contador_C
    
    mostrar_resultado(total, contador_A, contador_B, contador_C)

main()
