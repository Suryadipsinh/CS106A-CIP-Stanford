"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

def main():
    r1 = random.randint(10, 99)
    r2 = random.randint(10, 99)
    print("What is",r1, "+ " +str(r2)+ "?")
    ans_by_user = int(input("Your anser: "))
    right_ans = r1 + r2
    result(right_ans, ans_by_user)

def result(right_ans, ans_by_user):
    if(right_ans == ans_by_user):
        print("Correct!")
    else:
        print("Incorrect. The expected answer is", right_ans)

if __name__ == '__main__':
    main()
