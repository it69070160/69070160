"""3019-Safe Password"""
def main():
    """3019-Safe Password"""
    key = input()
    number = int(input())
    if key == "H" and number == 4567:
        print("safe unlocked")
    elif key == "H":
        print("safe locked - change digit")
    elif number == 4567:
        print("safe locked - change char")
    else:
        print("safe locked")
main()
