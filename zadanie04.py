#Wygeneruj liczby losowe
# a) liczbę rzeczywistą z przedziału (0,1)
# b) liczbę rzeczywistą z przedziału (0,20)
# c) liczbę rzeczywistą z przedziału (20,50)
# d) liczbę całkowitą z przedziału (0,10)
# e) liczbę całkowitą z przedziału (0,11)
# f) liczbę całkowitą z przedziału (50,100)
# Zbuduj dwa n-elementowe wektory 

import random
import matplotlib.pyplot as plt

print("Liczba rzeczywista z przedziału (0,1): ", random.random())
print("Liczba rzeczywista z przedziału (0,20): ", random.uniform(0,20))
print("Liczba rzeczywista z przedziału (0,20): ", random.uniform(0,20))
print("Liczba rzeczywista z przedziału (20,50): ", random.uniform(20,50))
print("Liczba całkowita z przedziału (0,10): ", random.randint(0,11))
print("Liczba całkowita z przedziału (0,11): ", random.randint(0,12))
print("Liczba całkowita z przedziału (50,101): ", random.randint(50,101))

dlugosc_wektorow = int(input("Podaj długość wektorów (n): "))
                       
wektor1 =[]
wektor2 =[]

for element in range(dlugosc_wektorow):
    wektor1.append(random.randint(50,101))
    wektor2.append(random.randint(50,101))

plt.title('Współrzędne losowych punktów na płaszczyźnie')
plt.scatter(wektor1, wektor2)
plt.show()


