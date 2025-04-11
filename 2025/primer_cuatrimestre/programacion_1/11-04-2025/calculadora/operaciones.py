def sumar(a: float, b: float) -> float:
    return a + b

def restar(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividr(a: float, b: float) -> float:
    if b == 0:
        print("❌ Error: No se puede dividir por 0.")
        return
    return a / b