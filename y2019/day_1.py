def calc_fuel_requirements(mass: int) -> int:
    return mass // 3 - 2


def calc_fuel_for_fuel(mass: int) -> int:
    total = 0
    mass = calc_fuel_requirements(mass)
    while mass > 0:
        total += mass
        mass = calc_fuel_requirements(mass)

    return total


def main():
    with open('inputs/day_1.txt') as f:
        module_sizes = f.read().splitlines()
        part_1 = sum(calc_fuel_requirements(int(mass)) for mass in module_sizes)
        part_2 = sum(calc_fuel_for_fuel(int(mass)) for mass in module_sizes)
        print(part_1, part_2)


if __name__ == '__main__':
    main()
