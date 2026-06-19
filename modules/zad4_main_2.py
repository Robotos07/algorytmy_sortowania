import matplotlib.pyplot as plt
import file


# =====================================================
# WCZYTANIE DANYCH - A (zmienne n)
# =====================================================
points_n = list(map(int, file.read("points_n.txt")))
dp_a = list(map(float, file.read("a_dp.txt")))
greedy_a = list(map(float, file.read("a_greedy.txt")))
error_a = list(map(float, file.read("a_error.txt")))


# =====================================================
# WCZYTANIE DANYCH - B (zmienne capacity)
# =====================================================
points_b = list(map(int, file.read("points_capacity.txt")))
dp_b = list(map(float, file.read("b_dp.txt")))
greedy_b = list(map(float, file.read("b_greedy.txt")))
error_b = list(map(float, file.read("b_error.txt")))


# =====================================================
# WYKRES 1 - CZAS (A)
# =====================================================
plt.figure()
plt.plot(points_n, dp_a, label="DP")
plt.plot(points_n, greedy_a, label="Zachłanny")
plt.title("A: Stała pojemność, zmienne n - czas")
plt.xlabel("Liczba kontenerów")
plt.ylabel("Czas [s]")
plt.legend()
plt.grid()
plt.show()


# =====================================================
# WYKRES 2 - BŁĄD (A)
# =====================================================
plt.figure()
plt.plot(points_n, error_a, label="Błąd względny")
plt.title("A: Stała pojemność, zmienne n - błąd")
plt.xlabel("Liczba kontenerów")
plt.ylabel("Błąd")
plt.legend()
plt.grid()
plt.show()


# =====================================================
# WYKRES 3 - CZAS (B)
# =====================================================
plt.figure()
plt.plot(points_b, dp_b, label="DP")
plt.plot(points_b, greedy_b, label="Zachłanny")
plt.title("B: Stała liczba kontenerów, zmienne capacity - czas")
plt.xlabel("Pojemność statku")
plt.ylabel("Czas [s]")
plt.legend()
plt.grid()
plt.show()


# =====================================================
# WYKRES 4 - BŁĄD (B)
# =====================================================
plt.figure()
plt.plot(points_b, error_b, label="Błąd względny")
plt.title("B: Stała liczba kontenerów, zmienne capacity - błąd")
plt.xlabel("Pojemność statku")
plt.ylabel("Błąd")
plt.legend()
plt.grid()
plt.show()