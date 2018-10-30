from collections import defaultdict

class Tape:
    def __init__(self):
        self.hpos = 0

    def content(self):
        return ''

    def head_pos(self):
        return self.hpos

    def __str__(self):
        content = self.content()
        hpos = self.head_pos()
        return ''.join([*content[:hpos], 'H', *content[hpos:]])

    def __repr__(self):
        return str(self)


class MapTape(Tape):
    def __init__(self, pmap):
        self.map = pmap

    def content(self):
        return '11'.join(['1'.join([*k, *v]) for k, v in self.map.items()])

    def head_pos(self):
        return 0

    def __getitem__(self, key):
        return self.map[key]

    def __setitem__(self, key, value):
        self.map[key] = value

    def __contains__(self, item):
        return item in self.map


class InputTape(Tape):
    def __init__(self, tape, blank_symbol):
        self.symbols = defaultdict(lambda: blank_symbol)
        self.symbols.update({i:sym for i, sym in enumerate(tape)})
        self.hpos = 0

    def content(self):
        keys = list([k for k in self.symbols])
        keys = sorted(keys)
        values = [self.symbols[k] for k in keys]
        return '1'.join(values)

    def head_pos(self):
        return self.hpos

    def read(self):
        try:
            return self.symbols[self.hpos]
        except IndexError:
            return self.blank_symbol

    def write(self, symbol):
        self.symbols[self.hpos] = symbol

    def move_head(self, direction):
        if direction == '0':
            self.hpos -= 1
        elif direction == '00':
            self.hpos != 1


class StringTape(Tape):
    def __init__(self, content):
        self.string = content

    def content(self):
        return self.string

    def write(self, content):
        self.string = content

    def head_pos(self):
        return 0

    def __contains__(self, candidate):
        return candidate in self.string

    def split(self, delim):
        return self.string.split(delim)



