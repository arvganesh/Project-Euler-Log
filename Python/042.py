def getTriangleNum(n): # Nth Triangular Number.
    lst = []
    for i in xrange(1, n + 1):
         trinum = (i*(i+1))/2
         lst.append(trinum)
    return lst

# Credit to Alex Koren for lines 9 - 12
input_file = open("words.txt") # Reads File "words.txt", from project directory.
text = input_file.read()
text.replace('','') # replaces the commas.
words = text.split(',') # Removes them.
triangleList = getTriangleNum(100) # Generates 100 Triangular Numbers

def toAscii(s): # Converts word to number for example, "A" is one and "B" is two and so on. The function adds up all of them in the word. For example, "ABCD" returns 10.
    number = 0
    for character in s:
        number += ord(character) - 64
    return number

count = 0 # Number of Triangular Numbers
for word in words:
    w = word[1:-1] # Removes Quotations Around the words in the file.
    number = toAscii(w) # Generates the number for the word.
    if number in triangleList: # Checks if its a triangle number
        count += 1 # increases count by one.
print count # Prints out answer :D
