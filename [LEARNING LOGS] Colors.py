"""[LEARNING LOGS] Colors"""
def main():
    """[LEARNING LOGS] Colors"""
    color_one = input().lower()
    color_two = input().lower()
    if set([color_one,color_two]) == set(["red","yellow"]):
        print("Orange")
    elif set([color_one,color_two]) == set(["red","blue"]):
        print("Violet")
    elif set([color_one,color_two]) == set(["yellow","blue"]):
        print("Green")
    elif set([color_one,color_two]) == set(["red"]):
        print("Red")
    elif set([color_one,color_two]) == set(["yellow"]):
        print("Yellow")
    elif set([color_one,color_two]) == set(["blue"]):
        print("Blue")
    else:
        print("Error")
main()
