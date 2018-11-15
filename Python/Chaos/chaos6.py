# chaos6.py
# 11/14/18 by A. White
#Part 6c of 1.1 Computing

def main():
    print("This program illustrates chaotic function")
    x = eval(input("Enter a number between 0 and 1:"))
    for i in range(100) :
        x = 3.9 * x - 3.9 * x * x
        print(x)
main()
