"""Elo"""
def main():
    """Elo"""
    ra = int(input())
    rb = int(input())
    strn = input()
    ea = 1 / (1+10**((rb-ra)/400))
    eb = 1 / (1+10**((ra-rb)/400))
    ea = round(ea ,2)
    eb = round(eb ,2)
    if strn == "A":
        print(f"{ea:.2f}")
    else:
        print(f"{eb:.2f}")
main()
