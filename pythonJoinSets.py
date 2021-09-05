
#using union method
# set1 = {"a","b","c","d"}
# set2 = {"a","e","g","c"}
# print("using union method")
# set3 = set1.union(set2)
# print(set3)

# set1 = {"a","b","c","d"}
# set2 = {"a","e","g","c"}
# set1.update(set2)
# print(set1)

#example intersection
# set1 = {"a","b","c","d"}
# set2 = {"a","e","g","c"}
# set3 = set1.intersection(set2)
# print(set3)

#example using intersection update method
# set1 = {"a","b","c","d"}
# set2 = {"a","e","g","c"}
# set1.intersection_update(set2)
# print(set1)

#symmetric diff in sets
set1 = {"a","b","c","d"}
set2 = {"a","e","g","c"}
set3 = set1.symmetric_difference(set2)
print(set3)

#symmetric diff update
set1 = {"a","b","c","d"}
set2 = {"a","e","g","c"}
set1.symmetric_difference_update(set2)
print(set1)