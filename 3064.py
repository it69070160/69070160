"""3065"""
def main():
    """3065"""
    num = int(input())
    if 0 > num:
        print("Error : Please input positive number")
    elif 0 <= num > 9 or not num:
        print("Error : Out of range")
    else:
        if num < 4:
            print("I"*num)
        elif num == 4:
            print("IV")
        elif num == 9:
            print("IX")
        else:
            print("V" + ("I"*(num-5)))
main()
