from copy import deepcopy

START = """
...#..#.
..##.##.
..#.....
....#...
#.##...#
####..##
...##.#.
#.#.#...
"""


# get starting config
# 3d grid
GRID = {}
for x, line in enumerate(START.strip().split('\n')):
    for y, char in enumerate(line):
        GRID[(x, y, 0)] = char

# get neighbors of one coord
def get_neighbors(coord):
    x, y, z = coord
    neighbors = set()
    for new_x in range(x - 1, x + 2):
        for new_y in range(y - 1, y + 2):
            for new_z in range(z - 1, z + 2):
                neighbors.add((new_x, new_y, new_z))
    # remove self
    neighbors.remove(coord)
    return neighbors

# get all the positions that we care about
# gonna be everything in the grid, extended out by 1
# could just use a set and do get neighbors on everything
def get_grid_neighbors(grid):
    coords = list(grid.keys())
    grid_neighbors = set()
    for coord in coords:
        neighbors = get_neighbors(coord)
        grid_neighbors = grid_neighbors.union(neighbors)
    return grid_neighbors

# rules
def get_next(grid, coord):
    current_state = grid.get(coord, '.')
    neighbors = get_neighbors(coord)
    num_active_neighbors = 0
    for n in neighbors:
        if grid.get(n) == '#':
            num_active_neighbors += 1
    if current_state == '#':
        if num_active_neighbors == 2 or num_active_neighbors == 3:
            return '#'
        else:
            return '.'
    else:
        if num_active_neighbors == 3:
            return '#'
        else:
            return '.'

# execute a run
def get_next_grid_state(grid):
    new_grid = deepcopy(grid)
    coords_to_update = get_grid_neighbors(new_grid)
    for coord in coords_to_update:
        new_coord_state = get_next(grid, coord)
        new_grid[coord] = new_coord_state
    return new_grid

# do 6 times
current_grid = deepcopy(GRID)
for _ in range(6):
    new_grid = get_next_grid_state(current_grid)
    current_grid = new_grid
# count active
num_final_active = 0
for coord in current_grid:
    if current_grid[coord] == '#':
        num_final_active += 1
print(num_final_active)