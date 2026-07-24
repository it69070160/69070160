"""test"""
def main():
    """test"""
    n = int(input())
    m = int(input())
    total = n-m
    if not total:
        print("Good!")
    elif m < n:
        print("Need more cash!")
    else:
        print(abs(total))
main()
