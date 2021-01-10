# bounce.py
#
# Exercise 1.5


hit_number = 1
height = 100

while hit_number <= 10:
    height = height * .6
    print(hit_number, round(height, 4))
    hit_number += 1
