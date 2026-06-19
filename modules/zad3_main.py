import time
import sys
sys.setrecursionlimit(100000)


# =========================
# Wczytywanie grafu
# =========================
def load_graph(filename):
    with open(filename, "r") as f:
        n = int(f.readline())
        matrix = [list(map(int, f.readline().split())) for _ in range(n)]
    return matrix


# =========================
# CYKL EULERA (DFS)
# =========================
def euler(v, graph, used_edges, cycle):
    for w in range(len(graph)):
        if graph[v][w] == 1 and not used_edges[v][w]:
            used_edges[v][w] = used_edges[w][v] = True
            euler(w, graph, used_edges, cycle)
    cycle.append(v + 1)


def run_euler(graph):
    n = len(graph)
    used = [[False] * n for _ in range(n)]
    cycle = []
    euler(0, graph, used, cycle)
    return cycle[::-1]


# =========================
# CYKL HAMILTONA (backtracking)
# =========================
def hamilton(v, graph, visited, path, result):
    n = len(graph)

    if len(path) == n:
        if graph[v][path[0]] == 1:
            result.append(path[:] + [path[0]])
            return True
        return False

    for w in range(n):
        if graph[v][w] == 1 and not visited[w]:
            visited[w] = True
            path.append(w)

            if hamilton(w, graph, visited, path, result):
                return True

            path.pop()
            visited[w] = False

    return False


def run_hamilton(graph):
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    result = []
    hamilton(0, graph, visited, [0], result)
    return result[0] if result else []


# =========================
# POMIARY
# =========================
def measure(graph):
    start = time.time()
    euler_cycle = run_euler(graph)
    t1 = time.time() - start

    start = time.time()
    hamilton_cycle = run_hamilton(graph)
    t2 = time.time() - start

    return t1, t2, euler_cycle, hamilton_cycle


# =========================
# MAIN EXPERYMENT
# =========================
if __name__ == "__main__":

    ns = [10, 15, 20, 25, 30, 35, 40, 45, 50,
          55, 60, 65, 70, 75, 80]

    densities = ["30", "70"]

    for d in densities:
        with open(f"results_{d}.txt", "w") as out:

            out.write("n time_euler time_hamilton\n")

            for n in ns:
                filename = f"graph_{n}_{d}.txt"
                graph = load_graph(filename)

                t_e, t_h, e_cycle, h_cycle = measure(graph)

                out.write(f"{n} {t_e:.6f} {t_h:.6f}\n")

                # zapis cykli osobno
                with open(f"cycles_{n}_{d}.txt", "w") as c:
                    c.write("Euler:\n")
                    c.write(" ".join(map(str, e_cycle)) + "\n\n")

                    c.write("Hamilton:\n")
                    c.write(" ".join(map(str, h_cycle)) + "\n")

    print("Eksperyment zakończony.")