# Please Note, This isn't my solution. I originally used a bunch of brute force for loops. 
# I just wanted to add a solution to the github.
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*target

for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]

print "Ways to make change =", ways[target]
