import operator
def isPandigital(n): # Checks if a number n is pandigital for example. "12345" is pandigital while "12344" is not.
    stringn = str(n)
    len_of_n = len(stringn)
    for x in xrange(1, len_of_n + 1):
        stringx = str(x)
        if stringx not in stringn:
            return False
    return True

lst = []
for x in xrange(1, 10000): # Guessed and checked the range of this.
    num_string = '' # String to add each multiple to. Because you cant add strings to ints.
    n = 1000 # Guessed and checked this number as well.
    count = 1
    while n > 1 and count != n:
        mult_num = x * count
        num_string = num_string + str(mult_num)
        if len(num_string) == 9 and isPandigital(num_string): # If it is a 1-9 number and pandigital.
            lst.append(int(num_string))
            break
        count += 1
print max(lst) # Print the greatest in a list
