import random

N = 15

def create_hamilton_cycle(n):
    cycle = list(range(n))
    random.shuffle(cycle)
    edges = set()

    for i in range(n):
        a = cycle[i]
        b = cycle[(i + 1) % n]
        edges.add(tuple(sorted((a, b))))

    return edges

def make_eulerian(edges, n):
    deg = [0] * n
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1

    odd = [i for i in range(n) if deg[i] % 2 == 1]

    for i in range(0, len(odd), 2):
        a, b = odd[i], odd[i + 1]
        edges.add(tuple(sorted((a, b))))

    return edges

def fill_density(edges, n, target_edges):
    while len(edges) < target_edges:
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        if a != b:
            edges.add(tuple(sorted((a, b))))
    return edges

def to_matrix(edges, n):
    m = [[0]*n for _ in range(n)]
    for a, b in edges:
        m[a][b] = 1
        m[b][a] = 1
    return m

def save_matrix(filename, matrix):
    with open(filename, "w") as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")

def generate_graph(n, density, name):
    max_edges = n*(n-1)//2
    target = int(max_edges * density)

    edges = create_hamilton_cycle(n)
    edges = make_eulerian(edges, n)
    edges = fill_density(edges, n, target)

    matrix = to_matrix(edges, n)
    save_matrix(f"{name}.txt", matrix)

# GENERACJA
generate_graph(N, 0.30, "graph_30")
generate_graph(N, 0.70, "graph_70")