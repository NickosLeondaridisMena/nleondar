
# Create a program, shortest.py, that has a function
# that takes in a string argument and prints a sentence
# indicating the shortest word in that string.
# If there is more than one word print only the first.
#  Your print statement should read:


#	“The shortest word is x”


#	Where x = the shortest word.
#  The word should be all uppercase.


def print_shortest_word(input_sentence):

    # we need to split the sentence into separate words
    temp = input_sentence.split()
    # I'm going to initialize a very, very large number
    initial_counter = 10000000000000000000000000000000

    # returned word is just a placeholder. our answer will end up here
    returned_word = ""
    # for every word we come across in this sentence
    for word in temp:
        # if the length of the word is less than our current huge number
        # note by making it strictly LESS, it will return the first occuring shortest
        # letter. If I made it less than or equal to, then it wouldn't work as asked
        if len(word) < initial_counter:
            # you need to replace that large number with the shortest word
            # length so far
            initial_counter = len(word)
            # and update our placeholder variable with our new shortest word
            returned_word = word

    # they asked to return this sentece with it capitalized
    return print("The shortest word is " + returned_word.upper())


# see how I added another 1 letter word afterwards and our output still works?
print_shortest_word("The shortest word is x P")
