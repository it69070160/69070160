"""การตรวจสอบบัตรประชาชน"""
def main():
    """การตรวจสอบบัตรประชาชน"""
    number = input()
    if len(number) == 13:
        print("yes")
    else:
        print("no")
main()
