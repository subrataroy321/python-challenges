# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


random_string = input("Give me a string to alphabetize\n")
ordered_chars = sorted(random_string)
ordered_string = "".join(ordered_chars)
print("Alphabetized: {}".format(ordered_string))