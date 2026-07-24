"""3063 - Safe.py """
def main():
    """SAFE"""
    char,num = input(),input()

    if char == "H" and num == "4567":
        print("safe unlocked")
    elif char == "H":
        print("safe locked - change digit")
    elif num == "4567":
        print("safe locked - change char")
    else:
        print("safe locked")

main()
