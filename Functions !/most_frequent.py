W= input('Please enter a string: ')
def most_frequent(string):
    dictionary = dict()
    for key in string:
        if key not in dictionary:
            dictionary[key] = 1
        else:
            dictionary[key] += 1
    return dictionary

print (most_frequent(W))
