base_pattern = [0, 1, 0, -1]


def gen_pattern(length, output_element):
    base_pattern_this_elem = []
    for i in range(4):
        base_pattern_this_elem += [base_pattern[i]] * (output_element + 1)
    pattern = []
    while len(pattern) < length + 1:
        pattern += base_pattern_this_elem
    return pattern[1:]


def do_phase(input_list):
    output_list = []
    for i in range(len(input_list)):
        row_total = 0
        pattern = gen_pattern(len(input_list), i)
        for j in range(len(input_list)):
            row_total += input_list[j] * pattern[j]
        output_list.append(int(str(row_total)[-1]))
    return output_list
        
        
def do_fft(phase_num, total_phases, starting_list):
    if phase_num == total_phases:
        return starting_list
    else:
        phase_output = do_phase(starting_list)
        return do_fft(phase_num + 1, total_phases, phase_output)


if __name__ == "__main__":
    with open("inputs/day16.txt", 'r') as fh:
        starting_list = [int(x) for x in list(fh.readline().strip())]
    
    #starting_list = [int(x) for x in list("19617804207202209144916044189917")]

    final_list = do_fft(0, 100, starting_list)
    print("".join([str(x) for x in final_list[0:8]]))
