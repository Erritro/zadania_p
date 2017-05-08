#Napisz skrypt, który generuje losowo liczbę
#całkowitą i drukuje czy ta liczba jest parzysta
#czy nieparzysta

import random
liczba = random.randint(0,100)

if(liczba%2==0):
    print("Wylosowana liczba ", liczba, "jest parzysta")
else:
    print("Wylosowana liczba ", liczba, "jest nieparzysta")
