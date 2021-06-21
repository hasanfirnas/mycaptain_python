'''
Sets are used to store multiple items in a single variable.
A set is a collection which is both unordered and unindexed.
'''
thisset = {"apple", "banana", "cherry"}
print(f"thisset={thisset}\n{'='*80}\n")
# <=================================================================================================>
print(f"To finf the number of item is set: {len(thisset)}\n{'='*80}\n")
# <=================================================================================================>
set1 = {"abc", 34, True, 40, "male"}  
print(f"the order of set will sorted and it has no index: {set1}\n{'='*80}\n")
# <=================================================================================================>
print(f"To add a item in set:")
thisset.add("orange")
print(f"thisset={thisset}\n{'='*80}\n")
# <=================================================================================================>
print("Add Any Iterable:")
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(f"After update a list to set :{thisset}\n{'='*80}\n")

'''
OUTPUT:
λ python3 Sets.py
thisset={'cherry', 'apple', 'banana'}
================================================================================

To finf the number of item is set: 3
================================================================================

the order of set will sorted and it has no index: {True, 34, 40, 'male', 'abc'}
================================================================================

To add a item in set:
thisset={'cherry', 'apple', 'orange', 'banana'}
================================================================================

Add Any Iterable:
After update a list to set :{'cherry', 'kiwi', 'orange', 'banana', 'apple'}
================================================================================
'''