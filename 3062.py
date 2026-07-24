"""Ticket"""
def main():
    """Age"""
    age,char = int(input()), input().lower()

    if age < 18 or char == "s":
        print("20")
    else:
        print("50")

main()
