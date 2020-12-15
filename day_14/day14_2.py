import re

with open('./input.txt') as f:
    lines = f.read().strip().split("\n")

# part 2

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
        key_as_bin_str = bin(int(key))[2:].rjust(mask_len, '0')
        masked_keys = self.apply_mask(key_as_bin_str)
        for key in masked_keys:
            self.mem[key] = value

    # return list of possible keys
    def apply_mask(self, bin_string):
        if not self.mask:
            return bin_string
        # overwrite with 1s and Xs
        overwritten = ""
        for idx in range(len(bin_string)):
            if self.mask[idx] == '0':
                overwritten += bin_string[idx]
            else:
                overwritten += self.mask[idx]

        return self.generate_variants(overwritten)

    def generate_variants(self, bin_string):
        first_x_idx = bin_string.find('X')
        if first_x_idx == -1:
            return [bin_string]
        # split into 2 variants
        v1 = bin_string[0:first_x_idx] + '0' + bin_string[first_x_idx + 1:]
        v2 = bin_string[0:first_x_idx] + '1' + bin_string[first_x_idx + 1:]
        return self.generate_variants(v1) + self.generate_variants(v2)

    def run(self, steps):
        for step in steps:
            if "mask" in step:
                self.set_mask(step)
            if "mem" in step:
                self.set_mem(step)

    def current_mem_sum(self):
        mem_values = [int(v) for v in self.mem.values()]
        return sum(mem_values)
