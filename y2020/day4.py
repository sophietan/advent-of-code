from pprint import pprint
from string import hexdigits
from typing import List


def solution(input: List[str]):
    valid = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    passports = []
    entry = {}
    num_valid = 0
    for line in input:
        e = line.strip().split()
        if len(e) == 0:
            passports.append(entry)
            entry = {}
        for field in e:
            k, v = field.split(':')
            entry[k] = v
    # append last entry
    passports.append(entry)
    for pp in passports:
        if len(valid - pp.keys()) == 0:
            num_valid += 1
    return num_valid


def solution_2(input: List[str]):
    valid = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    passports = []
    entry = {}
    num_valid = 0
    for line in input:
        e = line.strip().split()
        if len(e) == 0:
            passports.append(entry)
            entry = {}
        for field in e:
            k, v = field.split(':')
            entry[k] = v
    # append last entry
    passports.append(entry)
    for pp in passports:
        if len(valid - pp.keys()) == 0:
            isValid = (1920 <= int(pp['byr']) <= 2002
                       and 2010 <= int(pp['iyr']) <= 2020
                       and 2020 <= int(pp['eyr']) <= 2030
                       and (pp['hgt'].endswith('cm') and 150 <= int(pp['hgt'][:-2]) <= 193
                            or pp['hgt'].endswith('in') and 59 <= int(pp['hgt'][:-2]) <= 76)
                       and pp['hcl'].startswith('#')
                       and len(pp['hcl']) == 7
                       and not set(pp['hcl'][1:]) - set(hexdigits)
                       and pp['ecl'] in 'amb blu brn gry grn hzl oth'.split()
                       and len(pp['pid']) == 9
                       and pp['pid'].isdigit())
            num_valid += isValid

    return num_valid


if __name__ == '__main__':
    with open('y2020/inputs/day4.txt', 'r') as f:
        # pprint(solution(f.readlines()))
        pprint(solution_2(f.readlines()))

