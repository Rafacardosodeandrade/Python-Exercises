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
"""1. Return the second element of the given list. If the list has no second
    element, return None.
    """
    (L)

def select_second(L):
    if len(L) < 2:
        return None
    return L[1]

# You are analyzing sports teams. Members of each team are stored in a list. 
# The Coach is the first name in the list, the captain is the second name in
# the list, and other players are listed after that. These lists are stored 
# in another list, which starts with the best team and proceeds through the 
# list to the worst team last. 
# Complete the function below to select the captain of the worst team.

"""2. Given a list of teams, where each team is a list of names, return the 
2nd player (captain) from the last listed team
    """
def losing_team_captain(teams):
    return teams[-1][1]    

#LOOPS AND LIST COMPREHENSIONS
#DEBUGGING

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False

#SOLUTION
def has_lucky_number(nums):
    return any([num % 7 == 0 for num in nums])

# R and Python have some libraries (like numpy and pandas) compare each element of the 
# list to 2 (i.e. do an 'element-wise' comparison) and give us a list of booleans like
#  `[False, False, True, True]`. 
# Implement a function that reproduces this behaviour, returning a list of booleans 
# corresponding to whether the corresponding element is greater than n.

def element_greater_than(L, thresh)
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    pass

def element_greater_than(L, tresh):
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res

    #otherwise
def element_greater_than(L,thresh)
    return [ele > thresh for ele in L]

#3_
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
#solution
def menu_is_boring(meals):
    #Interate over all indices of the list, except the last one
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False

#STRING AND DICTIONARY
# There is a saying that "Data scientists spend 80% of their time cleaning data, 
# and 20% of their time complaining about cleaning data." Let's see if you can
# write a function to help clean US zip code data. Given a string, it should 
# return whether or not that string represents a valid zip code. 
# For our purposes, a valid zip code is any string consisting of exactly 5 digits.

# HINT: str has a method that will be useful here. Use help(str) to review a list 
# of string methods

def is_valid_zip(zip_code):
    return len(zip_code) == 5 and zip_code.isdigit()


##############
# EXERCISE 2 #
#            ##########################################################################
# A researcher has gathered thousands of news articles. But she wants to focus her 
# attention on articles including a specific word. Complete the function below to 
# help her filter her list of articles.
#
# Your function should meet the following criteria:
#
# Do not include documents where the keyword string shows up only as a part of a larger word. 
# For example, if she were looking for the keyword “closed”, you would not include the 
# string “enclosed.”
# She does not want you to distinguish upper case from lower case letters. So the phrase
#  “Closed the case.” would be included when the keyword is “closed”
# Do not let periods or commas affect what is matched. “It is closed.” 
# would be included when the keyword is “closed”. But you can assume there are no other 
# types of punctuation.

def word_search(doc_list, keyword):
    # List to hold the indices of matching documents
    indices = []
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(doc_list):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word, and it's set of all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

# Now the researcher wants to supply multiple keywords to search for. 
# Complete the function below to help her.
# (You're encouraged to use the word_search function you just wrote when 
# implementing this function. Reusing code in this way makes your programs 
# more robust and readable - and it saves typing!)
#
def multi_word_search (doc_list, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(doc_list, keyword)
    return keyword_to_indices

# WORKING WITH EXTERNAL LIBRARIES
# After completing the exercises on lists and tuples, Jimmy noticed that, 
# according to his estimate_average_slot_payout function, the slot machines 
# at the Learn Python Casino are actually rigged against the house, 
# and are profitable to play in the long run.

# Starting with $200 in his pocket, Jimmy has played the slots 500 times, 
# recording his new balance in a list after each spin. He used Python's 
# matplotlib library to make a graph of his balance over time:

# CODE
# Import the jimmy_slots submodule
from learntools.python import jimmy_slots
# Call the get_graph() function to get Jmmy's graph
graph = jimmy_slots.get_graph()
graph

# As you can see, he's hit a bit of bad luck recently. He wants to tweet this along with some choice emojis, but, as it looks right now, his followers will probably find it confusing. He's asked if you can help him make the following changes:

# Add the title "Results of 500 slot machine pulls"
# Make the y-axis start at 0.
# Add the label "Balance" to the y-axis
# After calling type(graph) you see that Jimmy's graph is of type matplotlib.axes._subplots.AxesSubplot. Hm, that's a new one. By calling dir(graph), you find three methods that seem like they'll be useful: .set_title(), .set_ylim(), and .set_ylabel().

# Use these methods to complete the function prettify_graph according to Jimmy's requests. We've already checked off the first request for you (setting a title).

# (Remember: if you don't know what these methods do, use the help() function!)

def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Result of 500 slot machine pulls")
    # Make the y-axis begin at 0
    graph.set_ylim(bottom=0) 
    # Label the yaxis
    graph.set_ylabel("Balance")
    # Bonus: format the numbers on the y-axis as dollar amounts
    # An array of the values displayed on the y-axis (150, 175, 200, etc.)
    ticks = graph.get_yticks()
    # Format those values into strings beginning with dollar sign
    new_labels = ['${}'.format(int(amt)) for amt in ticks]
    # Set the new labels
    graph.set_yticklabels(new_labels)
    
# 2. 🌶️🌶️
# This is a very hard problem. Feel free to skip it if you are short on time:

# Luigi is trying to perform an analysis to determine the best items for winning races 
# on the Mario Kart circuit. He has some data in the form of lists of 
# dictionaries that look like...

[
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    # Sometimes the racer's name wasn't recorded
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]
'items' is a list of all the power-up items the racer picked up in that race, and 'finish' 
was their placement in the race (1 for first place, 3 for third, etc.).

# He wrote the function below to take a list like this and return a dictionary mapping 
# each item to how many times it was picked up by first-place finishers.

def best_items(racers):
    """GIven a list of racer dictionaries, return a dictionary mapping items to the number 
    of times those items were picked up by racers who finished in first place.
    """
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interessed in racers who finished in first
        if racer['finish'] == 1:
            for i in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] +=1
        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encoutered racer with unknown name on interation {}/{} (racer = {})".format(i+1, len(racers), racer['name']))
    return winner_item_counts


# He tried it on a small example list above and it seemed to work correctly:

sample = [
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]
best_items(sample)

#OUTPUT
# WARNING: Encountered racer with unknown name on iteration 3/4 (racer = None)
# {'green shell': 2, 'mushroom': 1}

# However, when he tried running it on his full dataset, the program crashed with a TypeError.

# Can you guess why? Try running the code cell below to see the error message Luigi is getting.
# Once you've identified the bug, fix it in the cell below (so that it runs without any errors).

# Hint: Luigi's bug is similar to one we encountered in the tutorial when we talked about star imports.

def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for item in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts

# Try analyzing the imported full dataset
best_items(full_dataset)

##############################  EXERCISE => BLACKJACK
#  
# Suppose we wanted to create a new type to represent hands in blackjack. One thing we might want to do with 
# this type is overload the comparison operators like > and <= so that we could use them to check whether one 
# hand beats another. e.g. it'd be cool if we could do this:
#
# >>> hand1 = BlackjackHand(['K', 'A'])
# >>> hand2 = BlackjackHand(['7', '10', 'A'])
# >>> hand1 > hand2
# True
# Well, we're not going to do all that in this question (defining custom classes is a bit beyond the scope of these lessons), 
# but the code we're asking you to write in the function below is very similar to what we'd have to write if we were 
# defining our own BlackjackHand class. (We'd put it in the __gt__ magic method to define our custom behaviour for >.)
#
# Fill in the body of the blackjack_hand_greater_than function according to the docstring.
#
#
# REQUIRMENTS 
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """

def hand_total(hand):
    """Helper function to calculate the total points of a blackjack hand.
    """
    total = 0
    # Count the number of aces and deal with how to apply them at the end.
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            # Convert number cards (e.g. '7') to ints
            total += int(card)
    # At this point, total is the sum of this hand's cards *not counting aces*

    # Add aces, counting them as 1 for now. This is the smallest total we can make from this hand
    total += aces
    # "Upgrade" aces from 1 to 11 as long as it helps us get closer to 21
    # without busting
    while total + 10 <= 21 and aces > 0:
        # Upgrade an ace from 1 to 11
        total += 10
        aces -= 1
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)




       




