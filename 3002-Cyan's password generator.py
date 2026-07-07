"""Cyan's password generator"""
def main():
    """Cyan's password generator"""
    name = input()
    nameb = input()
    age = input()
    text = ""
    if len(name) >=5 and len(nameb) >=5:
        text = name[:2] + nameb[-1] + age[-1]
        print(text)
    else:
        text = name[:1] + age + nameb[-1]
        print(text)
main()
