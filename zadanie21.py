#Napisz funkcje sumkrok2, która oblicza sumę
#liczb od 1 do n z krokiem 2, gdzie n
#jest argumentem funkcji


def sumkrok2(n):

    suma = 0
    
    for liczba in range(1,n,2):
        print(liczba,"\n")
        suma += liczba

    return suma


granica = int(input("Podaj górną granicę: "))

print(sumkrok2(granica))

