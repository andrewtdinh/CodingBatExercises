def count_dups(arr):
    #This function will count the number of duplicates for each unique element in a list
    return [(x, arr.count(x)) for x in set(arr)]
