#Utwórz macierz (3x5) losowych liczb rzeczywistych.
#Usuń jej trzeci wiersz.

import random

macierz = []
wiersz = []

for wiersze in range(3):
    
    for kolumny in range(5):
        wiersz.append(random.uniform(1,10))
        
    macierz.append(wiersz)
    wiersz =[]
    
print("Macierz tabelarycznie")

for wiersz in range(3):
    for kolumny in range(5):
        print(macierz[wiersz][kolumny], "\t", end ="")
    print("\n", end="")


print("\n")

del macierz[2]
print(macierz, "\n")


print("Macierz tabelarycznie po usunięciu trzeciego wiersza\n")


for wiersz in range(2):
    for kolumny in range(5):
        print(macierz[wiersz][kolumny], "\t", end ="")
    print("\n", end="")





