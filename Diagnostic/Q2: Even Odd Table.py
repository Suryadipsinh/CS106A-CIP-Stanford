# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    # TODO write your solution here
    num = 0
    for i in range(1, 101):
        num += 1
        if num % 2 == 0:
            print(str(num)+ " is even")
        if num % 2 != 0:
            print(str(num)+ " is odd")

if __name__ == "__main__":
    main()
