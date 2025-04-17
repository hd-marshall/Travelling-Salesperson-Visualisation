# TSP Algorithm Comparison Tool

An interactive Python implementation for comparing different Traveling Salesman Problem (TSP) algorithms, featuring visualisation capabilities and performance analysis.

## 🎯 Features

- Implements multiple TSP solving algorithms:
  - Brute Force (exact solution) - O(n!)
  - Nearest Neighbor (greedy heuristic) - O(n²)
  - Christofides Algorithm (approximation) - O(n³)
- Interactive visualization of routes using matplotlib
- Real-time performance comparison
- Timeout handling for long-running computations
- Random city map generation
- Multi-processing support for algorithm execution

## 🔍 Algorithm Details

### Brute Force
- Generates all possible permutations to find the optimal solution.
- Guaranteed to find the shortest possible tour.
- Practical for small datasets (n ≤ 10) due to factorial time complexity.

### Nearest Neighbor
- Simple greedy heuristic that always chooses the closest unvisited city.
- Fast execution time, suitable for larger datasets.
- Solution quality varies; typically produces tours 20-30% longer than optimal.

### Christofides Algorithm
- Approximation algorithm with guaranteed performance ratio of 1.5.
- Uses minimum spanning tree and perfect matching.
- Good balance between solution quality and computation time.
- Requires NetworkX library for graph operations.

## 📊 Visualisation

- Interactive matplotlib interface for comparing different solutions.
- Clear representation of city locations and tour paths.
- Navigation buttons to switch between different algorithm results.
- City indices displayed for easy route tracking.

## 💻 Usage

```python
# Run the program with interactive prompt
python tsp_comparison.py

# Select:
# 1. Number of cities
# 2. Algorithms to run
# 3. View results and visualizations
```

## 🔧 Dependencies

- Python 3.x
- NetworkX
- Matplotlib
- Math
- Random
- Time
- Datetime
- Itertools
- Multiprocessing

## 🚀 Performance Considerations

- Brute Force: Limited to ~10 cities
- Nearest Neighbor: Efficient up to thousands of cities
- Christofides: Practical for hundreds of cities
- Default timeout of 900 seconds (15 minutes) per algorithm

## 📈 Example Output

```
Results:
------------------------------------------------------------
Brute Force     : Distance = 3242.56    Time = 0.45    seconds
Nearest Neighbor: Distance = 4156.89    Time = 0.02    seconds
Christofides    : Distance = 3856.23    Time = 0.15    seconds
------------------------------------------------------------
```

## 🎨 Visualisation Features

- Red dots: City locations
- Blue lines: Tour paths
- Numbered annotations: City indices
- Interactive navigation between different algorithm results
- Previous/Next buttons for comparing solutions

## 🤝 Contributing

Contributions are welcome! Some possible areas for improvement:
- Additional TSP algorithms (2-opt, 3-opt, etc.)
- More visualization options
- Performance optimisations
- Additional metrics for comparison
