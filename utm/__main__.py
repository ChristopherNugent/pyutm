from utm import UTM, MachineHalt

SAMPLE_MACHINE = '000100010100101001000'
DELTA_FUNCTION = '010100100100'
INPUT_TAPE = '0'

INPUT_MACHINE = '111'.join([SAMPLE_MACHINE, DELTA_FUNCTION, INPUT_TAPE])

if __name__ == '__main__':
    utm = UTM(INPUT_MACHINE)
    utm.print_description()
    print()

    try:
        while True:
            utm.print_state()
            print()
            utm.step()
    except MachineHalt:
        print('Machine halted,')
