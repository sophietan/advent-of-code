def intCode(input):
    input[1] = 20
    input[2] = 3
    position = 0
    while(position < len(input)):
        op_code = input[position]
        if op_code == 99:
            break

        index_a = input[position + 1]
        index_b = input[position + 2]
        index_result = input[position + 3]

        if index_a > len(input) or index_b > len(input) or index_result > len(input):
            raise IndexError('Found an index we cannot access!')

        if op_code == 1:
            input[index_result] = input[index_a] + input[index_b]

        if op_code == 2:
            input[index_result] = input[index_a] * input[index_b]
        position += 4
    return input


def main():
    with open('inputs/day_2.txt') as f:
        input = f.read().split(',')
        input = list(map(int, input))
        result = intCode(input)
        print(result[0])


if __name__ == '__main__':
    main()
