"""
Hailstone sequence:--
if the given number is even then take half and
if odd then take 3n + 1 until the number becomes 1.
then count the steps and print it.
"""

import random 

def main():
    step = 0
    # takes a number from user
    num = int(input("Enter a number: "))
    # this while loop will run until the given number becomes 1
    while num != 1:
        # if the  number is even then take the half of the number
        if num % 2 == 0 :
            even = num/2
            print(str(num)+ " is even, so I take half: "+ str(even))
            num = even
            step += 1
        # if the number is odd then take 3n + 1 of the number
        else :
            odd = 3*num + 1
            print(str(num)+ " is odd, so I make 3n + 1: "+ str(odd))
            num = odd
            step += 1
    # prints the total number of steps 
    print("The process took "+str(step)+" steps to reach 1")

if __name__ == "__main__":
    main()
