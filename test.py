"""test1"""

ID = str(input())

if ID[0:2] == "68" and ID[2:4] == "07" and 0 < int(ID[4:]) < 329:
    print("Yes")
else:
    print("No")
