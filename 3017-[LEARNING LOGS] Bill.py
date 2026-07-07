"""3017-[LEARNING LOGS] Bill"""
def main():
    """3017-[LEARNING LOGS] Bill"""
    total = int(input())
    service = (total * 10)/100
    pay = 0
    if service < 50:
        pay += total + 50
    elif service > 1000:
        pay += total + 1000
    else:
        pay += total + service
    vat = (pay*7)/100
    print(f"{pay+vat:.2f}")
main()
