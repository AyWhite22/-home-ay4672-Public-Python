# chaos3.py
# 11/14/18 by A. White
#Part 5 of 1.1 Computing

def main():

    n = eval(input("How many numbers should I print?"))
    print("This program. illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n) :
        x = 2.0 * x * (1 - x)
        print(x)
main()
