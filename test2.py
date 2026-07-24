"""Noodle"""

cost = int(input())
money = int(input())

if cost == money:
    print("Good!")
elif money < cost:
    print("Need more cash!")
else:
    print(money-cost)
