def count_paths(input_string):
    # Parse the input string to a 2D list
    grid = [[c for c in row] for row in input_string.split('\n') if row]

    # Get the dimensions of the grid
    m, n = len(grid), len(grid[0])

    # Initialize the 2D array of path counts
    paths = [[0] * n for _ in range(m)]

    # Mark the starting point as reachable
    paths[0][0] = 1

    # Fill in the path counts row by row
    for i in range(m):
        for j in range(n):
            # Skip points marked as "x"
            if grid[i][j] == 'x':
                continue
            # Update the path count for the current point
            if i > 0 and grid[i-1][j] != 'x':
                paths[i][j] += paths[i-1][j]
            if j > 0 and grid[i][j-1] != 'x':
                paths[i][j] += paths[i][j-1]

    # Return the number of paths to the bottom right point
    return paths[m-1][n-1]

input_string = 'A . . .\n. . . B'
number_of_paths = count_paths(input_string)
print(number_of_paths)  # Output: 0

input_string = 'A . . .\n. . . .\n. . . .\n. . x B'
number_of_paths = count_paths(input_string)
print(number_of_paths)  # Output: 1
