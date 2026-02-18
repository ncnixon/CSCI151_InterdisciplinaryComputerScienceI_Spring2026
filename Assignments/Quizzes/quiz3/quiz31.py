import stdio
import random
suits = ["diamonds", "hearts", "spades", "clubs"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

deck = []
for i in range(len(values)):
    for j in range(len(suits)):
        deck.append(values[i] + " of " + suits[j])
deckLength = len(deck)
stdio.writeln(deckLength)
