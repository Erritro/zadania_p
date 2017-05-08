#Znajdź elegancki sposób generacji macierzy
# 7 8 9 10
# 12 10 8 6
# Potem napisz wyrażenia, które dadzą:
# a) element w pierwszym wierszu i trzeciej kolumnie
# b) wszystkie elementy drugiego wiersza
# c) pierwsze dwie kolumny

wiersz1 = list(range(7,11))
wiersz2 = list(range(12,5,-2))
macierz = []

macierz.append(wiersz1)
macierz.append(wiersz2)

print("Element w pierwszym wierszu i trzeciej kolumnie: ", macierz[0][2], "\n")

print("Wszystkie elementy drugiego wiersza: ", end="")
for i in range(len(macierz[1])):
    print(macierz[1][i], end=" ")

print("\n\nPierwsze dwie kolumny: ")

print("- pierwsza kolumna: ", end ="")
for i in range(len(macierz)): #tyle ile jest wierszy
    print(macierz[i][0], end=" ")

print("\n- druga kolumna: ", end =" ")
for i in range(len(macierz)): #tyle ile jest wierszy
    print(macierz[i][1], end=" ")






