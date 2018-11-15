# chaos2.py
# 11/14/18 by A. White
#Part 4 of 1.1 Computing

def main():
    print("This program. illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20) :
        x = 2.0 * x * (1 - x)
        print(x)
main()
