from operaciones import *
def main() -> None:
    print("""Bienvenido a la calculadora. Elegí una operación a realizar.
          
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
          
""")
    
    while True:
        eleccion = input("Ingresá la operación a realizar (de 1 a 4): ")
        if eleccion == "salir":
            print("👋 Hasta la próxima.")
            return
        
        if eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4":
            print("🚫 Operación inválida, intentá de nuevo.\n")
            continue

        num_a = float(input("Ingresá el primer número: "))
        num_b = float(input("Ingresá el segundo número: "))

        if eleccion == "1":
            result = sumar(num_a, num_b)
            print(f"La suma de {num_a} + {num_b} es: {result}\n")
        elif eleccion == "2":
            result = restar(num_a, num_b)
            print(f"La resta de {num_a} - {num_b} es: {result}\n")
        elif eleccion == "3":
            result = multiplicar(num_a, num_b)
            print(f"La multiplicación de {num_a} * {num_b} es: {result}\n")
        elif eleccion == "4":
            result = dividr(num_a, num_b)
            print(f"La división de {num_a} / {num_b} es: {result}\n")
            


main()