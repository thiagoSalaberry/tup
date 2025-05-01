import matrices as Mtzs
import utilidades as Utils


def main() -> None:
    nombres_cols = ["#", "Nombre", "Apellido", "Edad", "Posición", "Goles"]

    mtz = None
    while True:
        Utils.mostrar_menu()

        eleccion = int(input("Ingresá la opción deseada: "))
        if eleccion == 4:
            print("👋 Hasta la próxima.")
            exit(0)

        if eleccion == 1:
            mtz = Mtzs.inicializar_mtz(5, 11)
            mtz = Mtzs.cargar_mtz(mtz, nombres_cols)
        elif eleccion == 2:
            if mtz is None:
                print("❌ Error: primero hay que cargar la matriz antes de mostrarla.\n")
                continue
            Mtzs.mostrar_mtz(mtz, nombres_cols)
        elif eleccion == 3:
            if mtz is None:
                print(
                    "❌ Error: primero hay que cargar la matriz antes de modificarla.\n")
                continue
            mtz = Mtzs.mod_mtz(mtz, nombres_cols)
            Mtzs.mostrar_mtz(mtz, nombres_cols)
        else:
            print("❌ Error: opción inválida. Elegí una opción del 1 al 4.\n")
            continue


main()
