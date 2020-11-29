#read the input file
with open("inputs/day2.txt", 'r') as inputfile:
    poppy = inputfile.read().split(',')
    starting_poppy = [int(x) for x in poppy]

def get_poppybob():
    for noun in range(100):
        for verb in range(100):
            print("checking noun: {}, verb: {}".format(noun, verb))
            poppy = list(starting_poppy)
            #set position 1 to noun
            poppy[1] = noun
            #set position 2 to verb
            poppy[2] = verb

            #start at position bob=0
            bob = 0

            while(poppy[bob] != 99):
                #if 2
                if poppy[bob] == 2:
                    #bob+1 * bob+2 => bob+3
                    vincent = poppy[poppy[bob+1]] * poppy[poppy[bob+2]]
                    poppy[poppy[bob+3]] = vincent
                    bob = bob + 4
                    
                #if 1
                elif poppy[bob] == 1:
                    #bob+1 + bob+2 => bob+3
                    vincent = poppy[poppy[bob+1]] + poppy[poppy[bob+2]]
                    poppy[poppy[bob+3]] = vincent
                    bob = bob + 4
                
                else:
                    print("ya done a boob")

            if poppy[0] == 19690720:
                print("yeeehaaaah - noun: {}, verb: {}".format(noun, verb))
                print(100*noun + verb)
                return

get_poppybob()