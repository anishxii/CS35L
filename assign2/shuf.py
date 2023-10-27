#!/usr/local/cs/bin/python3

import argparse 
import random
import sys


def parse_range(input):
    try:
        lo,hi = map(int, input.split('-'))
        return lo, hi
    
    except ValueError:
        sys.exit(f"Invalid Format: {input}")
    
        

class randLine:
    def __init__(self, filename, echoed = False, predetermined = None ):
        self.lines = []

        if echoed:
            self.lines = [each + '\n' for each in predetermined]
            return

        #Either from standard input or from inputted file
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

    parser = argparse.ArgumentParser(prog = "Randline", description = "A GNU Shuf replica written in Python3", epilog= "Anish Pal UID: 306045492")

    group = parser.add_mutually_exclusive_group()

    parser.add_argument('--head-count', '-n', action = 'store', dest = 'numlines', help = "Output at most count lines.")
    parser.add_argument('--repeat', '-r', action = 'store_true',dest = 'repeat', default='store_false', help = "Repeat output values, with replacement. \
                                                                                                                If not used with --head-count, will repeat indefinitely.")
    
    group.add_argument('--input-range', '-i', dest = 'range', type = parse_range, help = "Act as if input came from a file containing \
                                                                                            the range of unsigned decimal integers lo…hi, one per line." )
    
    parser.add_argument('--echo', '-e', action = "store_true", dest = "echo", help = "Treat each command-line operand as an input line")

    group.add_argument('filename', default = '-', nargs = '*', help = "Name of the file to process. If no file is entered, reading from standard input")

    args = parser.parse_args()

    
    #Check if using a pre-defined file with -i
    if args.range:
        if args.echo:
            print("Cannot use echo and input range at the same time")
            sys.exit(1)
        
        lo = args.range[0]
        hi = args.range[1]
        step = 1

        try: 
            if lo > hi:
                raise ValueError("High value must be greater than low.")
        except ValueError as e:
            sys.exit(f"Error: {e}")


        ranged_list = list(range(lo, hi + 1, step))
        random.shuffle(ranged_list)
        for element in ranged_list: 
            print(element)
        return


    #Using some sort of file, either from std input or filename
    #If no filename is entered, - will be the default file name
    if args.echo:
        gen = randLine("VOID", True, args.filename)
    else:
        gen = randLine(args.filename)

    
    #By this point, a data structure exists with all the file lines in place

    #If head-count is used, begin with that
    if args.numlines:
        try:
            numlines = int(args.numlines)
            #print(numlines)
        except ValueError:
            parser.error("invalid Number of Lines: {0}".format(args.numlines))

        if numlines < 0:
            parser.error("negative count: {0}".format(numlines))

        #Headcount is usually used with repeat flag, check if that is enabled
        if args.repeat is True:
            #with re-selection and count
            gen.shuf_repeat_count(numlines)
            return
        else:
            #Normal shuffle with determined number of lines 
            gen.shuf_count(numlines)
            return
    
    #If repeat functionality is enabled without a count
    if args.numlines is None and args.repeat is True:
        gen.shuf_indef()
        return

    #Default shuffle functionality if all else not used
    gen.shuf()


if __name__ == "__main__":
    main()

