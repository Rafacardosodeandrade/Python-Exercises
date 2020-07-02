def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")


# 1. Define a function called sign which takes a numerical argument 
# and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.
#
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

# 2. Add "logging" to our to_smash function from the previous exercise.
#
#
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after
    distributing the given number of candies evenly between 3 friends.
    >>> to_smash(91)
    1
    """
    print("Spliting", total_candies, "candies")
    return total_candies % 3
to_smash(91)
# OUTPUT
# Splitting 91 candies
# 1
# 

# That isn't great grammar!
# Modify the definition in the cell below to correct 
# the grammar of our print statement. (If there's only one candy, 
# we should use the singular "candy" instead of the plural "candies")
# Solution: A straightforward (and totally fine) solution is to replace
# the original print call with:

if total_candies == 1:
    print("Splitting 1 candy")
else:
    print("Splitting", total_candies, "candies")
Here's a slightly more succinct solution using a conditional expression:

print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

