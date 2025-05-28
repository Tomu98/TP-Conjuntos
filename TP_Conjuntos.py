#Parte 2 – Desarrollo del Programa en Python
# A. Operaciones con DNIs

# (Cree esta función para no complicar mucho la otra función `dni_conjuntos` y que sea más comodo cambiar cosas)
def analizar_dni_individual(dni, conjunto):
    """Función para analizar un DNI: la suma, frecuencias y diversidad de sus dígitos."""

    # Suma total de dígitos
    # (Me imagino que se refiere a la suma de los todos los dígitos del DNI)
    suma_digitos = sum(int(d) for d in dni)
    print(f"Suma total de dígitos: {suma_digitos}")

    # Frecuencia
    print("Frecuencia de cada dígito:")
    for digito in sorted(conjunto):
        frecuencia = dni.count(digito)
        if frecuencia > 1:
            print(f" • Dígito {digito}: {frecuencia} veces")
        else:
            print(f" • Dígito {digito}: {frecuencia} vez")
    
    # Diversidad numérica alta
    # (Podriamos colocarlo en la información de una mejor manera...)
    if len(conjunto) > 6:
        print("-> Diversidad numérica alta") # Acá no sé si quieren que se ponga más opciones, como "frecuencia baja/media".



def dni_conjuntos():
    dnis = []
    conjuntos = []

    # Mensajes iniciales
    # (Los mensajes iniciales y de todo el programa lo podría mejorar más...)
    print("\nIngrese entre 2 y 5 DNIs (7-8 dígitos cada uno)")

    while len(dnis) < 5:
        dni_input = input(f"\nDNI #{len(dnis) + 1}: ")

        if not dni_input.isdigit() or len(dni_input) < 7 or len(dni_input) > 8:
            print("ERROR: DNI inválido. Ingrese solo números, de 7-8 dígitos.")
            continue

        # Agregar DNI válido
        dni = int(dni_input)
        dnis.append(dni)
        conjunto = set(dni_input)
        conjuntos.append(conjunto)
        
        # Mostrar el conjunto de dígitos únicos del DNI ingresado
        print(f"Conjunto de dígitos únicos del DNI: {sorted(conjunto)}\n")

        # Analizar el DNI individual
        analizar_dni_individual(dni_input, conjunto)

        # Verificar si se alcanzó el máximo de DNIs
        if len(dnis) == 5:
            print("\nSe alcanzó el máximo de 5 DNIs.")
            break

        if len(dnis) >= 2:
            while True:
                continuar = input("\n¿Desea ingresar otro DNI? (s/n): ").lower()
                if continuar in ["s", "si"]:
                    break
                elif continuar in ["n", "no"]:
                    print("\nFinalizando ingreso de DNIs...")
                    break
                else:
                    print("Opción no válida. Ingrese 's/si' o 'n/no'.")

            if continuar in ["n", "no"]:
                break

    # Operaciones entre conjuntos de dígitos
    # (No sé si es mejor separar esta parte en otra función, cualquier cosa vemos luego)
    # (No me convence aún la claridad de los mensajes de las operaciones, lo podría mejorar)
    # (Otra cosa es que los conjuntos salen como listas, osea con "[]", no sé si está bien o no importa)
    print("\n------------ Operaciones entre conjuntos ------------")

    if len(dnis) == 2:
        print(f"Conjunto A (DNI:{dnis[0]}): {sorted(conjuntos[0])}")
        print(f"Conjunto B (DNI:{dnis[1]}): {sorted(conjuntos[1])}")
        set1, set2 = conjuntos[0], conjuntos[1]
    else:
        # En caso de más de 2 DNIs, se seleccionan dos DNIs para operar
        # (No sé si se complica mucho poner esta opción, pero lo dejo así por ahora)
        # (Cualquier cosa lo charlamos luego sobre como hacer en caso de que se ingresen más de 2 DNIs)
        print("\nLista de DNIs ingresados:")
        for i, dni in enumerate(dnis):
            print(f"{i + 1}. {dni}")

        while True:
            op1 = input("\nSeleccione el número del primer DNI: ")
            op2 = input("Seleccione el número del segundo DNI: ")

            if (op1.isdigit() and op2.isdigit() and
                1 <= int(op1) <= len(dnis) and
                1 <= int(op2) <= len(dnis) and
                op1 != op2):
                i1 = int(op1) - 1
                i2 = int(op2) - 1
                set1, set2 = conjuntos[i1], conjuntos[i2]
                print(f"\nSeleccionaste DNI {dnis[i1]} y DNI {dnis[i2]}")
                print(f"Conjunto A (DNI:{dnis[i1]}): {sorted(set1)}")
                print(f"Conjunto B (DNI:{dnis[i2]}): {sorted(set2)}")
                break
            else:
                print("Selección inválida. Intente nuevamente eligiendo dos números distintos y válidos.")

    # Operaciones entre los dos conjuntos seleccionados
    print(f"\n • Unión (A ∪ B): {sorted(set1.union(set2))}")
    print(f" • Intersección (A ∩ B): {sorted(set1.intersection(set2))}")
    print(f" • Diferencia (A - B): {sorted(set1.difference(set2))}")
    print(f" • Diferencia (B - A): {sorted(set2.difference(set1))}")
    print(f" • Diferencia simétrica (A △ B): {sorted(set1.symmetric_difference(set2))}")

    # Mensajes finales
    print("\nGracias por usar el programa. ¡Hasta luego!.\n")

dni_conjuntos()






# B. Operaciones con años de nacimiento
#a. Ingreso de los años de nacimiento
def anio_nacimiento():
    anios = []
    #bucle para obtener los 5 inputs
    for i in range (5):
        anio= int(input("Ingresá un año de nacimiento: "))
        anios.append(anio) #Agregamos cada año a la lista
    print("Años ingresados:", anios)
    return anios #devuelve la lista con los resultados

anios=anio_nacimiento() #lo que ejecuta la función se guarda en la variable anios 

#b. Imprimir pares e impares 
pares=0
impares=0
for anio in anios:
    if anio %2==0: pares+=1
    else: impares+=1
print(f"Pares: {pares} Impares: {impares}")

#c. Imprimir Grupo Z si todos somos > 2000
if all(anio>2000 for anio in anios): #se pueden poner bucles dentro de condicionales :O. All asegura que todos los elementos de la lista sean > 2000
    print("Grupo Z")

#d. Año bisiestro = tiene que ser divisible por 4 y NO ser divisible por 100, salvo que también sea divisible por 400. 
def bisiestro(anios):
    for anio in anios:
        if(anio%4==0 and anio%100!=0 or  anio%400==0): #si es divisible por 400 también lo es por 4 y por 100.
            print("Tenemos un año especial")
            break #para que no imprima varias veces si hay más de un año bisiesto
bisiestro(anio)

#e. Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.
edades= []
for edades in anios:
    edades.append(2025-edades)
print(edades)

#calcular el producto cartesiano: todas las combinaciones posibles entre los años y las edades -> para eso necesito dos bucles anidados
producto_cartesiano = []
for anio in anios: #recorremos años para combinar con todas las edades 
    for edad in edades:
        producto_cartesiano.append((anio, edad))
print("Producto cartesiano:", producto_cartesiano)

