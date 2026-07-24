"""3067"""
def main():
    """3067"""
    x,y,z = float(input()),float(input()),float(input())
    if z > y > x:
        print("increasing")
    elif x > y > z:
        print("decreasing")
    else:
        print("neither")
main()
