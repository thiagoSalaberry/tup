for piso in range(1, 5):
    if piso == 1:
        pregunta = "¿Febrero siempre tiene los mismos días? Respondé V o F"
        respuesta_correcta = "f"
    elif piso == 2:
        pregunta = "¿Estamos en clase de inglés? Respondé V o F"
        respuesta_correcta = "f"
    elif piso == 3:
        pregunta = "¿Hoy es viernes? Respondé V o F"
        respuesta_correcta = "v"
    elif piso == 4:
        pregunta = "¿Es Lionel Messi un poeta argentino? Respondé V o F"
        respuesta_correcta = "f"
    print(f"Piso {piso}")
    print(pregunta)
    while True:
        respuesta = input().lower()
        if respuesta == respuesta_correcta:
            print("✅ Correcto, siguiente pregunta.\n")
            break
        else:
            print("❌ Respuesta incorrecta. Intentá de nuevo.")

print("¡🎉 Felicitaciones, sos el amo supremo del conocimiento 🧙‍♂️!")