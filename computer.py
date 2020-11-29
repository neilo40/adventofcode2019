class Computer:
    DEBUG = False
    QUIET = True
    
    def __init__(self, input_values, memory):
        self.output = []
        self.input_values = input_values
        self.input = None
        self.memory = memory
        self.relative_base = 0
        self.score = 0
        self.screen = [[" " for x in range(50)] for y in range(25)]
        self.tilemap = [" ", "|", "#", "=", "o"]
        self.paddle = (0, 0)
        self.ball = (0, 0)

    def log(self, value):
        if self.DEBUG:
            print(value)

    def get_opcode_mode(self, value):
        opcode = int(value[-2:])
        if len(value) < 3:
            mode_raw = "000"
        else:
            mode_raw = value[:-2]
            while len(mode_raw) < 3:
                mode_raw = '0' + mode_raw
        mode = list(reversed([int(x) for x in mode_raw]))
        return opcode, mode

    def get_operand(self, address, mode):
        """ 
        mode 0 = position
        mode 1 = value
        mode 2 = relative
        """
        value = self.get_memory(address)
        if mode == 0:
            return int(self.get_memory(value))
        elif mode == 1:
            return int(value)
        elif mode == 2:
            return int(self.get_memory(self.relative_base + value))

    def get_store_address(self, address, mode):
        value = self.get_memory(address)
        if mode == 0:
            return int(value)
        elif mode == 1:
            print("Invalid address mode for store address")
            return None
        elif mode == 2:
            return self.relative_base + value

    def set_memory(self, address, value):
        if address < 0:
            print("Invalid negative address {}".format(address))
            return
        elif address >= len(self.memory):
            self.memory.extend([0 for x in range(address - len(self.memory) + 1)])
        self.memory[address] = value

    def get_memory(self, address):
        if address >= len(self.memory):
            self.memory.extend([0 for x in range(address - len(self.memory) + 1)])
        return self.memory[address]

    def get_operands(self, address, opcode, mode):
        operands = []
        if opcode in [1, 2, 5, 6, 7, 8]:
            r = range(1, 3)
        elif opcode in [4, 9]:
            r = range(1, 2)
        else:
            r = range(0)
        
        for i in r:
            operands.append(self.get_operand(address + i, mode[i - 1]))

        # store address
        if opcode in [1, 2, 7, 8]:
            operands.append(self.get_store_address(address + 3, mode[2]))
        elif opcode in [3]:
            operands.append(self.get_store_address(address + 1, mode[0]))

        return operands

    def display_output(self):
        if len(self.output) == 3:
            x = self.output[0]
            y = self.output[1]
            tile = self.output[2]
            if x == -1 and y == 0:
                self.score = tile
            else:
                if tile == 3:
                    self.paddle = (x, y)
                elif tile == 4:
                    self.ball = (x, y)
                self.screen[y][x] = self.tilemap[tile]
            self.output = []
        
        for row in self.screen:
            print("".join([str(z) for z in row]))
        print("Score: {}".format(self.score))

        if self.ball[0] < self.paddle[0]:
            self.input = -1
        elif self.ball[0] > self.paddle[0]:
            self.input = 1
        else:
            self.input = 0

    def run_program(self):
        address = 0
        opcode = 0
        input_value_index = 0

        while(True):
            opcode, mode = self.get_opcode_mode(str(self.memory[address]))
            operands = self.get_operands(address, opcode, mode)
            self.log("At address {}, executing opcode {} in mode {} with operands {}".format(address, opcode, mode, operands))

            #ADD
            if opcode == 1:
                self.log("ADD {} to {} -> {}".format(operands[0], operands[1], operands[2]))
                self.set_memory(operands[2], operands[0] + operands[1])
                address += 4

            #MUL
            elif opcode == 2:
                self.log("MUL {} by {} -> {}".format(operands[0], operands[1], operands[2]))
                self.set_memory(operands[2], operands[0] * operands[1])
                address += 4
                    
            #STR
            elif opcode == 3:
                self.log("STORE input at {}".format(operands[0]))
                if self.input is not None:
                    input_num = self.input
                elif self.input_values:
                    input_num = self.input_values[input_value_index]
                    input_value_index += 1
                else:
                    input_num = input("provide input: ")
                self.set_memory(operands[0], int(input_num))
                address += 2

            #PRN
            elif opcode == 4:
                if not self.QUIET:
                    print(operands[0])
                self.output.append(operands[0])
                address += 2

            #BTR
            elif opcode == 5:
                if not operands[0] == 0:
                    address = operands[1]
                else:
                    address += 3

            #BFL
            elif opcode == 6:
                if operands[0] == 0:
                    address = operands[1]
                else:
                    address += 3

            #SLT
            elif opcode == 7:
                if operands[0] < operands[1]:
                    self.set_memory(operands[2], 1)
                else:
                    self.set_memory(operands[2], 0)
                address += 4

            #SEQ
            elif opcode == 8:
                if operands[0] == operands[1]:
                    self.set_memory(operands[2], 1)
                else:
                    self.set_memory(operands[2], 0)
                address += 4

            #REL
            elif opcode == 9:
                self.relative_base += operands[0]
                address += 2

            #BRK
            elif opcode == 99:
                return

            else:
                print("ya done a boob, got an opcode of {} at address {}".format(opcode, address))
                return

            self.display_output()