# Ingresar dni
def dni_conjunto():
    while True:
        dni = int(input("Ingrese su DNI: "))
        while dni < 1000000 or len(str(dni)) > 8:
            print("DNI Invalido. Intente nuevamente.")
            dni = int(input("Ingrese su DNI: "))

        print(f"\nDNI ingresado: {dni}")
        print(f"Conjunto de dígitos del DNI: {sorted(set(str(dni)))}")

        continuar = input("\n¿Desea ingresar otro DNI? (s/n): ").lower()
        if continuar not in ["s", "si"]:
            break

dni_conjunto()
        
        
