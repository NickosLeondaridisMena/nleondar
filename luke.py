# Do NOT use elif statement or nested if-else statement for this assignment.
# You should only need one single if-else statement at most (points will be deducted
# if more than one single if-else statement is used or the dictionary is changed).


# Create a program, luke.py, using the following dictionary:


relations = {'Darth Vader': 'father', 'Leia': 'sister', 'Han': 'brother in law',
             'R2D2': 'droid', 'Rey': 'Padawan', 'Tatooine': 'homeworld'}


# The program will take one argument, corresponding to one of the relations’ keys.
# The program will print out the statement:


#	“Luke, I am your x”
#	Where x = the relationship.


# For example:

# If the argument is Leia, it should print “Luke, I am your sister”
# If the key is ‘Darth Vader’ it should instead print “No, I am your father”

def luke_funct(input):
    if input == "Darth Vader":
        return print("No, I am your " + relations.get(input))
    else:
        return print("Luke, I am your " + relations.get(input))


luke_funct("Darth Vader")

luke_funct("Leia")
