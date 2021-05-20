def main():
    # This is program for non decresing numbers.
    greater = -0.000000001
    length = 0
    while True:
        print("Enter a sequence of non-decreasing numbers.")
        num = float(input("Enter num: "))
        if num < greater:
            break
        length += 1
        greater = num 
    print("Thanks for playing!")
    print("Sequence length: ", length)


if __name__ == "__main__":
    main()
