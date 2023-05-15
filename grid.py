def count_paths(input_string):
    # Parse the input string to create a grid
    grid = []
    for line in input_string.split('\n'):
        row = []
        for char in line.split():
            if char == 'A':
                start = (len(grid), len(row))
            elif char == 'B':
                end = (len(grid), len(row))
            row.append(char)
        grid.append(row)

    # Define a recursive function to count the number of paths
    def count_paths_helper(curr, visited):
        if curr == end:
            return 1
        count = 0
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_pos = (curr[0] + move[0], curr[1] + move[1])
            if 0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0]) and grid[next_pos[0]][next_pos[1]] != 'x' and next_pos not in visited:
                count += count_paths_helper(next_pos, visited + [next_pos])
        return count

    # Call the helper function to count the number of paths
    return count_paths_helper(start, [start])

# Test the function with sample inputs
input_string = 'A . . . \n. . . B'
number_of_paths = count_paths(input_string)
print(number_of_paths)
# Output: 0

input_string = 'A . . .\n. . . .\n. . . .\n. . x B'
number_of_paths = count_paths(input_string)
print(number_of_paths)  # Output: 1
