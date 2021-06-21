'''
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
'''

x = ("apple", "banana", "cherry", "apple","cherry")
print(f"x={x}")
print(f"Type of this x is: {type(x)}\n{'='*80}\n")
# <=================================================================================================>
print(f"Convert the tuple into a list:")
y = list(x)
print(f"Type of this x after Convert to list: {type(y)}\n{'='*80}\n")
# <=================================================================================================>
print(f"To count the number of str in tuples:'.count('str')")
print(f'number apple present in it: {x.count("apple")}\n{"="*80}\n')
# <=================================================================================================>
print(f"To find specified value and returns the position of where it was found.")
print(f'the position of srt "banana" in tuple is :{x.index("banana")}')


'''
OUTPUT:
λ python3 Tuples.py
x=('apple', 'banana', 'cherry', 'apple', 'cherry')
Type of this x is: <class 'tuple'>
================================================================================

Convert the tuple into a list:
Type of this x after Convert to list: <class 'list'>
================================================================================

To count the number of str in tuples:'.count('str')
number apple present in it: 2
================================================================================

To find specified value and returns the position of where it was found.
the position of srt "banana" in tuple is :1
'''