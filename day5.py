from computer import Computer


if __name__ == "__main__":
    #read the input file
    with open("inputs/day5.txt", 'r') as inputfile:
        memory = inputfile.read().split(',')
        memory = [int(x) for x in memory]

    c = Computer(None, memory)
    c.DEBUG = True
    c.run_program()