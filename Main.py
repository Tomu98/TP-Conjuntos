from funciones import dni_conjuntos, operaciones_anios_nacimiento


def mostrar_menu():
    """Muestra el menú principal del programa."""
    # Separa las opciones del menú
    print("\n" + "="*60)
    print("PROGRAMA DE OPERACIONES CON DNIs Y AÑOS DE NACIMIENTO")
    # Separa las opciones del menú
    print("="*60)
    print("Seleccione una opción:")
    print("A. Operaciones con DNIs")
    print("B. Operaciones con años de nacimiento")
    print("C. Ejecutar ambas operaciones")
    print("S. Salir")
    # Separa las opciones del menú
    print("-" * 60)



def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()

        opcion = input("Ingrese su opción (A/B/C/S): ").upper().strip()

        if opcion == 'A':
            print("\n" + "="*50)
            print("OPERACIONES CON DNIs")
            print("="*50)
            dni_conjuntos()

        elif opcion == 'B':
            operaciones_anios_nacimiento()

        elif opcion == 'C':
            # Separa las opciones del menú
            print("\n" + "="*50)
            print("OPERACIONES CON DNIs")
            # Separa las opciones del menú
            print("="*50)
            dni_conjuntos()
            operaciones_anios_nacimiento()

        elif opcion == 'S':
            print("\nGracias por usar el programa. ¡Hasta luego!.\n")
            break

        else:
            print("\nOpción no válida. Por favor seleccione A, B, C o S.")

        # Pausa antes de mostrar el menú nuevamente
        if opcion in ['A', 'B', 'C']:
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
