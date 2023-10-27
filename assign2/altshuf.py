import argparse
import string
import random


class shuf:
    def __init__(self, filename):
        f = open(filename, 'r')
        self.lines = f.readlines()
        f.close()
        random.shuffle(self.lines)

    def chooseLine(self):
        return random.choice(self.lines)

def shuffle_array(self):
    random.shuffle(self.lines)
    return self.lines

def main():
    parser = argparse.ArgumentParser(prog='shuf', description='shuffles any input you desire!', epilog='Pranav Puranam 35L | UID: 205993404');
    inputs = parser.add_mutually_exclusive_group()
    inputs.add_argument('infile', nargs='?')
    inputs.add_argument('-e', '--echo', nargs='*', action='append', dest='lines', default=[],
    help="enter input to be shuffled (default [])")
    inputs.add_argument('-i lo-hi', '--input-range=lo-hi', action='store', dest = 'ranges', type=str, default="",
    help="use a range of integers as input")
    parser.add_argument('-n', '--head-count', action='store', dest='head_count', type=int, default=None,
    help="output at most head-count lines")
    parser.add_argument('-r', '--repeat', action='store_true', dest='repeat_flag', default=False,
    help="repeat process or not")
    args = parser.parse_args()
    try:
        count = args.head_count
        if count and count < 0:
            parser.error("Head count must be positive")
        if args.infile and args.infile != '-':
            try:
                generator = shuf(args.infile)
                for token in generator.lines:
                    print(token)
                    if count != None:
                        count -= 1
                    if count <= 0:
                        break
                while args.repeat_flag:
                    if count != None:
                        if count > 0:
                            count -= 1
                        else:
                            break
                    print(generator.chooseLine())
            except:
                parser.error("Input file not found")
        elif len(args.lines) != 0 and len(args.ranges) != 0:
            parser.error("Cannot use -i and -e arguments together")
        elif len(args.lines) != 0:
            try:
                elements = args.lines[0]
                random.shuffle(elements)
                for token in elements:
                    print(token)
                    if count != None:
                        count -= 1
                        if count <= 0:
                            break
                while args.repeat_flag:
                    if count != None:
                        if count > 0:
                            count -= 1
                        else:
                            break
                    print(random.choice(elements))
            except:
                parser.error("Invalid Arguments")
        elif len(args.ranges) != 0:
            try:
                arr = args.ranges.split('-')
                start, end = int(arr[0]), int(arr[1]) + 1
                if end < start:
                    raise ValueError
    # parser.error("Invalid input range")
                elements = [x for x in range(int(arr[0]), int(arr[1]) + 1)]
                random.shuffle(elements)
                for token in elements:
                    print(token)
                    if count != None:
                        count -= 1
                    if count <= 0:
                        break
                while args.repeat_flag:
                    if count != None:
                        if count > 0:
                            count -= 1
                        else:
                            break
                    print(random.choice(elements))
            except:
                parser.error("Invalid range input")
            else:
                try:
                    lines = []
                    for line in sys.stdin:
                        lines.append(line)
                        random.shuffle(lines)
                    for token in lines:
                        print(token)
                        if count != None:
                            count -= 1
                            if count <= 0:
                                break
                    while args.repeat_flag:
                        if count != None:
                            if count > 0:
                                count -= 1
                            else:
                                break
                        print(random.choice(lines))
                except:
                    parser.error("Invalid input from stdin")
    except:
    # parser.error("Invalid Input")
        pass

if __name__ == "__main__":
    main()