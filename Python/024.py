import itertools
def permute(n):
    permList = [''.join(p) for p in itertools.permutations(str(n))] # Similar to '.split()' in java

    sorted(permList) # Sorts permutations from least to greatest
    return permList[999999] # Returns 1000000th Permutation
print permute('0123456789') 
