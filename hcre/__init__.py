from .Rules import Rules
import sys

def main():
    rules = Rules()
    for rulefile in sys.argv[1::]:
        rules.load_file(rulefile)
    
    try:
        line = sys.stdin.readline()
        while line:
            line = line.strip()
            print("\n".join(rules.mangle(line)))
            line = sys.stdin.readline()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()