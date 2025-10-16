#----------set = unordered collection and contains unique element. cannot be duplicate----------

# set = {'laptop', 'phone', 'mac', 'ipad', 'laptop', 'iphone'}
# print("Number of item in set are: ", len(set))
# for i in set:
#     print(i, end=" ")

#-----------clear() = remove all items in set--------------------------

# set = {'laptop', 'phone', 'mac', 'ipad', 'laptop', 'iphone'}
# print("Number of item in set are: ", len(set))
# set.clear()
# print(f"After clear the number in item is: ", len(set))
# for i in set:
#     print(i, end=" ")

#----------remove() = update set / remove items in set---------------------------

# set = {'laptop', 'phone', 'mac', 'ipad', 'laptop', 'iphone'}
# print("Number of item in set are: ", len(set))
# for i in set:
#     print(i, end=" ")

# set.remove('laptop')
# print(f"After removing one item in set: ", len(set))
# for i in set:
#     print(i, end=" ")

#--------------union() - return new set from both sets-----------------------

#duplicate items is not shown

# set_a = {100,200,350,400}
# set_b = {22,33,44,55}
# set_c = {1,2,3,4}

# print(f"\nFirst set contains {len(set_a)} items")
# print(set_a)
# print(f"Second set contains {len(set_b)} items")
# print(set_b)
# print(f"Second set contains {len(set_c)} items")
# print(set_c)

# unionset=set_a.union(set_b,set_c)
# print(f"Union first and second set contains {len(unionset)} items")
# print(unionset)

#-----------intersection - return set which is common element in sets--------------------------

# set_a = {100,200,350,400}
# set_b = {22,33,44,55,100}
# set_c = {1,2,3,4,100}

# print(f"\nFirst set contains {len(set_a)} items")
# print(set_a)
# print(f"Second set contains {len(set_b)} items")
# print(set_b)
# print(f"Second set contains {len(set_c)} items")
# print(set_c)

# newset=set_a.intersection(set_b,set_c)
# print(f"Intersection in first and second set contains {len(newset)} items")
# print(newset)

#-------------difference - return set which contains in s1 not s2------------------------

set_a = {100,200,350,400}
set_b = {22,33,44,55,100}

print(f"\nFirst set contains {len(set_a)} items")
print(set_a)
print(f"Second set contains {len(set_b)} items")
print(set_b)

newset=set_a.difference(set_b)
print(f"Difference in first and second set contains {len(newset)} items")
print(newset)











   