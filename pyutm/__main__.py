from utm import UTM
SAMPLE_MACHINE = '1'.join(['0' * i for i in [7, 3, 1, 3, 1, 6, 7]])
DELTAS = [(1, 1, 2, 3, 2),
          (1, 2, 7, 2, 2),
          (1, 3, 7, 3, 2),
          (2, 1, 3, 2, 2),
          (2, 2, 2, 2, 2),
          (2, 3, 6, 3, 2),
          (3, 1, 4, 2, 2),
          (3, 2, 3, 2, 2),
          (3, 3, 5, 3, 1),
          (4, 1, 3, 1, 2),
          (4, 2, 4, 2, 2),
          (4, 3, 7, 3, 2),
          (5, 1, 5, 1, 1),
          (5, 2, 5, 2, 1),
          (5, 3, 2, 3, 2)]
DELTA_TAPE = '11'.join(['1'.join(['0' * i for i in d]) for d in DELTAS])
INPUT_TAPE = '1'.join(['0'] * 2**20)


INPUT_MACHINE = '111'.join([SAMPLE_MACHINE, DELTA_TAPE, INPUT_TAPE])

if __name__ == '__main__':
    utm = UTM(INPUT_MACHINE)
    utm.print_description()
    print()
    print('-----Transitions-----')
    # print('Machine tape: {}'.format(utm.machine_tape))
    count = 0    
    for _ in utm:
        # print('{} => {}'.format(start, end))
        count += 1

    print()
    print('Machine halted in {} steps. Final state:'.format(count))
    utm.print_state()
