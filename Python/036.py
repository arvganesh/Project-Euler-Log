get_bin = lambda x: format(x, 'b') # Gets binary of a number. Found on stackoverflow. Python also has a built in "bin()" but i didnt know that :D

def isPalindrome(strin): # Checks if Palindrome
    instr = str(strin)
    numrev = instr[::-1]
    if instr == numrev:
        return True
    return False

my_sum = 0
for i in xrange(1, 1000001):
    if isPalindrome(i) and isPalindrome(get_bin(i)): # Checks if i is a Palindrome and if the binary of i is a Palindrome
        my_sum += i # Adding i to a variable.
print my_sum
