"""test"""
def main():
    """test"""
    n = input()
    num = int(n[4:8])
    if n[:2] == "68" and n[2:4] == "07":
        if 328 >= num >= 1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main()
