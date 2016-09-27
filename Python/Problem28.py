def diagonalNum(n): # n is the number of rows.
    increment = 2
    getDiaNum = 1
    sumOfNums = 0
    count = 1
    limit = (n-1)/2 # How Many Squares(excluding the first one) are added before answer. ex 5 rows : 2 squares, 7 : 3 etc.
    for i in xrange(1, limit + 1): # 1 all the way until the limit
        while count <= 4: # Four Numbers Per square
            getDiaNum += increment # Each Number in the square(1,3,5,7,9,13 etc)
            sumOfNums += getDiaNum # Sum of total numbers checked.
            count += 1             
        increment += 2 # Every four numbers, count increases by two.
        count = 1 # Resetting the value of count.
    return sumOfNums + 1 # Didn't count the 1st box(which had "1")

print diagonalNum(1001) 
