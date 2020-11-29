from computer import Computer


if __name__ == "__main__":
    #read the input file
    with open("inputs/day9.txt", 'r') as inputfile:
        memory = inputfile.read().split(',')
        memory = [int(x) for x in memory]

    #memory = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    c = Computer(None, memory)
    #c.DEBUG = True
    c.run_program()