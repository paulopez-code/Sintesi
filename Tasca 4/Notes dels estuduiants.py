# Aquesta linia crea una llista amb les notes d'uns alumnes
Notes = [1, 0, 6, 10, 8, 7, 5, -1, 9, 3, 2, 4]
for Nota in Notes:
    # Aquestes linies imprimiran les notes i comprovaran si hi ha algun 10
    if Nota > -1:
        print(Nota)
    # Aquestes linies comproven si la nota es -1 per aturar el bucle
    if Nota == -1:
        print(Nota)
        break
# Aquestes linies comproven si hi ha hagut alguna nota que te un 10
if max(Notes) == 10:
    print("Hi ha hagut alguna nota que te un 10")
else:
    print("No hi ha cap 10")