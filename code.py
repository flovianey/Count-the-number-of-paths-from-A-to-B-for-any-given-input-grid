def count_paths(input_string):
    # Parse input string and create grid
    rows = input_string.strip().split('\n')
    grid = [list(row) for row in rows]
    n_rows = len(grid)
    n_cols = len(grid[0])

    # Find starting and final positions
    start_pos = None
    final_pos = None
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == "A":
                start_pos = (i, j)
            elif grid[i][j] == "B":
                final_pos = (i, j)

    # Define helper function to check if a position is valid
    def is_valid(pos, visited):
        i, j = pos
        if i < 0 or i >= n_rows or j < 0 or j >= n_cols:
            return False
        if grid[i][j] == "x":
            return False
        if pos in visited:
            return False
        return True

    # Define recursive function to count paths
    def count_paths_recursive(pos, visited):
        if pos == final_pos and len(visited) == n_rows * n_cols - grid.count("x"):
            return 1
        count = 0
        visited.add(pos)
        for next_pos in [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]:
            if is_valid(next_pos, visited):
                count += count_paths_recursive(next_pos, visited)
        visited.remove(pos)
        return count

    # Call recursive function starting from initial position
    visited = set()
    return count_paths_recursive(start_pos, visited)
