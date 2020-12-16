# starting_sequence = [0,6,1,7,2,19,20]

class Game:
    def __init__(self, starting_sequence, last_turn):
        self.starting_sequence = starting_sequence
        self.move_log = {}
        # self.moves = []
        self.last_move = None
        self.current_turn = 0
        self.last_turn = last_turn

    def log_move(self, num):
        # self.moves.append(num)
        self.last_move = num
        print(num)
        past_moves_with_num = self.move_log.get(num)
        if not past_moves_with_num:
            self.move_log[num] = {'last': self.current_turn}
        else:
            self.move_log[num]['prev'] = past_moves_with_num['last']
            self.move_log[num]['last'] = self.current_turn
        self.current_turn += 1

    def play_turn(self):
        # get through the starting numbers first
        if self.current_turn < len(self.starting_sequence):
            num = self.starting_sequence[self.current_turn]
            self.log_move(num)
        else:
            log_last_move = self.move_log[self.last_move]
            if log_last_move.get('prev') is not None:
                diff = log_last_move['last'] - log_last_move['prev']
                self.log_move(diff)
            else:
                self.log_move(0)

    def run_game(self):
        while self.current_turn < self.last_turn:
            self.play_turn()

        return self.last_move
