# chaos.py
# 11/13/18 by A. White 
# Part 3 of 1.1 Computing

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10) :
        x = 2.0 * x * (1 - x)
        print(x)
main()


# What I've noticed is that there's a difference between the original
#and the most recent version of the chaos outline is that since you're
#multiplying the "x" by 2.0 and not 3.9, the 10 values of the equation
#is lower than the original's version. And I've also noticed that the
#values in the original version is more similar than the numbers in the
#most recent version.

