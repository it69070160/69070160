"""หาระยะทางระหว่างจุด 3D"""
import math
def main():
    """หาระยะทางระหว่างจุด 3D"""
    x, y, z = map(int,input().split())
    x2, y2, z2 = map(int,input().split())
    d = math.sqrt(((x-x2)**2)+((y-y2)**2)+((z-z2)**2))
    print(f"{d:.2f}")
main()
