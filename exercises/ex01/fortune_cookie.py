"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730409119"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
from random import randint

print("Your fortune cookie says...")

fortune_value: int= randint(1,40)

if fortune_value <10:
    print("Patience is the key to a happy life")
else:
    if fortune_value <20:
        print("Hard work beats talent when talent fails to work hard")
    else: 
        if fortune_value <30:
            print("You learn more from failure than from success")
        else: 
            if fortune_value <40:
                print("A life full of good fortune awaits you")
print("Now, go spread positive vibes!")
