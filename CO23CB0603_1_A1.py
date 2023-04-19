# take user input for the number of oranges in two boxes
box1 = int(input("Enter the number of oranges in box 1: "))
box2 = int(input("Enter the number of oranges in box 2: "))

# compare the number of oranges using comparison operators
more_oranges = box1 > box2
less_oranges = box1 < box2
same_oranges = box1 == box2
at_least_as_many_oranges = box1 >= box2
at_most_as_many_oranges = box1 <= box2

# print the comparison results
print("Box 1 has more oranges than Box 2:", more_oranges)
print("Box 1 has less oranges than Box 2:", less_oranges)
print("Box 1 and Box 2 have the same number of oranges:", same_oranges)
print("Box 1 has at least as many oranges as Box 2:", at_least_as_many_oranges)
print("Box 1 has at most as many oranges as Box 2:", at_most_as_many_oranges)
