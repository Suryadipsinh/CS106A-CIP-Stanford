"""
Part A:
At a end of this program there will be printed 10 insted of 5.because in this program both the function have same variable and one 
function can not access the variables of another function.
"""

"""
Part B: 
Edit this code so that it works correctly
"""

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n // 2   # put // for getting 5 instead of 5.0
        return n  # this will return the value of n
    else:
        n = (n + 1) // 2
        return n  # this will return the value of n

def main():
    n = 10
    """
    here I created another variable where we can assign the value
    returned by the function-divide_and_round
    """
    rounded_num = divide_and_round(n)
    # at the end we will print the value of our new varible called rounded_num
    print(rounded_num) 


if __name__ == "__main__":
    main()
