# Aquesta linia crea una llista amb uns nombres enters
Nobres = [-3, -4, 1, 5, 7, 6, -5, 4, 2, 3]
# Aquestes linies imprimiran els nombres i comprovaran si hi ha algun nombre negatiu
for Nombre in Nobres:
    print(Nombre)
    if Nombre < 0:
        break
if min(Nobres) < 0:
    print("Hi ha nombres negatius")
if min(Nobres) >= 0:
    print("No hi ha nombres negatius")