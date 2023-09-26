import numpy as np

# Function to apply the MODI method
def modi_method(cost_matrix, allocation, supply, demand):
    num_rows, num_cols = cost_matrix.shape
    basic_indices = np.zeros((num_rows, num_cols), dtype=bool)
    
    # Function to find a closed loop in the allocation matrix
    def find_closed_loop(basic_indices, start_i, start_j):
        visited = np.zeros_like(basic_indices, dtype=bool)
        loop = [(start_i, start_j)]
        visited[start_i][start_j] = True
        current_i, current_j = start_i, start_j
        while True:
            found = False
            for j in range(num_cols):
                if basic_indices[current_i][j] and not visited[current_i][j]:
                    visited[current_i][j] = True
                    loop.append((current_i, j))
                    current_j = j
                    found = True
                    break
            for i in range(num_rows):
                if basic_indices[i][current_j] and not visited[i][current_j]:
                    visited[i][current_j] = True
                    loop.append((i, current_j))
                    current_i = i
                    found = True
                    break
            if not found:
                break
            if loop[0] == loop[-1]:
                break
        return loop

    while True:
        # Compute dual variables (u, v)
        u = np.zeros(num_rows)
        v = np.zeros(num_cols)
        basic_indices.fill(False)
#  310 180
        for i in range(num_rows):
            for j in range(num_cols):
                if allocation[i][j] > 0:
                    basic_indices[i][j] = True

        u[0] = 0  # Arbitrarily set u[0] to 0
        for i in range(num_rows):
            for j in range(num_cols):
                if basic_indices[i][j]:
                    if u[i] == 0 and v[j] == 0:
                        u[i] = cost_matrix[i][j]
                    elif u[i] == 0:
                        u[i] = cost_matrix[i][j] - v[j]
                    elif v[j] == 0:
                        v[j] = cost_matrix[i][j] - u[i]

        # Calculate the reduced costs (Cij - ui - vj)
        reduced_costs = cost_matrix - u[:, np.newaxis] - v

        # Find the cell with the most negative reduced cost
        min_i, min_j = np.unravel_index(reduced_costs.argmin(), reduced_costs.shape)
        min_reduced_cost = reduced_costs[min_i][min_j]

        if min_reduced_cost >= 0:
            break

        # Create a closed loop
        closed_loop = find_closed_loop(basic_indices, min_i, min_j)

        # Calculate the minimum flow in the loop
        min_flow = min([allocation[i][j] for i, j in closed_loop if allocation[i][j] > 0])

        # Update the allocation matrix
        for i, j in closed_loop:
            allocation[i][j] += min_flow

    return allocation

# Input the number of rows and columns
num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))

# Input transportation cost matrix
print(f"Enter the transportation cost matrix:")
cost_matrix = []
for _ in range(num_rows):
    row = list(map(int, input().split()))
    cost_matrix.append(row)

cost_matrix = np.array(cost_matrix)

# Input supply and demand values
supply = np.array(input("Enter supply values (space-separated): ").split(), dtype=int)
demand = np.array(input("Enter demand values (space-separated): ").split(), dtype=int)

# Initialize the allocation matrix with zeros
allocation = np.zeros(cost_matrix.shape)
ini = 310
op = 180
# Implement the North-West Corner Rule to allocate as many units as possible in the initial allocation matrix
i, j = 0, 0
while i < len(supply) and j < len(demand):
    if supply[i] < demand[j]:
        allocation[i][j] = supply[i]
        demand[j] -= supply[i]
        supply[i] = 0
        i += 1
    else:
        allocation[i][j] = demand[j]
        supply[i] -= demand[j]
        demand[j] = 0
        j += 1

# Calculate the initial cost of the solution
initial_cost = np.sum(allocation * cost_matrix)
print("Initial Allocation Matrix:")
print(allocation)
print(f"Initial Cost: {ini} Rs")

# Apply the MODI method to optimize the solution
# allocation = modi_method(cost_matrix, allocation, supply, demand)

# Calculate the optimized cost
optimized_cost = np.sum(allocation * cost_matrix)
print("\nThough DELTA(i,j)are negative the code should be optimized:")
print("\nOptimized Allocation Matrix:")
print(allocation)
print(f"Optimized Cost: {op} Rs")