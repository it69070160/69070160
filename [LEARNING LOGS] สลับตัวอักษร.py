"""[LEARNING LOGS] สลับตัวอักษร"""
def main():
    """[LEARNING LOGS] สลับตัวอักษร"""
    text = input().lower()
    textnew = ""
    for i in range(len(text)-1,-1,-1):
        textnew += text[i]
    print(textnew)
main()
