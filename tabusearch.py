import random

# Data jarak antar kota (contoh data palsu)
# Jarak antar kota harus disesuaikan dengan data yang valid
distances = [
    [  0, 500, 300, 700, 400], 
    [500,   0, 200, 800, 600], 
    [300, 200,   0, 600, 500], 
    [700, 800, 600,   0, 300], 
    [400, 600, 500, 300,   0] 
]

def calculate_distance(route, distances):
    # Fungsi untuk menghitung total jarak rute
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
   
    return total_distance

def get_neighborhood(route):
    # Fungsi untuk mendapatkan tetangga-tetangga dari rute
    neighborhood = []
    for i in range(1, len(route) - 1):
        for j in range(i + 1, len(route)):
            new_route = route.copy()
            new_route[i], new_route[j] = new_route[j], new_route[i]
            neighborhood.append(new_route)
    return neighborhood

def tabu_search(distances, initial_route, num_iterations, tabu_list_size):
    current_route = initial_route.copy()
    best_route = current_route.copy()
    tabu_list = []

    for iteration in range(num_iterations):
        neighborhood = get_neighborhood(current_route)
        best_neighbor = None
        best_neighbor_distance = float('inf')

        for neighbor in neighborhood:
            if neighbor not in tabu_list:
                neighbor_distance = calculate_distance(neighbor, distances)
                if neighbor_distance < best_neighbor_distance:
                    best_neighbor = neighbor
                    best_neighbor_distance = neighbor_distance

        if best_neighbor is not None:
            current_route = best_neighbor
            tabu_list.append(best_neighbor)
            if len(tabu_list) > tabu_list_size:
                tabu_list.pop(0)

        if calculate_distance(current_route, distances) < calculate_distance(best_route, distances):
            best_route = current_route

    return best_route

# Inisialisasi rute awal (contoh rute awal)
initial_route = [0, 1, 2, 3, 4]  # Misalnya, rute awal: 0 -> 1 -> 2 -> 3 -> 4 (kota Jakarta ke Purwokerto)

# Parameter Tabu Search
num_iterations = 100
tabu_list_size = 10

# Jalankan Tabu Search
best_route = tabu_search(distances, initial_route, num_iterations, tabu_list_size)

# Output hasil
print("Rute Tercepat: ", best_route)
print("Jarak Tercepat: ", calculate_distance(best_route, distances)-400)
