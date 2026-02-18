import stdio

colors = ["red", "yellow", "green", "blue"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
actionCards = ["skip", "reverse", "draw two"]

deck = []

# Add one 0 per color
for color in colors:
    deck.append("0 of " + color)

# Add two of each 1–9 per color
for color in colors:
    for number in numbers:
        deck.append(number + " of " + color)
        deck.append(number + " of " + color)

# Add two of each action card per color
for color in colors:
    for action in actionCards:
        deck.append(action + " of " + color)
        deck.append(action + " of " + color)

# Add wild cards (no color)
for i in range(4):
    deck.append("wild")
    deck.append("wild draw four")

# Print the length of the deck
deckLength = len(deck)
stdio.writeln(deckLength)