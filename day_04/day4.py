def row_into_dict(row):
    pairs = row.split(" ")
    quoted_pairs = map(lambda p: pair_into_quoted_pair(p), pairs)
    contents = ','.join(quoted_pairs)
    dict_str = '{' + contents + '}'
    return json.loads(dict_str)


# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

# # rules

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.


def is_valid(passport):
    return(
        passport.get('byr') and
        passport.get('iyr') and
        passport.get('eyr') and
        passport.get('hgt') and
        passport.get('hcl') and
        passport.get('ecl') and
        passport.get('pid')
    )

def valid_byr(byr):
    return (
        byr and
        len(byr) == 4 and
        byr >= "1920" and
        byr <= "2002"
    )

def valid_iyr(iyr):
    return (
        iyr and
        len(iyr) == 4 and
        iyr >= "2010" and
        iyr <= "2020"
    )

def valid_eyr(eyr):
    return (
        eyr and
        len(eyr) == 4 and
        eyr >= "2020" and
        eyr <= "2030"
    )

def valid_hgt(hgt):
    if not hgt:
        return False
    p = re.compile('^(\d+)(in|cm)\Z')
    m = p.match(hgt)
    if not m:
        return False
    num = m.group(1)
    unit = m.group(2)
    if unit == 'cm':
        return num >= "150" and num <= "193"
    else:
        return num >= "59" and num <= "76"

def valid_hcl(hcl):
    if not hcl:
        return False
    p = re.compile('^#(\d|[a-f]){6}\Z')
    return (p.match(hcl) is not None)


def valid_ecl(ecl):
    if not ecl:
        return False
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in valid_colors


def valid_pid(pid):
    if not pid:
        return False
    p = re.compile('^(\d){9}\Z')
    return (p.match(pid) is not None)

def is_valid(passport):
    return(
        valid_byr(passport.get('byr')) and
        valid_iyr(passport.get('iyr')) and
        valid_eyr(passport.get('eyr')) and
        valid_hgt(passport.get('hgt')) and
        valid_hcl(passport.get('hcl')) and
        valid_ecl(passport.get('ecl')) and
        valid_pid(passport.get('pid'))
    )


def passport_strs():
    next_item = ""
    for row in open("/Users/oscarliu/Desktop/aoc/day4.txt", "r"):
        if row == "\n":
            yield next_item
            next_item = ""
        else:
            next_item += row
    yield next_item

def passport_str_into_dict(ps):
    no_newlines = ps.replace("\n", " ").strip()
    pairs = no_newlines.split(" ")
    passport = {}
    for pair in pairs:
        k, v = pair.split(":")
        passport[k] = v
    return passport

num_valid = 0
pstrings = passport_strs()
for p in pstrings:
    if is_valid(passport_str_into_dict(p)):
        num_valid += 1

print(num_valid)
