from computer import Computer


if __name__ == "__main__":
    #read the input file
    with open("inputs/day13.txt", 'r') as inputfile:
        memory = inputfile.read().split(',')
        memory = [int(x) for x in memory]

    c = Computer(None, memory)
    c.memory[0] = 2
    c.run_program()