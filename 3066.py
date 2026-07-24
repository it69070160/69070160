"""3066"""
def main():
    """3066"""
    x,y,z = input(),input(),input()
    if x == y == z:
        print("all the same")
    elif x != y and y != z and z != x:
        print("all different")
    else:
        print("neither")
main()
