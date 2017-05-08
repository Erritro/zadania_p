# Napisz funkcję, która pobiera
# macierz i oblicza średnią wszystkich
# jej elementów

wiersze = int(input("Podaj liczbę wierszy macierzy: \n"))
macierz = []

def srednia(macierz):

    lista = []  #lista to macierz spłaszczona do 1 wymiaru  
    
    for wiersz in range(len(macierz)):
        for kolumna in range(len(macierz[wiersz])):
            
            lista.append(macierz[wiersz][kolumna])
            

    return sum(lista)/len(lista)

for i in range(wiersze):
    w = input("Podaj elementy " + str(i+1) + " wiersza oddzielone spacją: ")
    w = w.split(" ")
    w = [int(i) for i in w] # zmieniam elementy na str
    macierz.append(w) # dodaję całą liste jako pierwszy wiersz
    

print("Średnia wszystkich elementów macierzy: ", srednia(macierz))


        



