from tapes import MapTape, StringTape, InputTape

# Define some strings on the tape
DATA = '0'
DELIM = '1'
RULE_DELIM = 2 * DELIM
CATEGORY_DELIM = 3 * DELIM


class UTM:
    def __init__(self, input_tape):
        split_tape = input_tape.split(CATEGORY_DELIM)
        if len(split_tape) != 3:
            raise ValueError('Tape should have 3 categories, found {}. Tape: {}'.format(
                             len(split_tape), input_tape))
        machine, rules, tape = [StringTape(string) for string in split_tape]
        self.build_machine(machine)
        self.build_rules(rules)
        self.build_tape(tape)

    def build_machine(self, machine):
        machine_fields = machine.split(DELIM)
        if len(machine_fields) != 7:
            raise ValueError('Machine description should have 7 fields, found {}. Machine: '. format(
                             len(machine_fields), machine))
        self.states = StringTape(machine_fields[0])
        self.tape_symbols = StringTape(machine_fields[1])
        self.input_symbols = StringTape(machine_fields[2])
        self.blank_symbol = StringTape(machine_fields[3])
        if self.blank_symbol.content() not in self.tape_symbols:
            raise ValueError('The blank symbol must be in the set of tape symbols.')
        self.state = StringTape(machine_fields[4])
        self.start_state = machine_fields[4]
        if self.state.content() not in self.states:
            raise ValueError('The start state must be in the set of states.')
        self.accept_state = StringTape(machine_fields[5])
        if self.accept_state.content() not in self.states:
            raise ValueError('The accept state must be in the set of states.')
        self.reject_state = StringTape(machine_fields[6])
        if self.reject_state.content() not in self.states:
            raise ValueError('The reject state must be in the set of states.')

    def build_rules(self, rules):
        rules = rules.content().split(RULE_DELIM)
        self.rules = MapTape(dict())
        for rule in rules:
            rule_fields = rule.split(DELIM)
            if len(rule_fields) != 5:
                raise ValueError('Rules should have 5 fields, found {}. Rule: {}'.format(rule))
            if rule_fields[0] not in self.states:
                raise ValueError('Rule input state not must be in the set of states.')
            if rule_fields[1] not in self.tape_symbols:
                raise ValueError('Rule input tape symbol must be in the set of tape symbols.')
            if rule_fields[2] not in self.states:
                raise ValueError('Rule output state not must be in the set of states.')
            if rule_fields[3] not in self.tape_symbols:
                raise ValueError('Rule output tape symbol must be in the set of tape symbols.')
            if rule_fields[4]  not in {'0', '00'}:
                raise ValueError('Rule output direction must be in the set of directions.')
            self.rules[tuple(rule_fields[:2])] = tuple(rule_fields[2:])

    def build_tape(self, tape):
        symbols = tape.split(DELIM)
        illegal_symbols = {err for err in symbols if err not in self.tape_symbols}
        if illegal_symbols:
            raise ValueError('Illegal tape symbols: {}'.format(illegal_symbols))
        self.machine_tape = InputTape(symbols, self.blank_symbol.content())

    def __iter__(self):
        return self

    def __next__(self):
        state = self.state.content()
        tape_symbol = self.machine_tape.read()
        key = (state, tape_symbol)
        try:
            value = self.rules[key]
            new_state, new_symbol, direction = value
        except KeyError:
            raise StopIteration()
        self.state.write(new_state)
        self.machine_tape.write(new_symbol)
        self.machine_tape.move_head(direction)
        nice_key = tuple([len(k) for k in key])
        nice_value = tuple([len(v) for v in value[:-1]] + ['L' if value[-1] == '0' else 'R'])
        return nice_key, nice_value

    def print_state(self):
        print('State: {}'.format(len(self.state.content())))
        print('Head: {}'.format(len(self.machine_tape.read())))
        if self.state.content() == self.accept_state.content():
            print ('Accepting.')
        elif self.state.content() == self.reject_state.content():
            print('Rejecting.')

    def print_description(self):
        print('Number of states: {}'.format(len(self.states.content())))
        print('The start state is: {}'.format(len(self.start_state)))
        print('The accept state is: {}'.format(len(self.accept_state.content())))
        print('The reject state is: {}'.format(len(self.reject_state.content())))
        print('Number of tape symbols: {}'.format(len(self.tape_symbols.content())))
        print('Number of input symbols: {}'.format(len(self.input_symbols.content())))
        print('The blank symbol is: {}'.format(len(self.blank_symbol.content())))
        print('Number of rules: {}.'.format(len(self.rules.map)))
        for k, v in self.rules.map.items():
            k = tuple([len(s) for s in k])
            v = tuple([len(s) for s in v[:-1]] + [{'0':'L', '00':'R'}[v[-1]]])
            print('{} => {}'.format(k, v))

    def print_static_tapes(self):
        print('States tape:')
        print(self.states)
        print('Tape symbols tape:')
        print(self.tape_symbols)
        print('Input symbols tape:')
        print(self.input_symbols)
        print('Accept state tape:')
        print(self.accept_state)
        print('Reject state tape:')
        print(self.reject_state)
        print('Delta function tape:')
        print(self.rules)

    def print_dynamic_tapes(self):
        print('State tape:')
        print(self.state)
        print('Machine tape:')
        print(self.machine_tape)
