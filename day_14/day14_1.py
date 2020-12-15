import re

with open('./input.txt') as f:
    lines = f.read().strip().split("\n")

# part 1

class Masker:

    def __init__(self):
        self.mask = None
        self.mask_len = 36
        self.mem = {}

    def set_mask(self, line):
        [_, mask_str] = line.split(' = ')
        self.mask = mask_str

    def set_mem(self, line):
        p = re.compile('mem\[(\d+)\] = (\d+)')
        m = p.match(line)
        key = m.group(1)
        value = m.group(2)
        # convert to binary and pad
        value_as_bin_str = bin(int(value))[2:].rjust(mask_len, '0')
        masked_value = self.apply_mask(value_as_bin_str)
        self.mem[key] = masked_value

    def apply_mask(self, bin_string):
        if not self.mask:
            return bin_string
        output = ""
        for idx in range(len(bin_string)):
            if self.mask[idx] == 'X':
                output += bin_string[idx]
            else:
                output += self.mask[idx]
        return output

    def run(self, steps):
        for step in steps:
            if "mask" in step:
                self.set_mask(step)
            if "mem" in step:
                self.set_mem(step)

    def current_mem_sum(self):
        mem_values = [int(v, 2) for v in self.mem.values()]
        return sum(mem_values)
