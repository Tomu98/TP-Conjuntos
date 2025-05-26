#Parte 2 – Desarrollo del Programa en Python
# A. Operaciones con DNIs

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


        
        
