def HolaMundo():
    print("HolaMundo()")
    print("Hola, Mundo!")
def area_del_quadrat():
    print("area_del_quadrat()")
    costat = float(input("Introdueix la longitud del costat del quadrat: "))
    area = costat * costat
    print(f"L'àrea del quadrat és: {area}")
def suma_nombres():
    print("suma_nombres()")
    num1 = float(input("Introdueix el primer nombre: "))
    num2 = float(input("Introdueix el segon nombre: "))
    suma = num1 + num2
    print(f"La suma dels nombres és: {suma}")
def frase_feta():
    print("frase_feta()")
    print ("farem una frase feta amb 3 paraules que ens donis")
    paraula1 = input ("Introdueix la primera paraula: ")
    paraula2 = input ("Introdueix la segona paraula: ")
    paraula3 = input ("Introdueix la tercera paraula: ")
    frase_feta = "Comprar 1 " + paraula1 + " més 2 " + paraula2 + " i 3 " + paraula3
    print ("La frase feta es:", frase_feta)
def major_o_menor():
    print("major_o_menor()")
    edat = int(input("Introdueix la teva edat: "))
    if edat >= 18:
        print("Ets major d'edat.")
    else:
        print("Ets menor d'edat.")
def nombres_parells():
    print("nombres_parells()")
    for x in range(1, 201):
        if x % 2 == 0:
            print(x)
def notes_estudiants():
    print("notes_estudiants()")
    Nombre_de_deus = 0
    Nota = int(input("Introdueix una nota entre 0 i 10 (-1 per acabar): "))
    while Nota != -1:
        Nota = int(input("Introdueix una nota entre 0 i 10 (-1 per acabar): "))
        if Nota == 10:
            Nombre_de_deus += 1
        if Nota == -1:
            break
    if Nombre_de_deus == 10:
        print("Hi ha hagut almenys un 10")
    else:
        print("No hi ha cap 10")
def positiu_o_negatiu():
    print("positiu_o_negatiu()")
    Nobres = [-3, -4, 1, 5, 7, 6, -5, 4, 2, 3]
    for Nombre in Nobres:
        print(Nombre)
        if Nombre < 0:
            break
    if min(Nobres) < 0:
        print("Hi ha nombres negatius")
    if min(Nobres) >= 0:
        print("No hi ha nombres negatius")
def positiu_negatiu():
    print("positiu_negatiu()")
    Nombre = input("Introdueix un nombre positiu o negatiu: ")
    if float(Nombre) > 0:
        print("El nombre és positiu.")
    elif float(Nombre) < 0:
        print("El nombre és negatiu.")
    else:
        print("El nombre és zero.")
def quin_nombre_mes_gran():
    print("quin_nombre_mes_gran()")
    num1 = float(input("Introdueix el primer nombre: "))
    num2 = float(input("Introdueix el segon nombre: "))
    if num1 > num2:
        print(f"{num1} és més gran que {num2}.")
    elif num2 > num1:
        print(f"{num2} és més gran que {num1}.")
    else:
        print("Els dos nombres són iguals.")
def calculs_basics():
    print("calculs_basics()")
    print ("Anem a sumar, restar, multiplicar i dividir dos nombres")
    nombre1 = int(input ("Introdueix el primer nombre: "))
    nombre2 = int(input ("Introdueix el segon nombre: "))
    suma = nombre1 +nombre2
    resta = nombre1 - nombre2
    multiplicació = nombre1 * nombre2
    divisió = nombre1 / nombre2
    print ("la suma es:", int(suma), "la resta es:", int(resta), "la multiplicació es:", int(multiplicació), "la divisió es:", divisió)
while True:
    print("1. Hello, World!")
    print("2. Àrea del quadrat")
    print("3. Casting nombres")
    print("4. Frase feta")
    print("5. Major o menor d'edat")
    print("6. Nombres parells de 1 a 200")
    print("7. Notes dels estudiants")
    print("8. Positiu o negatiu")
    print("9. Positiu o negatiu en la llista")
    print("a. Quin nombre és més gran?")
    print("b. Suma, Resta, Multiplicació, Divisió")
    print("S. Sortir")
    opcio = input("Que desitjes fer? ")
    match opcio:
        case "1":
            HolaMundo()
        case "2":
            area_del_quadrat()
        case "3":
            suma_nombres()
        case "4":
            frase_feta()
        case "5":
            major_o_menor()
        case "6":
            nombres_parells()
        case "7":
            notes_estudiants()
        case "8":
            positiu_negatiu()
        case "9":
            positiu_o_negatiu()
        case "a":
            quin_nombre_mes_gran()
        case "b":
            calculs_basics()
        case "S" | "s":
            print("Fins aviat!")
            break
        case _:
            print("Opció no vàlida. Si us plau, tria una opció vàlida.")