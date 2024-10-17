import math
import random
import time
import itertools
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def generate_random_map(n, max_coord=1000):
    """Generate a random map with n cities."""
    return [(random.randint(0, max_coord), random.randint(0, max_coord)) for _ in range(n)]

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(tour, cities):
    """Calculate the total distance of a tour."""
    return sum(distance(cities[tour[i]], cities[tour[(i+1) % len(tour)]]) for i in range(len(tour)))

def brute_force_tsp(cities):
    """Brute force algorithm for TSP."""
    n = len(cities)
    best_tour = min(itertools.permutations(range(n)), key=lambda tour: total_distance(tour, cities))
    return list(best_tour), total_distance(best_tour, cities)

def nearest_neighbor_tsp(cities):
    """Nearest Neighbor heuristic for TSP."""
    n = len(cities)
    unvisited = set(range(1, n))
    tour = [0]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda city: distance(cities[last], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
    return tour, total_distance(tour, cities)

def christofides_tsp(cities):
    """Christofides algorithm for TSP."""
    G = nx.Graph()
    for i, city1 in enumerate(cities):
        for j, city2 in enumerate(cities[i+1:], i+1):
            G.add_edge(i, j, weight=distance(city1, city2))
    
    # Minimum spanning tree
    mst = nx.minimum_spanning_tree(G)
    
    # Find odd-degree vertices
    odd_vertices = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]
    
    # Minimum weight perfect matching on odd-degree vertices
    G_odd = nx.subgraph(G, odd_vertices)
    matching = nx.min_weight_matching(G_odd)
    
    # Combine MST and matching
    eulerian_graph = nx.MultiGraph(mst)
    eulerian_graph.add_edges_from(matching)
    
    # Find Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(eulerian_graph))
    
    # Make Hamiltonian circuit
    visited = set()
    tour = []
    for u, v in eulerian_circuit:
        if u not in visited:
            tour.append(u)
            visited.add(u)
    
    return tour, total_distance(tour, cities)

def run_algorithm(algorithm, cities, max_time=1800):
    """Run an algorithm with a time limit."""
    start_time = time.time()
    tour, distance = algorithm(cities)
    end_time = time.time()
    execution_time = end_time - start_time
    if execution_time > max_time:
        return None, None, execution_time
    return tour, distance, execution_time

def test_algorithms(n, max_time=1800, selected_algorithms=None):
    """Test selected algorithms on a random map of size n."""
    cities = generate_random_map(n)
    all_algorithms = {
        "Brute Force": brute_force_tsp,
        "Nearest Neighbor": nearest_neighbor_tsp,
        "Christofides": christofides_tsp
    }
    
    if selected_algorithms is None:
        selected_algorithms = all_algorithms.keys()
    
    results = []
    tours = {}
    for name in selected_algorithms:
        algorithm = all_algorithms[name]
        tour, distance, time_taken = run_algorithm(algorithm, cities, max_time)
        if tour is not None:
            results.append(f"{name:<15}: Distance = {distance:<10.2f} Time = {time_taken:<10.2f} seconds")
            tours[name] = tour
        else:
            results.append(f"{name:<15}: Exceeded time limit of {max_time} seconds")
    
    return results, cities, tours

def visualize_tours(cities, tours):
    """Visualize the cities and tours found by different algorithms with interactive navigation."""
    n = len(cities)
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.subplots_adjust(bottom=0.2)
    
    tour_names = list(tours.keys())
    current_tour = [0]

    def update_plot(index):
        ax.clear()
        name = tour_names[index]
        tour = tours[name]
        x, y = zip(*cities)
        ax.scatter(x, y, c='red')
        for j in range(n):
            ax.annotate(j, (x[j], y[j]))
        
        tour_coords = [cities[tour[j % n]] for j in range(n + 1)]
        x, y = zip(*tour_coords)
        ax.plot(x, y, c='blue')
        
        ax.set_title(f"{name} Tour")
        ax.set_xlabel("X coordinate")
        ax.set_ylabel("Y coordinate")
        plt.draw()

    def on_prev(event):
        current_tour[0] = (current_tour[0] - 1) % len(tour_names)
        update_plot(current_tour[0])

    def on_next(event):
        current_tour[0] = (current_tour[0] + 1) % len(tour_names)
        update_plot(current_tour[0])

    ax_prev = plt.axes([0.3, 0.05, 0.1, 0.075])
    ax_next = plt.axes([0.6, 0.05, 0.1, 0.075])
    btn_prev = Button(ax_prev, 'Previous')
    btn_next = Button(ax_next, 'Next')
    
    btn_prev.on_clicked(on_prev)
    btn_next.on_clicked(on_next)

    update_plot(0)
    plt.show()

def print_results(results):
    """Print results with improved formatting."""
    print("\nResults:")
    print("-" * 60)
    for result in results:
        print(result)
    print("-" * 60)

def main():
    max_time = 1800  # 30 minutes in seconds
    
    while True:
        try:
            n = int(input("\nHow many cities should the algorithms explore? (Enter 0 to exit): "))
            if n == 0:
                print("Exiting the program. Goodbye!")
                break
            
            selected_algorithms = []
            print("\nSelect algorithms to run:")
            algorithms = ["Brute Force", "Nearest Neighbor", "Christofides"]
            for alg in algorithms:
                choice = input(f"Include {alg}? (y/n, default: n): ").lower()
                if choice == 'y':
                    selected_algorithms.append(alg)
            
            if not selected_algorithms:
                print("No algorithms selected. Please select at least one algorithm.")
                continue
            
            print(f"\nTesting algorithms on a random map with {n} cities:")
            results, cities, tours = test_algorithms(n, max_time, selected_algorithms)
            print_results(results)
            
            visualize_tours(cities, tours)
        
        except ValueError:
            print("Please enter a valid integer for the number of cities.")

if __name__ == "__main__":
    main()