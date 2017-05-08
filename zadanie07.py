#Utwórz macierz (4x2), zawierającą zera
#i przypisz ją do zmiennej.
#Potem zastąp jej drugi wiersz przez 3 i 6

macierz = []
wiersz = []

for wiersze in range(4):
    
    for kolumny in range(2):
        wiersz.append(0)
        
    macierz.append(wiersz)
    wiersz =[]
    
print("\nMacierz przed zastąpieniem: ", macierz, "\n")
print("Macierz przed zastąpieniem tabelarycznie")

for wiersz in range(4):
    for kolumny in range(2):
        print(macierz[wiersz][kolumny], "\t", end ="")
    print("\n", end="")   

zamiana = [3,6]

for i in range(2):
    macierz[1][i]=zamiana[i]

print("\nMacierz po zastąpieniu: ", macierz, "\n")
print("Macierz po zastąpieniu tabelarycznie")

for wiersz in range(4):
    for kolumny in range(2):
        print(macierz[wiersz][kolumny], "\t", end ="")
    print("\n", end="") 






