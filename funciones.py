# Archivo con todas las funciones para las operaciones con DNIs y años de nacimiento
from datetime import date  # Date para obtener la fecha actual y calcular edades


# A. Operaciones con DNIs
def analizar_dni_individual(dni, conjunto):
    """Función para analizar el DNI: mostrar conjunto de dígitos únicos, suma total de dígitos y frecuencia."""
    print("\nAnálisis del DNI ingresado:")

    # Mostrar el conjunto de dígitos únicos del DNI ingresado
    print(f"• Conjunto de dígitos únicos del DNI: {sorted(conjunto)}")

    # Suma total de dígitos
    suma_digitos = sum(int(d) for d in dni)
    print(f"• Suma total de dígitos: {suma_digitos}")

    # Frecuencia
    print("• Frecuencia de cada dígito:")
    for digito in sorted(conjunto):
        frecuencia = dni.count(digito)
        veces = "vez" if frecuencia == 1 else "veces"
        print(f" - Dígito {digito}: {frecuencia} {veces}")


def obtener_dni():
    """Función principal para manejar operaciones con DNIs y conjuntos de dígitos."""
    dnis = []
    conjuntos = []

    # Mensajes iniciales
    print("Ingrese entre 2 y 5 DNIs (7-8 dígitos cada uno).")

    while len(dnis) < 5:
        dni_input = input(f"\nDNI #{len(dnis) + 1}: ")

        # Validación de DNI
        if not dni_input.isdigit() or not 7 <= len(dni_input) <= 8:
            print("ERROR: DNI inválido. Ingrese solo números, de 7-8 dígitos.")
            continue

        # Agregar DNI válido
        dni = int(dni_input)
        dnis.append(dni)
        conjunto = set(dni_input)
        conjuntos.append(conjunto)

        # Analizar el DNI individual
        analizar_dni_individual(dni_input, conjunto)

        # Verificar si se alcanzó el máximo de DNIs
        if len(dnis) == 5:
            print("\nSe alcanzó el máximo de 5 DNIs.")
            break

        if len(dnis) >= 2:
            continuar = input("\n¿Desea ingresar otro DNI? (s/n): ").lower()
            while continuar not in ["s", "si", "n", "no"]:
                continuar = input("\nOpción no válida. Ingrese 's/si' o 'n/no': ").lower()
            if continuar in ["n", "no"]:
                print("\nFinalizando ingreso de DNIs...")
                break

    return dnis, conjuntos


def operaciones_dnis(dnis, conjuntos):
    """Función para realizar operaciones entre dos DNIs seleccionados."""
    if len(dnis) == 2:
        # Si hay exactamente 2 DNIs, se usan directamente
        set1, set2 = conjuntos[0], conjuntos[1]
        print(f"\nConjunto A (DNI:{dnis[0]}): {sorted(set1)}")
        print(f"Conjunto B (DNI:{dnis[1]}): {sorted(set2)}")
    else:
        # Permite elegir 2 DNIs entre varios
        print("Para realizar operaciones, elija dos DNIs de la lista:")
        for i, dni in enumerate(dnis):
            print(f"{i + 1}. DNI {dni}")

        while True:
            op1 = input("\nNúmero del primer DNI: ")
            op2 = input("Número del segundo DNI: ")

            if (op1.isdigit() and op2.isdigit() and
                1 <= int(op1) <= len(dnis) and
                1 <= int(op2) <= len(dnis) and
                op1 != op2):
                i1 = int(op1) - 1
                i2 = int(op2) - 1
                set1, set2 = conjuntos[i1], conjuntos[i2]
                print(f"\n------------ Seleccionaste el DNI {dnis[i1]} y el DNI {dnis[i2]} ------------")
                print(f"Conjunto A (DNI:{dnis[i1]}): {sorted(set1)}")
                print(f"Conjunto B (DNI:{dnis[i2]}): {sorted(set2)}")
                break
            else:
                print("Selección inválida, elige dos números distintos y válidos. Intente nuevamente.")

    # Operaciones básicas entre dos conjuntos
    print(f"\n • Unión (A ∪ B): {sorted(set1.union(set2))}")
    print(f" • Intersección (A ∩ B): {sorted(set1.intersection(set2))}")
    print(f" • Diferencia (A - B): {sorted(set1.difference(set2))}")
    print(f" • Diferencia (B - A): {sorted(set2.difference(set1))}")
    print(f" • Diferencia simétrica (A △ B): {sorted(set1.symmetric_difference(set2))}")


def expresiones_logicas_dnis(conjuntos):
    # Expresiones lógicas entre todos los conjuntos
    print("\n------------ Expresiones lógicas de todos los DNIs ------------")

    # Diversidad numérica alta
    diversidad_numerica_alta = True
    for conjunto in conjuntos:
        if len(conjunto) < 5:
            diversidad_numerica_alta = False
            break

    if diversidad_numerica_alta:
        print("✓ Diversidad numérica alta: Todos los DNIs tienen 5 o más dígitos únicos")

    # Grupos sin ceros
    grupo_sin_cero = True
    for conjunto in conjuntos:
        if "0" in conjunto:
            grupo_sin_cero = False
            break

    if grupo_sin_cero:
        print("✓ Grupo sin ceros: Ningún DNI contiene el dígito 0")

    # Evaluar si algún dígito aparece en todos los conjuntos, marcar como dígito común 
    digitos_comunes = set.intersection(*conjuntos)
    if digitos_comunes:
        print(f"• Dígito(s) común(es) en todos los DNIs: {sorted(digitos_comunes)}")

    # Dígito representativo: intersección exacta entre todos con un solo elemento
    interseccion_total = set.intersection(*conjuntos)
    if len(interseccion_total) == 1:
        print(f"• Dígito representativo del grupo: {list(interseccion_total)[0]}")
    elif len(interseccion_total) > 1:
        print(f"• Hay múltiples dígitos comunes, no hay uno representativo: {sorted(interseccion_total)}")
    else:
        print("✗ No hay ningún dígito común en todos los DNIs.")

    # Evaluar si hay más conjuntos con cantidad par de elementos que con cantidad impar
    pares = 0
    impares = 0
    for conjunto in conjuntos:
        if len(conjunto) % 2 == 0:
            pares += 1
        else:
            impares += 1

    if pares > impares:
        print("✓ Grupo par: Hay más conjuntos con cantidad par de elementos que impares.")
    elif impares > pares:
        print("✓ Grupo impar: Hay más conjuntos con cantidad impar de elementos que pares.")
    else:
        print("= Grupos equilibrados: Hay igual cantidad de conjuntos pares e impares.")


def dni_conjuntos():
    """Funcion principal para manejar todas las operaciones con DNIs."""
    # Ingreso de los DNIs
    dnis, conjuntos = obtener_dni()

    # Realizar operaciones entre conjuntos
    print("\n" + "="*50)
    print("OPERACIONES ENTRE CONJUNTOS")
    print("="*50)

    # Operaciones con DNIs
    operaciones_dnis(dnis, conjuntos)

    # Expresiones lógicas entre los conjuntos de DNIs
    expresiones_logicas_dnis(conjuntos)



# B. Operaciones con años de nacimiento
def obtener_anios_nacimiento():
    """Función para obtener hasta 5 años de nacimiento válidos."""
    anios = []
    cant_de_anios = input("¿Cuántos años desea ingresar? (máximo 5): ")

    # Validación de la cantidad de años
    if not cant_de_anios.isdigit() or not 1 <= int(cant_de_anios) <= 5:
        print("Número inválido. Se usarán 5 años por defecto.")
        cant_de_anios = 5
    else:
        cant_de_anios = int(cant_de_anios)

    print(f"\nIngrese {cant_de_anios} años de nacimiento: ")

    # Bucle para ingresar los años de nacimiento
    while len(anios) < cant_de_anios:
        try:
            anio = int(input(f"Año #{len(anios)+1}/{cant_de_anios} (entre 1900 y 2025): "))
            
            if 1900 <= anio <= 2025:  # Validación básica del rango
                anios.append(anio)
            else:
                print("Por favor ingrese un año válido (entre 1900 y 2025).")
        except ValueError:
            print("Por favor ingrese un número válido.")

    print(f"\nAños ingresados: {anios}")
    return anios


def contar_pares_impares(anios):
    """Función para contar años pares e impares."""
    pares = 0
    impares = 0

    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    return pares, impares


def verificar_grupo_z(anios):
    """Función para verificar si todos los años son posteriores a 2000 (Grupo Z)."""
    if all(anio > 2000 for anio in anios):
        print("✓ Grupo Z: Todos nacieron después del año 2000")
        return True
    else:
        print("✗ No es Grupo Z: No todos nacieron después del año 2000")
        return False


def es_bisiesto(anio):
    """Función para verificar si un año es bisiesto."""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def verificar_anios_bisiestos(anios):
    """Función para verificar si hay años bisiestos en la lista."""
    anios_bisiestos = []

    for anio in anios:
        if es_bisiesto(anio):
            anios_bisiestos.append(anio)

    if anios_bisiestos:
        print(f"✓ Años bisiestos encontrados: {anios_bisiestos}")
        return anios_bisiestos
    else:
        print("✗ No hay años bisiestos en la lista")
        return []


def calcular_edades(anios):
    """Función que calcula las edades actuales en base al año."""
    edad_actual = date.today().year
    return [edad_actual - anio for anio in anios]


def producto_cartesiano(lista1, lista2):
    """Función para calcular el producto cartesiano entre dos listas."""
    producto = []

    for elemento1 in lista1:
        for elemento2 in lista2:
            producto.append((elemento1, elemento2))

    return producto


def operaciones_anios_nacimiento():
    """Función principal para manejar todas las operaciones con años de nacimiento."""
    print("\n" + "="*50)
    print("OPERACIONES CON AÑOS DE NACIMIENTO")
    print("="*50)

    # a. Ingreso de los años de nacimiento
    anios = obtener_anios_nacimiento()

    # b. Imprimir pares e impares
    print("\n--- Análisis de paridad ---")
    contar_pares_impares(anios)

    # c. Verificar Grupo Z
    print("\n--- Verificación Grupo Z ---")
    verificar_grupo_z(anios)

    # d. Verificar años bisiestos
    print("\n--- Verificación años bisiestos ---")
    verificar_anios_bisiestos(anios)

    # e. Calcular el producto cartesiano entre años y edades
    print("\n--- Cálculo de edades y producto cartesiano ---")
    edades = calcular_edades(anios)
    print(f"Edades calculadas: {edades}")

    producto = producto_cartesiano(anios, edades)
    print(f"\nProducto cartesiano (Años × Edades): {len(producto)} combinaciones")

    # Mostrar algunas combinaciones como ejemplo
    print("Primeras 10 combinaciones:")
    for i, (a, e) in enumerate(producto[:10], 1):
        print(f"  {i}. Año {a} - Edad {e}")
    if len(producto) > 10:
        print("  ...")
