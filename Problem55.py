def isPalindrome(strin): # Checks if Palindrome
    instr = str(strin)
    numrev = instr[::-1]
    if instr == numrev:
        return True
    return False

def lychrelNum(n):
    storageInt = n
    reverseNum = int(str(storageInt)[::-1])
    count = 0
    while count < 50: # 50 Iteration Limit
        my_sum = reverseNum + storageInt
        if isPalindrome(my_sum):
            return False
        storageInt = my_sum
        reverseNum = int(str(my_sum)[::-1])
        count += 1
    return True

count = 0
for x in xrange(1, 10001): # 1st 10000 numbers.
    if lychrelNum(x):
        count += 1
print count
