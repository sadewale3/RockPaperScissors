import sys

player1 = input("What is the name of Player1? ")
player2 = input("What is the name of Player2? ")
player1_a = input("%s - rock, paper or scissors? " % player1)
player2_a = input("%s - rock, paper or scissors? " % player2)

def compare(p1, p2):
    if p1 == p2:
        return("Tied!")
    elif p1 == 'rock':
        if p2 == 'scissors':
            return("%s wins!" % player1)
        else:
            return("%s wins!" % player2)
    elif p1 == 'scissors':
        if p2 == 'paper':
            return("%s wins!" % player1)
        else:
            return("%s wins!" % player2)
    elif p1 == 'paper':
        if p2 == 'rock':
            return("%s wins!" % player1)
        else:
            return("%s wins!" % player2)
    else:
        return("Input is not valid!please make sure you enter 'rock, paper or scissors', try again.")
        sys.exit()

print(compare(player1_a, player2_a))
