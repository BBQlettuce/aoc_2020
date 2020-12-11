from copy import deepcopy


with open('./seats.txt') as f:
    seat_rows = f.read().strip().split('\n')
    seat_map = [list(row) for row in seat_rows]
    num_rows = len(seat_map)
    num_cols = len(seat_map[0])


def _urow(s_map, row, col):
    next_row = row + 1
    while next_row < num_rows:
        next_visible = s_map[next_row][col]
        if next_visible == '#':
            return [next_row, col]
        if next_visible == 'L':
            return None
        next_row += 1
    return None


def _drow(s_map, row, col):
    next_row = row - 1
    while next_row >= 0:
        next_visible = s_map[next_row][col]
        if next_visible == '#':
            return [next_row, col]
        if next_visible == 'L':
            return None
        next_row -= 1
    return None


def _ucol(s_map, row, col):
    next_col = col + 1
    while next_col < num_cols:
        next_visible = s_map[row][next_col]
        if next_visible == '#':
            return [row, next_col]
        if next_visible == 'L':
            return None
        next_col += 1
    return None


def _dcol(s_map, row, col):
    next_col = col - 1
    while next_col >= 0:
        next_visible = s_map[row][next_col]
        if next_visible == '#':
            return [row, next_col]
        if next_visible == 'L':
            return None
        next_col -= 1
    return None


def _urow_ucol(s_map, row, col):
    next_row = row + 1
    next_col = col + 1
    while next_row < num_rows and next_col < num_cols:
        next_visible = s_map[next_row][next_col]
        if next_visible == '#':
            return [next_row, next_col]
        if next_visible == 'L':
            return None
        next_row += 1
        next_col += 1
    return None


def _urow_dcol(s_map, row, col):
    next_row = row + 1
    next_col = col - 1
    while next_row < num_rows and next_col >= 0:
        next_visible = s_map[next_row][next_col]
        if next_visible == '#':
            return [next_row, next_col]
        if next_visible == 'L':
            return None
        next_row += 1
        next_col -= 1
    return None


def _drow_ucol(s_map, row, col):
    next_row = row - 1
    next_col = col + 1
    while next_row >= 0 and next_col < num_cols:
        next_visible = s_map[next_row][next_col]
        if next_visible == '#':
            return [next_row, next_col]
        if next_visible == 'L':
            return None
        next_row -= 1
        next_col += 1
    return None


def _drow_dcol(s_map, row, col):
    next_row = row - 1
    next_col = col - 1
    while next_row >= 0 and next_col >= 0:
        next_visible = s_map[next_row][next_col]
        if next_visible == '#':
            return [next_row, next_col]
        if next_visible == 'L':
            return None
        next_row -= 1
        next_col -= 1
    return None


def visible_occupied(s_map, row, col):
    visible = [
        _urow(s_map, row, col),
        _drow(s_map, row, col),
        _ucol(s_map, row, col),
        _dcol(s_map, row, col),
        _urow_ucol(s_map, row, col),
        _urow_dcol(s_map, row, col),
        _drow_ucol(s_map, row, col),
        _drow_dcol(s_map, row, col),
    ]
    return [c for c in visible if c]


def get_next_seat_state(s_map, row, col):
    content = s_map[row][col]
    if content == '.':
        return content
    occupied = visible_occupied(s_map, row, col)
    if not occupied:
        return '#'
    if len(occupied) >= 5:
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
