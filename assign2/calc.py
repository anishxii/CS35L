import argparse
import sys

parser = argparse.ArgumentParser(prog="Two Calc", description="A simple, two argument calculator")

#parser.add_argument('--mult', '-m', action = 'store', dest = 'm_sign')

parser.add_argument('arg1', action = 'store', help = "The first operand")
parser.add_argument('arg2', action = 'store',  help = "The second operand")


args = parser.parse_args()


try:
    print(int(args.arg1) + int(args.arg2))
except ValueError:
    print("Not formatted properly")