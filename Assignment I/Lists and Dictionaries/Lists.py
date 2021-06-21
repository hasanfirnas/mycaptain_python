'''
Lists are used to store multiple items in a single variable.
	Ordered:
	When we say that lists are ordered, it means that the items have a defined order, 
		and that order will not change.
	If you add new items to a list, the new items will be placed at the end of the list.
'''
# <=================================================================================================>
print(f"A list with strings, integers and boolean values:") 
list1 = ["abc", 34, True, 40, "male"]
print(f"\tlist = {list1}\n \ttype of the list is:{type(list1)}\n \tType of data inside list[4]:{type(list1[3])}\n{'='*80}\n")
# <=================================================================================================>
print(f"To change the value of a specific item, refer to the index number:")
list1[0] = "xyz"
list1[2] = False
print(f"\tAfter the change list={list1}\n{'='*80}\n")
# <=================================================================================================>
print(f"Range of Indexes:")
print(f"\tTo find lenth of list= {len(list1)}")
print(f"\tTo print a pirticult range in list={list1[1:3]}\n{'='*80}\n")
# <=================================================================================================>
print(f"Copy a List:")
print(f"\tTo copy a list '.copy()' this will help us")
list2=list1.copy()
list2[0] = "hello"
print(f"\tCopied list1 to list2={list2}\n{'='*80}\n")
# <=================================================================================================>
print(f"Join Two Lists:")
print(f"\tThere are several ways to join a list")
print(f"\t# Using '+' : {list1+list2}")
print(f"\t# Using for loop and adding one by to a list")
for x in list2:
  list1.append(x)
print(f"\t  The list after for loop {list1}")
list1 = ["abc", 34, True, 40, "male"] ##### re-assigning the list
list1.extend(list2)
print(f"\t# Using '.extend() funtion : {list1}")
num_list=["9","0","6","4","1","3","0"]
print(f"\t# To sort the list sorted() will help us \n\t  After the sorted funtion{sorted(num_list)}\n{'='*80}\n")
# <=================================================================================================>
print(f"To find more about list https://stackoverflow.com/search?q=python+lsit")



'''
OUTPUT:
λ python3 Lists.py
A list with strings, integers and boolean values:
        list = ['abc', 34, True, 40, 'male']
        type of the list is:<class 'list'>
        Type of data inside list[4]:<class 'int'>
================================================================================

To change the value of a specific item, refer to the index number:
        After the change list=['xyz', 34, False, 40, 'male']
================================================================================

Range of Indexes:
        To find lenth of list= 5
        To print a pirticult range in list=[34, False]
================================================================================

Copy a List:
        To copy a list '.copy()' this will help us
        Copied list1 to list2=['hello', 34, False, 40, 'male']
================================================================================

Join Two Lists:
        There are several ways to join a list
        # Using '+' : ['xyz', 34, False, 40, 'male', 'hello', 34, False, 40, 'male']
        # Using for loop and adding one by to a list
          The list after for loop ['xyz', 34, False, 40, 'male', 'hello', 34, False, 40, 'male']
        # Using '.extend() funtion : ['abc', 34, True, 40, 'male', 'hello', 34, False, 40, 'male']
        # To sort the list sorted() will help us
          After the sorted funtion['0', '0', '1', '3', '4', '6', '9']
================================================================================

To find more about list https://stackoverflow.com/search?q=python+lsit

'''