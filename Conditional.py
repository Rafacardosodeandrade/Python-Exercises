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


#######
#1#
def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

#2#
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

#3#
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and not mustard and not onion

#4# 
def exactly_one_souce(ketchup, mustard, onion):
    """Return wheter the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")"""
    return (ketchup and not mustard) or (mustard and not ketchup)

#5#MINE SOLUTION
def exactly_one_topping(ketchup, mustard, onion)
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (ketchup and not mustard and not onion) or (mustard and not ketchup and not onion) or (onion and not ketchup and not mustard)

#5#SOLUTION B
return (ketchup + mustard + onion) == 1

#5#SOLUTION C
return (int(ketchup) + int(mustard) + int(onion)) == 1

#BLACKJACK
def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    return False


#LISTS
"""Return the second element of the given list. If the list has no second
    element, return None.
    """
    (L)

def select_second(L):
    if len(L) < 2:
        return None
    return L[1]
    