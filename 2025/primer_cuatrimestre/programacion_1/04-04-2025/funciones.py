def calcular_edad(anio_actual, anio_nacimiento):
    return anio_actual - anio_nacimiento

anio_actual = int(input("Ingresá el año actual: "))
anio_usuario = int(input("Ingresá tu año de nacimiento: "))
edad = calcular_edad(anio_actual, anio_usuario)

print(f"Tenés entre {edad - 1} y {edad} años.")