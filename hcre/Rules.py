
from .StringReader import StringReader
from .Mangler import Mangler
import sys

class Rules:
    def __init__(self):
        self.rules = []

    def load_rule(self, rule):
        mangler = Mangler()

        rpr = StringReader(rule)

        while rpr.i < len(rpr.string):
            op = rpr.readChar()
            while op == " " and op != None:
                op = rpr.readChar()

            if op == ":":
                pass
            elif op == "l":
                mangler.add_mangler(mangler.mangle_lowercase())
            elif op == "u":
                mangler.add_mangler(mangler.mangle_uppercase())
            elif op == "c":
                mangler.add_mangler(mangler.mangle_capitalize())
            elif op == "C":
                mangler.add_mangler(mangler.mangle_invert_capitalize())
            elif op == "t":
                mangler.add_mangler(mangler.mangle_toggle_case())
            elif op == "T":
                to = rpr.readTo(" ")
                mangler.add_mangler(mangler.mangle_toggle_at(to))
            elif op == "r":
                mangler.add_mangler(mangler.mangle_reverse())
            elif op == "d":
                mangler.add_mangler(mangler.mangle_duplicate())
            elif op == "p":
                times = rpr.readTo(" ")
                mangler.add_mangler(mangler.mangle_duplicate_n(times))
            elif op == "f":
                mangler.add_mangler(mangler.mangle_reflect())
            elif op == "{":
                mangler.add_mangler(mangler.rotate_left())
            elif op == "}":
                mangler.add_mangler(mangler.rotate_right())
            elif op == "$":
                char = rpr.readChar()
                mangler.add_mangler(mangler.mangle_append_character(char))
            elif op == "^":
                char = rpr.readChar()
                mangler.add_mangler(mangler.mangle_prepend_character(char))
            elif op == "@":
                char = rpr.readChar()
                mangler.add_mangler(mangler.mangle_purge(char))
            elif op == "s":
                x = rpr.readChar()
                y = rpr.readChar()
                mangler.add_mangler(mangler.mangle_replace_character(x, y))
            else:
                print("Unknown op: " + op, file=sys.stderr)

        self.add_mangler(mangler)

    def add_mangler(self, mangler):
        self.rules.append(mangler)

    def load_file(self, fn):
        with open(fn) as f:
            for line in f.readlines():
                line = line.strip()
                if len(line) == 0 or line[0] == '#':
                    continue
                
                self.load_rule(line)
                
    
    def mangle(self, string):
        """
        Mangle a string with defined manglers
        """
        mangled = set()
        mangled.add(string)

        for mangler in self.rules:
            mangled.add(mangler.mangle(string))

        return mangled