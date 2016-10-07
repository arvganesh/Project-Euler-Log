from collections import Counter
from pprint import pprint
"""
for card in line:
    if "T" in card:
        card = card.replace("T", "10")
    if "J" in card:
        card = card.replace("J", "11")
    if "Q" in card:
        card = card.replace("Q", "12")
    if "K" in card:
        card = card.replace("K", "13")
    if "A" in card:
        card = card.replace("A", "14")
    lst.append(card)
"""
hierarchy = ["2" ,"3" , "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
cards = ["10H","11H","12H","13H","14H","2C","3S","8S","8D","10D"]
playerOne = cards[:5]
def getHighestValue(deck):
    b = 0
    index = 0
    for val in deck:
        i = int(val[:len(val) - 1])
        if i > b:
            b = i
            index = deck.index(val)
    return index, int(deck[index][:len(deck[index]) - 1])

def checkPair(deck):
    hand = []
    for val in deck:
        hand.append(val[:len(val) - 1])
    count = 0
    c = Counter(hand)
    for key, value in c.iteritems():
        if value == 2:
            return key
    return False

def twoPair(deck):
    hand = []
    for val in deck:
        hand.append(val[:len(val) - 1])
    count = 0
    c = Counter(hand)
    for key, value in c.iteritems():
        if value == 2:
            count += 1
    if count == 2:
        return True
    return False

def threeOfAKind(deck):
    hand = []
    for val in deck:
        hand.append(val[:len(val) - 1])
    count = 0
    c = Counter(hand)
    for key, value in c.iteritems():
        if value == 3:
            return key
    return False

def fourOfAKind(deck):
    hand = []
    for val in deck:
        hand.append(val[:len(val) - 1])
    count = 0
    c = Counter(hand)
    for key, value in c.iteritems():
        if value == 4:
            return key
    return False

def isFullHouse(deck):
    if not not threeOfAKind(deck) and not not checkPair(deck):
        return threeOfAKind(deck)
    return False

def isFlush(deck):
    previous = ""
    c = 0
    for val in deck:
        if val[len(val) - 1] != previous and c > 0:
            return False
        previous = val[len(val) - 1]
        c += 1
    return True

def isStraight(deck):
    c = 0
    previous = 0
    for val in deck:
        if int(val[:len(val) - 1]) != previous and c > 0:
            return False
        previous = int(val[:len(val) - 1]) + 1
        c += 1
    return True

def isRoyalFlush(deck):
    letterDeck = ["10", "11", "12", "13", "14"]
    for val in deck:
        if not isStraight(deck):
            return False
        if val[:len(val) - 1] not in letterDeck:
            return False
        letterDeck.remove(val[:len(val) - 1])
    return True

def isStraightFlush(deck):
    if isStraight(deck) and isFlush(deck):
        return True
    return False

def parse():
    arr = []
    with open("p054_poker.txt", "r") as f:
        text = f.readlines()
        for line in text:
            lst = []
            line = line.rstrip("\n")
            line = line.split(" ")
            for card in line:
                if "T" in card:
                    card = card.replace("T", "10")
                if "J" in card:
                    card = card.replace("J", "11")
                if "Q" in card:
                    card = card.replace("Q", "12")
                if "K" in card:
                    card = card.replace("K", "13")
                if "A" in card:
                    card = card.replace("A", "14")
                lst.append(card)
            arr.append(lst)
    return arr

parse()

"""
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
for hand in handDealt:

"""
handDealt = parse()
p1 = 0
p2 = 0
for hand in handDealt:
    playerOne = hand[:5]
    playerTwo = hand[5:]
    t = playerOne
    p = playerTwo
    var = 0
    val = 0
    # Checks Royal Flushes.
    if isRoyalFlush(playerOne) and not isRoyalFlush(playerTwo):
        p1 += 1
        continue
    elif isRoyalFlush(playerOne) and isRoyalFlush(playerTwo):
        while getHighestValue(t) == getHighestValue(p):
            t.remove(getHighestValue(t))
            p.remove(getHighestValue(p))
            var = getHighestValue(t)
            val = getHighestValue(p)
        if var > val:
            p1 += 1
            continue
        else:
            p2 += 1
            continue

    # Checks Straight Flushes.
    if isStraightFlush(playerOne) and not isStraightFlush(playerTwo):
        p1 += 1
        continue
    elif isStraightFlush(playerOne) and isStraightFlush(playerTwo):
        while getHighestValue(t) == getHighestValue(p):
            t.remove(getHighestValue(t))
            p.remove(getHighestValue(p))
            var = getHighestValue(t)
            val = getHighestValue(p)
        if var > val:
            p1 += 1
            continue
        else:
            p2 += 1
            continue
    # Checks Four of a kind
    if not not fourOfAKind(playerOne) and not fourOfAKind(playerTwo):
        p1 += 1
    elif not not fourOfAKind(playerOne) and not not fourOfAKind(playerTwo):
            while getHighestValue(t) == getHighestValue(p):
                t.remove(getHighestValue(t))
                p.remove(getHighestValue(p))
                var = getHighestValue(t)
                val = getHighestValue(p)
            if var > val:
                p1 += 1
                continue
            else:
                p2 += 1
                continue
    if isFullHouse(playerOne) and not isFullHouse(playerTwo):
        p1 += 1
        continue
    elif isFullHouse(playerOne) and isFullHouse(playerTwo):
        while getHighestValue(t) == getHighestValue(p):
            t.remove(getHighestValue(t))
            p.remove(getHighestValue(p))
            var = getHighestValue(t)
            val = getHighestValue(p)
        if var > val:
            p1 += 1
            continue
        else:
            p2 += 1
            continue

    if isFlush(playerOne) and not isFlush(playerTwo):
        p1 += 1
        continue
    elif isFlush(playerOne) and isFlush(playerTwo):
        while getHighestValue(t) == getHighestValue(p):
            t.remove(getHighestValue(t))
            p.remove(getHighestValue(p))
            var = getHighestValue(t)
            val = getHighestValue(p)
        if var > val:
            p1 += 1
            continue
        else:
            p2 += 1
            continue
    if isStraight(playerOne) and not isStraight(playerTwo):
        p1 += 1
        continue
    elif isStraight(playerOne) and isStraight(playerTwo):
        while getHighestValue(t) == getHighestValue(p):
            t.remove(getHighestValue(t))
            p.remove(getHighestValue(p))
            var = getHighestValue(t)
            val = getHighestValue(p)
        if var > val:
            p1 += 1
            continue
        else:
            p2 += 1
            continue
    if not not threeOfAKind(playerOne) and not threeOfAKind(playerTwo):
        p1 += 1
    elif not not threeOfAKind(playerOne) and not not threeOfAKind(playerTwo):
            while getHighestValue(t) == getHighestValue(p):
                t.remove(getHighestValue(t))
                p.remove(getHighestValue(p))
                var = getHighestValue(t)
                val = getHighestValue(p)
            if var > val:
                p1 += 1
                continue
            else:
                p2 += 1
                continue
    if twoPair(playerOne) and not twoPair(playerTwo):
        p1 += 1
    elif not not twoPair(playerOne) and not not threeOfAKind(playerTwo):
            while getHighestValue(t) == getHighestValue(p):
                t.remove(getHighestValue(t))
                p.remove(getHighestValue(p))
                var = getHighestValue(t)
                val = getHighestValue(p)
            if var > val:
                p1 += 1
                continue
            else:
                p2 += 1
                continue
    if not not checkPair(playerOne) and not checkPair(playerTwo):
        p1 += 1
    elif not not checkPair(playerOne) and not not checkPair(playerTwo):
            while getHighestValue(t) == getHighestValue(p):
                t.remove(getHighestValue(t))
                p.remove(getHighestValue(p))
                var = getHighestValue(t)
                val = getHighestValue(p)
            if var > val:
                p1 += 1
                continue
            else:
                p2 += 1
                continue
print p1, p2
