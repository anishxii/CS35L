import argparse 
import random
import sys


def parse_range(input):
    try:
        lo,hi = map(int, input.split('-'))
        return lo, hi
    
    except ValueError:
        print(f"Invalid Format: {input}")
        sys.exit(1)
    
        

class randLine:
    def __init__(self, filename):
        self.lines = []
        if filename == '-':
            for line in sys.stdin:
                self.lines.append(line)
        else:
            f = open(filename, 'r')
            self.lines = f.readlines()
            f.close()
    
    def shuf(self):
        random.shuffle(self.lines)

        for each in self.lines:
            print(each, end = '')

    def shuf_repeat_count(self, n):
        for i in range(n):
            print(random.choice(self.lines), end = '')


    def shuf_indef(self):
        while True:
            print(random.choice(self.lines), end = '')
            

    def shuf_count(self, n):
        random.shuffle(self.lines)
        for i in range(n):
            print(self.lines[i % len(self.lines)], end = '')
        

def main():

    parser = argparse.ArgumentParser(prog = "Randline", description = "A GNU Shuf replica written in Python3")

    parser.add_argument('filename', default = '-', nargs = '?', help = "Name of the file to process. If no file is entered, reading from standard input")
    parser.add_argument('--head-count', '-n', action = 'store', dest = 'numlines', help = "Output at most count lines.")
    parser.add_argument('--repeat', '-r', action = 'store_true',dest = 'repeat', default='store_false', help = "Repeat output values, with replacement. \
                                                                                                                If not used with --head-count, will repeat indefinitely.")
    
    parser.add_argument('--input-range', '-i', dest = 'range', type = parse_range, help = "Act as if input came from a file containing \
                                                                                            the range of unsigned decimal integers lo…hi, one per line." )


    args = parser.parse_args()

    if args.range:
        lo = args.range[0]
        hi = args.range[1]
        step = 1

        if lo > hi:
            print("An error occured. High value must be greater than low.")
            sys.exit(1)


        ranged_list = list(range(lo, hi + 1, step))
        random.shuffle(ranged_list)
        for element in ranged_list: 
            print(element)
        return


    gen = randLine(args.filename)

    
    #--head-count
    if args.numlines:
        try:
            numlines = int(args.numlines)
        except ValueError:
            parser.error("invalid Number of Lines: {0}".format(args.numlines))

        if numlines < 0:
            parser.error("negative count: {0}".format(numlines))

        #print(f"The number of lines entered was {numlines}")
        if args.repeat is True:
            gen.shuf_repeat_count(numlines)
        else:
            gen.shuf_count(numlines)
            return
        
    if args.numlines is None and args.repeat is True:
        gen.shuf_indef()
        return
    else:
        gen.shuf()


if __name__ == "__main__":
    main()

