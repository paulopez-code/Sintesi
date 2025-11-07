# Aquesta linia crea una llista buida per guardar les notes
Notes = []
Nota = int(input("Introdueix una nota entre 0 i 10 (-1 per acabar): "))
while Nota != -1:
    Notes.append(Nota)
    Nota = int(input("Introdueix una nota entre 0 i 10 (-1 per acabar): "))
    # Aquestes linies comproven si la nota es -1 per aturar el bucle
    if Nota == -1:
        break
# Aquestes linies comproven si hi ha hagut alguna nota que te un 10
if max(Notes) == 10:
    print("Hi ha hagut alguna nota que te un 10")
else:
    print("No hi ha cap 10")