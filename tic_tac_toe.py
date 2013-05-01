import sys


class Player:
  
    winningNumbers = ([ set("123"), set("456"), set("789"), set("147"), 
                      set("258"), set("369"), set("159"), set("357") ])

    validMoves = list("123456789")

    def __init__(self,symbol):
        self.symbol = symbol
        self.movesMade = []

    def makeValidMove(self):
        while True:
            move = raw_input(self.symbol + ": ")
            if move in Player.validMoves:
                Player.validMoves.remove(move)
                self.movesMade.append(move)
                return move
            else:
                print "Invalid Move."
                print "Please enter a number from 1 to 9 that is not already occupied."

    def isWinner(self):
        for winner in Player.winningNumbers:
            if winner.issubset(set(self.movesMade)):
                print self.symbol + " wins the game!"
                sys.exit(0)

    def isTie(self):
        # checks if Player.validMoves == [] (there are no more valid moves)
        if not Player.validMoves:
            print ("This game has ended in a tie!")
            sys.exit(0)

# allMoves stores the current state of the tic tac toe board        
allMoves = list("123456789")

# printGame prints the current state of the tic tac toe board
def printGame(moves):
    print moves[0] + " " + moves[1] + " " + moves[2]
    print moves[3] + " " + moves[4] + " " + moves[5]
    print moves[6] + " " + moves[7] + " " + moves[8]
    print


def main(): 

    # Creates "X" Player and "O" Player
    xPlayer = Player("X")
    oPlayer = Player("O")

    print
    print "Tic Tac Toe"
    print "Enter your move as a number from 1 to 9 as shown below:"
    print

    printGame(allMoves)

    while True:

        x = xPlayer.makeValidMove()

        allMoves[int(x)-1] = xPlayer.symbol
        printGame(allMoves)
    
        xPlayer.isWinner()
        xPlayer.isTie()

        o = oPlayer.makeValidMove()
        
        allMoves[int(o)-1] = oPlayer.symbol
        printGame(allMoves)

        oPlayer.isWinner()
        # Don't need to check oPlayer.isTie() because tie can only happen after X's turn

main()

