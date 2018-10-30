from utm import UTM
SAMPLE_MACHINE = '000100010100101001000'
DELTA_FUNCTION = '010100100100'
INPUT_TAPE = '01000'

INPUT_MACHINE = '111'.join([SAMPLE_MACHINE, DELTA_FUNCTION, INPUT_TAPE])

if __name__ == '__main__':
    utm = UTM(INPUT_MACHINE)
    utm.print_description()
    print()

    print('-----Transitions-----')
    for start, end in utm:
        print('{} => {}'.format(start, end))
        print('Machine tape: {}'.format(utm.machine_tape))
        print()
    print()
    print('Machine halted. Final state:')
    utm.print_state()
