
# Create a program called capCount.py that has a function
#  that takes in a string and prints the number of capital
# letters in the first line, then prints the sum of their
#  indices in the second line.


# The string “hEllo, World” would should look like this:
# 2
# 8
def cap_counter(input_string):

    # it's best to create a new variable that keeps track of all lower case letters
    # note that punctuations and spaces will also be captured here
    # make it a set for fast operations (but not required)
    lower_case_variant = set(input_string.lower())

    # create a counter that counts the number of capital letters
    capital_counter = 0

    # create a counter that also keeps track of the index
    index_counter = 0

    # I'm going to use a list to keep track of the indexes of capital letters
    # You could probably use a set, or a running sum, but this is what came
    # to my mind the easiet
    index_list = []

    # check for every letter
    for letter in input_string:

        # if the letter isn't captured in the lower case variant
        # note this will only capture upper case letters
        if letter not in lower_case_variant:
            # if it's true, increment the number of capital letters found
            capital_counter = capital_counter + 1
            # and log the index it occured at
            index_list.append(index_counter)
        # make sure you increment the counter outside the for-loop so it happens
        # on every iteration.
        index_counter = index_counter + 1

    print(capital_counter)
    print(sum(index_list))

    return


cap_counter("hEllo, World")
