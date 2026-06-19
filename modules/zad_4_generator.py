import random
import file

# Maksymalna liczba kontenerów
n = 1500

# Bazowa ładowność (wykorzystywana w eksperymencie A)
capacity = 100

# Losowanie ciężarów i wartości kontenerów
weights = [random.randint(1, 100) for _ in range(n)]
values = [random.randint(1, 100) for _ in range(n)]

# Zapis do pliku
file.write("dane.txt", n, weights, values, capacity)

print("Dane zapisane do dane.txt")