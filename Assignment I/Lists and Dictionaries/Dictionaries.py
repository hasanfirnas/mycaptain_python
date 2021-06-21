'''
Dictionary:
	Dictionaries are used to store data values in key:value pairs.
	A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
	Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
'''
# <=================================================================================================>
print(f"Create and print a dictionary:")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"\t{thisdict}\n{'='*80}\n")
# <=================================================================================================>\
print(f"To print value for key")
print(f'\tThe key id give as "brand" and the output :{thisdict["brand"]}\n{"="*80}\n')
# <=================================================================================================>\
print(f"Duplicates Not Allowed:")
thisdict_has_duplicates=	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(f"\tCheak the code to see different{thisdict_has_duplicates}\n{'='*80}\n") 
# <=================================================================================================>\
print(f"Nested Dictionaries:")
print(f"\tA dictionary can contain dictionaries, this is called nested dictionaries. and it also ha list, Tuples, Sets, and any data type")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(f"To Print Nested Dictionaries:")
print(f"\t{myfamily}\n{'='*80}\n")
# <=================================================================================================>\
print(f"List inside Nested Dictionaries:")
mylist = ["apple", "banana", "cherry"]
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}

myfamily = {
  "list" : mylist,
  "child1" : child1,
  "child2" : child2
}
print(f"To Print List and Nested Dictionaries:")
print(f"\t{myfamily}\n{'='*80}\n")
# <=================================================================================================>\


'''
OUTPUT:
λ python3 Dictionaries.py
Create and print a dictionary:
        {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
================================================================================

To print value for key
        The key id give as "brand" and the output :Ford
================================================================================

Duplicates Not Allowed:
        Cheak the code to see different{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
================================================================================

Nested Dictionaries:
        A dictionary can contain dictionaries, this is called nested dictionaries. and it also ha list, Tuples, Sets, and any data type
To Print Nested Dictionaries:
        {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
================================================================================

List inside Nested Dictionaries:
To Print List and Nested Dictionaries:
        {'list': ['apple', 'banana', 'cherry'], 'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}}
================================================================================
'''