import time
import file


# =====================================================
# Programowanie dynamiczne
# =====================================================
def dynamic_knapsack(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]

        for c in range(capacity + 1):
            if w <= c:
                dp[i][c] = max(
                    dp[i - 1][c],
                    dp[i - 1][c - w] + v
                )
            else:
                dp[i][c] = dp[i - 1][c]

    return dp[n][capacity], dp


# =====================================================
# Algorytm zachłanny
# =====================================================
def greedy_knapsack(weights, values, capacity):
    items = []

    for i in range(len(weights)):
        items.append((values[i] / weights[i], i))

    items.sort(reverse=True)

    total_weight = 0
    total_value = 0

    for _, i in items:
        if total_weight + weights[i] <= capacity:
            total_weight += weights[i]
            total_value += values[i]

    return total_value


# =====================================================
# Wczytanie danych
# =====================================================
n, weights_all, values_all, base_capacity = file.read("dane.txt")


# =====================================================
# A) Stała ładowność, zmienna liczba kontenerów
# =====================================================

points_n = [
    100, 200, 300, 400, 500,
    600, 700, 800, 900, 1000,
    1100, 1200, 1300, 1400, 1500
]

dp_times_A = []
greedy_times_A = []
errors_A = []

for size in points_n:

    weights = weights_all[:size]
    values = values_all[:size]

    start = time.perf_counter()
    dyn_val, dp_table = dynamic_knapsack(
        weights,
        values,
        base_capacity
    )
    dp_times_A.append(time.perf_counter() - start)

    start = time.perf_counter()
    greedy_val = greedy_knapsack(
        weights,
        values,
        base_capacity
    )
    greedy_times_A.append(time.perf_counter() - start)

    error = (
        (dyn_val - greedy_val) / dyn_val
        if dyn_val != 0 else 0
    )

    errors_A.append(error)


# =====================================================
# B) Zmienna ładowność, stała liczba kontenerów
# =====================================================

fixed_n = 1000

points_capacity = [
    100, 200, 300, 400, 500,
    600, 700, 800, 900, 1000,
    1100, 1200, 1300, 1400, 1500
]

dp_times_B = []
greedy_times_B = []
errors_B = []

weights = weights_all[:fixed_n]
values = values_all[:fixed_n]

for capacity in points_capacity:

    start = time.perf_counter()
    dyn_val, _ = dynamic_knapsack(
        weights,
        values,
        capacity
    )
    dp_times_B.append(time.perf_counter() - start)

    start = time.perf_counter()
    greedy_val = greedy_knapsack(
        weights,
        values,
        capacity
    )
    greedy_times_B.append(time.perf_counter() - start)

    error = (
        (dyn_val - greedy_val) / dyn_val
        if dyn_val != 0 else 0
    )

    errors_B.append(error)


# =====================================================
# Zapis wyników
# =====================================================

file.write_list("points_A.txt", points_n)
file.write_list("dp_times_A.txt", dp_times_A)
file.write_list("greedy_times_A.txt", greedy_times_A)
file.write_list("errors_A.txt", errors_A)

file.write_list("points_B.txt", points_capacity)
file.write_list("dp_times_B.txt", dp_times_B)
file.write_list("greedy_times_B.txt", greedy_times_B)
file.write_list("errors_B.txt", errors_B)


# =====================================================
# Wyświetlenie tabeli DP
# =====================================================

print("TABELA WARTOŚCI POŚREDNICH (ostatni pomiar z eksperymentu A):\n")

for row in dp_table:
    print(row)