def get_row(code):
    row_code = code[0:7]
    range_start = 0
    range_end = 128
    output = None
    for char in row_code:
        midpoint = (range_end + range_start) / 2
        if char == 'F':
            range_end = midpoint
        if char == 'B':
            range_start = midpoint
        difference = range_end - range_start
        if difference == 1:
            output = range_start if char == 'F' else range_end

    return output - 1


def get_column(code):
    row_code = code[7:]
    range_start = 0
    range_end = 8
    output = None
    for char in row_code:
        midpoint = (range_end + range_start) / 2
        if char == 'L':
            range_end = midpoint
        if char == 'R':
            range_start = midpoint
        difference = range_end - range_start
        if difference == 1:
            output = range_start if char == 'F' else range_end

    return output - 1


def get_row(code):
    row_code = code[0:7]
    row_code_as_bstring = row_code.replace("F", "0").replace("B", "1")
    return int(row_code_as_bstring, 2)

def get_column(code):
    column_code = code[7:]
    column_code_as_bstring = column_code.replace("L", "0").replace("R", "1")
    return int(column_code_as_bstring, 2)

def get_seat_id(code):
    return (get_row(code) * 8) + get_column(code)


occupied = {}
for code in codes:
    row = get_row(code)
    column = get_column(code)
    if not occupied.get(row):
        occupied[row] = [column]
    else:
        occupied[row].append(column)
