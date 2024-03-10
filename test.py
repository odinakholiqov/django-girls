first_tuple = (1, 2, 3, 4, 5)
second_tuple = (2, 4, 5)

contains_all = (elem in first_tuple for elem in second_tuple)
print(contains_all) # True