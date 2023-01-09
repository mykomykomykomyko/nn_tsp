# Travelling Salesman Problem (TSP): 
The solution to the Travelling Salesman Problem with the method of NN.

**The Traveling Salesman Problem (TSP)** is a well-known problem in computer science and operations research, as it involves finding the shortest possible route that visits a given set of locations and returns to the starting point.

**Objective**: A salesman must visit a number of cities, with the goal of finding the shortest possible route that visits each city exactly once before returning to the starting point. The problem is to find the shortest possible route that satisfies this requirement.

**Description**: The TSP is an example of a combinatorial optimization problem, which means that it involves finding the best solution from a finite set of possible solutions. It is a difficult problem to solve, especially for large sets of cities, as the number of possible routes grows exponentially with the number of cities. As a result, finding an exact solution to the TSP can be computationally infeasible for all but the smallest instances of the problem. However, approximate solutions can often be found using heuristic algorithms or approximation algorithms.

![Representation](https://miro.medium.com/max/992/1*3Ct_bqpIsDVnMEJh6R29Hw.png)
# Nearest Neighbour Algorithm:

**The Nearest Neighbor algorithm** is a heuristic algorithm for solving this forementioned problem. It is a simple and effective method for finding approximate solutions to the TSP. The basic idea behind the NN algorithm is to:
 
- start at a given city, and at each step, visit the nearest unvisited city.
- this process is repeated until all cities have been visited.
- the route formed by the algorithm is then returned as the solution to the TSP.

One advantage of the Nearest Neighbor algorithm is that it is relatively easy to implement and can often find good solutions to the TSP in a reasonable amount of time. However, it is not guaranteed to find the optimal solution, and the quality of the solution can vary significantly depending on the order in which the cities are visited. Despite these limitations, the Nearest Neighbor algorithm is a useful starting point for solving the TSP and can often be improved upon by using more advanced algorithms.
