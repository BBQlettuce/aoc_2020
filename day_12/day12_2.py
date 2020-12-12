with open('./input.txt') as f:
    steps = f.read().strip().split('\n')

class Ship:
    default_position = {
        'x': 0,
        'y': 0,
    }

    default_waypoint = {
        'x': 10,
        'y': 1
    }

    def __init__(self, position=default_position, waypoint=default_waypoint):
        self.position = position
        self.waypoint = waypoint

    def shift_waypoint(self, action, units):
        if action == 'E':
            self.waypoint['x'] += units
        if action == 'S':
            self.waypoint['y'] -= units
        if action == 'W':
            self.waypoint['x'] -= units
        if action == 'N':
            self.waypoint['y'] += units
    
    def turn(self, action, units):
        times_to_turn = units / 90
        sign = -1 if action == 'L' else 1
        rotation_way = int(times_to_turn * sign) % 4
        current_waypoint_x = self.waypoint['x']
        current_waypoint_y = self.waypoint['y']
        if rotation_way == 1:
            self.waypoint['x'] = current_waypoint_y
            self.waypoint['y'] = -1 * current_waypoint_x
        if rotation_way == 2:
            self.waypoint['x'] = -1 * current_waypoint_x
            self.waypoint['y'] = -1 * current_waypoint_y
        if rotation_way == 3:
            self.waypoint['x'] = -1 * current_waypoint_y
            self.waypoint['y'] = current_waypoint_x

    def forward(self, units):
        x_shift = self.waypoint['x'] * units
        y_shift = self.waypoint['y'] * units
        self.position['x'] += x_shift
        self.position['y'] += y_shift

    def perform_step(self, code):
        action = code[0]
        units = int(code[1:])
        if action in ['N', 'E', 'S', 'W']:
            self.shift_waypoint(action, units)
        if action in ['L', 'R']:
            self.turn(action, units)
        if action == 'F':
            self.forward(units)

    def run_steps(self, codes):
        for code in codes:
            self.perform_step(code)