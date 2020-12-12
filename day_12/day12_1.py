with open('./input.txt') as f:
    steps = f.read().strip().split('\n')

class Ship:
    default_position = {
        'x': 0,
        'y': 0,
        'direction': 'E'
    }

    def __init__(self, position=default_position):
        self.position = position

    def shift(self, action, units):
        if action == 'E':
            self.position['x'] += units
        if action == 'S':
            self.position['y'] -= units
        if action == 'W':
            self.position['x'] -= units
        if action == 'N':
            self.position['y'] += units
    
    def turn(self, action, units):
        turn_order = ['N', 'E', 'S', 'W']
        times_to_turn = units / 90
        sign = -1 if action == 'L' else 1
        current_direction_idx = turn_order.index(self.position['direction'])
        new_direction_idx = current_direction_idx + int(times_to_turn * sign)
        if new_direction_idx > 3 or new_direction_idx < -4:
            new_direction_idx = new_direction_idx % 4
        self.position['direction'] = turn_order[new_direction_idx]

    def forward(self, units):
        self.shift(self.position['direction'], units)

    def perform_step(self, code):
        action = code[0]
        units = int(code[1:])
        if action in ['N', 'E', 'S', 'W']:
            self.shift(action, units)
        if action in ['L', 'R']:
            self.turn(action, units)
        if action == 'F':
            self.forward(units)

    def run_steps(self, codes):
        for code in codes:
            self.perform_step(code)