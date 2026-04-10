import itertools

# Distance matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [0, 1, 2, 3]

def calculate_distance(path):
    distance = 0

    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i+1]]

    # Return to starting city
    distance += graph[path[-1]][path[0]]

    return distance


min_distance = float('inf')
best_path = None

# Generate all possible routes
for path in itertools.permutations(cities):

    distance = calculate_distance(path)

    if distance < min_distance:
        min_distance = distance
        best_path = path


print("Best Path:", best_path)
print("Minimum Distance:", min_distance)
