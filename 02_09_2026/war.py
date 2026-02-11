import stdio
import random
suits = ["diamonds", "hearts", "spades", "clubs"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

deck = []
# for value in values:
for i in range(len(values)):
    for j in range(len(suits)):
        deck.append(values[i] + " of " + suits[j])
#stdio.writeln(deck)

# shuffling.
for i in range(len(deck)):
    randomIndex = random.randint(0, len(deck)-1)
    # swap.
    temp = deck[randomIndex]
    deck[randomIndex] = deck[i]
    deck[i] = temp
#stdio.writeln(deck)


player1Deck = []
player2Deck = []
player1Discard = []
player2Discard = []
# loop unrolling.
for x in range(0, len(deck) // 2, 2):
    player1Deck.append(x)
    player2Deck.append(x+1)
# players 1 - 2

stdio.writeln(player1Deck)
stdio.writeln(player2Deck)
playing = True
while playing:
    # player 1 draws a card.
    player1Card = deck[player1Deck.pop()]
    player2Card = deck[player2Deck.pop()]
    stdio.writeln(str(player1Card) + " vs. " + str(player2Card))
    # conditional.
    if  player1Card > player2Card:
        stdio.writeln("Player 1 wins")
    else:
        stdio.writeln("Player 2 wins")

    playing = False
