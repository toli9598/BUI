import sys
import lib.greet as greet
import lib.print_time as time

def main ():
    name = "world"
    if __name__ == "__main__" and sys.argv.__len__() >= 2 : name = sys.argv[1]
    print(greet.getGreet(name))
    time.printTime()
