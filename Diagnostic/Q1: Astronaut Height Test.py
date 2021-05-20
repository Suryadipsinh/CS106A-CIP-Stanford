def main():
    # this program will check height of Austonaut
    height = float(input("Enter your height in meters: "))
    while height <= 0:
        print("please Enter a valid height")
        height = float(input("Enter your height in meters: "))

    if (height > 1.6 and height < 1.9) :
        print("Correct height to be an astronaut")
    elif height < 1.6 :
        print("Below minimum astronaut height")
    elif height > 1.9 :
        print("Above maximum astronaut height")

if __name__ == "__main__":
    main()
