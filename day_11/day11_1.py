from copy import deepcopy


with open('./seats.txt') as f:
    seat_rows = f.read().strip().split('\n')
    seat_map = [list(row) for row in seat_rows]
    num_rows = len(seat_map)
    num_cols = len(seat_map[0])


def adjacent_coordinates(row, col):
    coords = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1]
    ]
    return [coord for coord in coords if coord[0] >= 0 and coord[0] < num_rows and coord[1] >= 0 and coord[1] < num_cols]


def is_occupied(s_map, row, col):
    return s_map[row][col] == '#'


def adjacent_occupied(s_map, row, col):
    adj_coords = adjacent_coordinates(row, col)
    occupied = [coord for coord in adj_coords if is_occupied(s_map, *coord)]
    return occupied


def get_next_seat_state(s_map, row, col):
    content = s_map[row][col]
    if content == '.':
        return content
    occupied = adjacent_occupied(s_map, row, col)
    if not occupied:
        return '#'
    if len(occupied) >= 4:
        return 'L'
    return content


def get_next_map_state(s_map):
    new_map = deepcopy(s_map)
    for row in range(num_rows):
        for col in range(num_cols):
            new_map[row][col] = get_next_seat_state(s_map, row, col)

    return new_map


def maps_equal(map1, map2):
    for row in range(num_rows):
        for col in range(num_cols):
            if map1[row][col] != map2[row][col]:
                return False
    return True


def get_final_map(s_map):
    current_map = deepcopy(s_map)
    next_map = get_next_map_state(current_map)
    while not maps_equal(current_map, next_map):
        current_map = next_map
        next_map = get_next_map_state(next_map)
    return next_map


def num_occupied(s_map):
    output = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if s_map[row][col] == '#':
                output += 1
    return output
