import argparse
import sys

def calc(argument):
    if argument.o == "add":
        return argument.x + argument.y
    else:
        return "No operation detected"

if __name__ == '__main__':

    # initialising the parser
    parser = argparse.ArgumentParser()
    
    # adding arguments
    parser.add_argument("--x" , type=float , default=1.0,help="Enter firsr number")
    
    parser.add_argument("--o" , type=str , default="+",help="Enter operation")
    
    parser.add_argument("--y" , type=float , default=1.0,help="Enter 2nd number")

    args = parser.parse_args() # parsing the args.

    sys.stdout.write(str(calc(argument=args))) # write takes string value
