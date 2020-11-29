from computer import Computer
from itertools import permutations


def get_thruster_signal(phase_settings, memory):
    amp_input = 0
    for amp_num in range(5):
        amp_memory = [int(x) for x in memory.split(',')]
        c = Computer([phase_settings[amp_num], amp_input], amp_memory)
        c.run_program()
        amp_output = c.output
        amp_input = amp_output
    return amp_output


def get_phase_settings():
    return permutations("01234", 5)


if __name__ == "__main__":
    with open("inputs/day7.txt", 'r') as fh:
        memory = fh.readline().strip()

    phase_settings = get_phase_settings()
    thruster_signals = []

    for phase_setting in phase_settings:
        thruster_signals.append(get_thruster_signal(phase_setting, memory))

    print(max(thruster_signals))
