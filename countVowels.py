
# Create a program called countVowels.py that has a function that takes in a string then prints the number of unique vowels in the string
#  (regardless of it being upper or lower case).

# For example:
# The argument “swEet” should print 1
# The argument “AaaaeeE” should print 2


def count_vowels_function(input_string):

    # This function needs to first take all input strings
    # and put them all into lower case
    input_string = input_string.lower()

    # it's best to utilize sets for this exercise b/c
    # lookups for sets and dictionaries are faster
    # than any other data structure (constant lookup time)
    # in terms of big O complexity and it leverages the fact
    # that if there are duplicates, it won't care,
    # by the nature of it being a set.

    # first create a set of all vowels. Check if you need
    # to include Y. if you do, just add it.

    # we will use this set to look up if it's a vowel or not
    vowels = set(["a", "e", "i", "o", "u"])

    # then we will add this to another set that we call
    # accrued. This is helpful to be a set again because of
    # the fact it will ignore duplicates as well
    accrued = set()

    # iterate through every letter of the input string
    for letter in input_string:
        # if the letter is in the vowel set
        if letter in vowels:
            # add it to our accrued set
            accrued.add(letter)

    # return the number of unique vowels found in the string
    return print(len(accrued))


# test case number 1
count_vowels_function("swEet")
# test case number 2
count_vowels_function("AaaaeeE")
