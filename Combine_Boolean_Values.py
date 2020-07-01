# Combining Boolean Values
# You can combine boolean values using the standard concepts of "and", "or", and "not". In fact, the words to do this are: and, or, and not.
#
#With these, we can make our can_run_for_president function more accurate.
#
def can_run_for_president(age, is_natural_born_citizen):
 #   """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)

print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))
False
False
True
#Quick, can you guess the value of this expression?

True or True and False
True

#To answer this, you'd need to figure out the order of operations.

# For example, and is evaluated before or. 
# That's why the first expression above is True.
# If we evaluated it from left to right, we would have calculated
# True or True first (which is True), and then taken the and of that 
# result with False, giving a final value of False.

#You could try to memorize the order of precedence, but a safer bet is to 
# just use liberal parentheses. Not only does this help prevent bugs, 
# it makes your intentions clearer to anyone who reads your code.

#For example, consider the following expression:

prepared_for_weather = have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday
I'm trying to say that I'm safe from today's weather....

# if I have an umbrella...
# or if the rain isn't too heavy and I have a hood...
# otherwise, I'm still fine unless it's raining and it's a workday
# But not only is my Python code hard to read, it has a bug. 
# We can address both problems by adding some parentheses:

prepared_for_weather = have_umbrella or (rain_level < 5 and have_hood) or not (rain_level > 0 and is_workday)
You can add even more parentheses if you think it helps readability:

prepared_for_weather = have_umbrella or ((rain_level < 5) and have_hood) or (not (rain_level > 0 and is_workday))
We can also split it over multiple lines to emphasize the 3-part structure described above:

prepared_for_weather = (
    have_umbrella 
    or ((rain_level < 5) and have_hood) 
    or (not (rain_level > 0 and is_workday))
)