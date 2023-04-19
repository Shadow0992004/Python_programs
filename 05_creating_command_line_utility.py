import argparse
import sys

def calc(args):
    if args.o=="add":
        return args.x + args.y

    elif args.o=="sub":
        return args.x - args.y

    elif args.o=="mult":
        return args.x * args.y

    elif args.o=="div":
        return args.x / args.y
    else:
        print("something went wrong")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=1.0, help="Enter 1st no., utility for maths, contact~aryan")

    parser.add_argument("--y", type=float, default=2.0, help="Enter 2nd no., utility for maths, contact~aryan")
    
    parser.add_argument("--o", type=str, default="add", help="utility for maths, contact~aryan for more")

    args=parser.parse_args()

    sys.stdout.write(str(calc(args)))
