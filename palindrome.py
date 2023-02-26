
# Create a program, palindrome.py, that has a function that takes one string
# argument and prints a sentence indicating if the text is a palindrome.
# The function should consider only the alphanumeric characters in the string,
# and not depend on capitalization, punctuation, or whitespace.

#	If your string is a palindrome it should print:

#	It's a palindrome!

#	If it is not a palindrome, it should print:

#	It's not a palindrome!

#	*Note: please copy and paste these versions into your code
# because the type of apostrophe can differ between IDEs, command
# line, etc.

# import a package to focus only on alphanumerics, aka remove punctuation
from string import punctuation
# import the regex package
import re


def palindrome_funct(input_string):

    # strip the leading and trailing white space
    temp = input_string.strip()

    # strip the remaining punctuation as recommended. This only
    # works if it's at the end of the string
    temp = temp.strip(punctuation)

    # below is some regex to combat incase the punctuation is in
    # the middle of the word
    # I googled the below regular expression
    temp = re.sub(r'[^\w\s]', "", temp)

    # find the reversed variant of the alpha numeric characters
    reversed = temp[::-1]

    # ignore capitalization as recommended
    # check to see the the reverse is the same as the forward
    # and return/print the appropriate statement
    if temp.lower() == reversed.lower():
        return print("It's a palindrome!")
    else:
        return print("It's not a palindrome!")


palindrome_funct(" 1Poo?p1!?")
