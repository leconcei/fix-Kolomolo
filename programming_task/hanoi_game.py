def is_valid_move(source, destination):
    if destination[-1] < source[-1]:
        return False
    return True

def is_puzzle_solved(stacks, num_discs):
    for i in range(1, num_discs+1):
        if i not in stacks[-1]:
            return False
    return True

def solve_hanoi_puzzle(num_discs, num_stacks, moves):
    stacks = [[] for _ in range(num_stacks)]

    for move in moves:
        source, destination = move
        source_stack = stacks[source-1]
        destination_stack = stacks[destination-1]

        if not is_valid_move(source_stack, destination_stack):
            print("Invalid move!")
            return

        disk = source_stack.pop()
        destination_stack.append(disk)

        if is_puzzle_solved(stacks, num_discs):
            print("Puzzle solved!")
            return

    print("Puzzle not solved!")


filename = "input_01.txt"

with open(filename, "r") as file:
    num_discs, num_stacks = map(int, file.readline().split())
    moves = [list(map(int, line.split())) for line in file.readlines()]

solve_hanoi_puzzle(num_discs, num_stacks, moves)
