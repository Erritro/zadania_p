#Uzywajac możliwości Pythona utwórz następujące wektory
# a) 3, 4, 5, 6
# b) 1.0000, 1.5000, 2.0000, 2.5000, 3.0000
# c) 5, 4, 3, 2

wektor_a =[3, 4, 5, 6]
wektor_b =[1.0000, 1.5000, 2.0000, 2.5000, 3.0000]
wektor_c =[5, 4, 3, 2]

print("Średnia [3, 4, 5, 6]: ", sum(wektor_a)/len(wektor_a))
print("Średnia [1.0000, 1.5000, 2.0000, 2.5000, 3.0000]: ", sum(wektor_b)/len(wektor_b))
print("Średnia [5, 4, 3, 2]: ", sum(wektor_c)/len(wektor_c))

# średnie z odpowiednim formatowaniem
print("\n")

print("Średnia [3, 4, 5, 6]: {0:1.2f}".format(sum(wektor_a)/len(wektor_a)))
print("Średnia [1.0000, 1.5000, 2.0000, 2.5000, 3.0000]: {0:1.4f}".format(sum(wektor_b)/len(wektor_b)))
print("Średnia [5, 4, 3, 2]: {0:1.2f}".format(sum(wektor_c)/len(wektor_c)))





