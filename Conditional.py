def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")


# Define a function called sign which takes a numerical argument 
# and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.
#
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

