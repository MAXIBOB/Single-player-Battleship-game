from random import randint

board = []
print "Let's play Battleship!"
level=raw_input("Choose the difficulty:1, 2, 3, or unlimited shots(type 4):")
def print_board(board):
    for row in board:
        print " ".join(row)
if level.isalpha():
    print "That is not a valid input"
elif int(level)==2:
    board.append([" ","","1","2","3","4","5"])
    board.append([" ","-----------"])
    for x in range(5):
        board.append([str(x+1)+"|","O","O","O","O","O"])

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)
    for turn in range(4):
        print "Turn", turn+1
        print_board(board)
        guess_row = raw_input("Guess Row:")
        guess_col = raw_input("Guess Col:")

        if guess_row.isalpha() or guess_col.isalpha():
            print "That's not a location, you lose 1 turn."
        elif int(guess_row)-1 == ship_row and int(guess_col)-1 == ship_col:
            print "Congratulations! You sunk my battleship in "+str(turn+1)+" turns!"
            break
        else:
            if (int(guess_row)-1 < 0 or int(guess_row)-1 > 4) or (int(guess_col)-1 < 0 or int(guess_col)-1 > 4):
                print "Oops, that's not even in the ocean."
            elif(board[int(guess_row)-1][int(guess_col)-1] == "X"):
                print "You guessed that one already."
                turn+=1
            else:
                print "You missed my battleship!"
                board[int(guess_row)-1][int(guess_col)-1] = "X"
            if turn==3:
                board[ship_row][ship_col]="S"
                print "Game Over"
                print_board(board)
                break
elif int(level)==1:
    board.append([" ","","1","2","3"])
    board.append([" ","------"])
    for x in range(3):
        board.append([str(x+1)+"|","O","O","O"])
    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)
    for turn in range(5):
        print "Turn", turn+1
        print_board(board)
        guess_row = raw_input("Guess Row:")
        guess_col = raw_input("Guess Col:")

        if guess_row.isalpha() or guess_col.isalpha():
            print "That's not a location, you lose 1 turn."
        elif int(guess_row)-1 == ship_row and int(guess_col)-1 == ship_col:
            print "Congratulations! You sunk my battleship in "+str(turn+1)+" turns!"
            break
        else:
            if (int(guess_row)-1 < 0 or int(guess_row)-1 > 3) or (int(guess_col)-1 < 0 or int(guess_col)-1 > 3):
                print "Oops, that's not even in the ocean."
            elif(board[int(guess_row)-1][int(guess_col)-1] == "X"):
                print "You guessed that one already."
                turn+=1
            else:
                print "You missed my battleship!"
                board[int(guess_row)-1][int(guess_col)-1] = "X"
            if turn==4:
                board[ship_row][ship_col]="S"
                print "Game Over"
                print_board(board)
                break
elif int(level)==3:
    board.append([" ","","1","2","3","4","5","6","7"])
    board.append([" ","--------------"])
    for x in range(7):
        board.append([str(x+1)+"|","O","O","O","O","O","O","O"])

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)
    for turn in range(5):
        print "Turn", turn+1
        print_board(board)
        guess_row = raw_input("Guess Row:")
        guess_col = raw_input("Guess Col:")

        if guess_row.isalpha() or guess_col.isalpha():
            print "That's not a location, you lose 1 turn."
        elif int(guess_row)-1 == ship_row and int(guess_col)-1 == ship_col:
            print "Congratulations! You sunk my battleship in "+str(turn+1)+" turns!"
            break
        else:
            if (int(guess_row)-1 < 0 or int(guess_row)-1 > 7) or (int(guess_col)-1 < 0 or int(guess_col)-1 > 7):
                print "Oops, that's not even in the ocean."
            elif(board[int(guess_row)-1][int(guess_col)-1] == "X"):
                print "You guessed that one already."
                turn+=1
            else:
                print "You missed my battleship!"
                board[int(guess_row)-1][int(guess_col)-1] = "X"
elif int(level)==4:
    board.append([" ","","1","2","3","4","5","6","7"])
    board.append([" ","--------------"])
    for x in range(7):
        board.append([str(x+1)+"|","O","O","O","O","O","O","O"])
    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)
    for turn in range(50):
        print "Turn", turn+1
        print_board(board)
        guess_row = raw_input("Guess Row:")
        guess_col = raw_input("Guess Col:")

        if guess_row.isalpha() or guess_col.isalpha():
            print "That's not a location!"
        elif int(guess_row)-1 == ship_row and int(guess_col)-1 == ship_col:
            print "Congratulations! You sunk my battleship in "+str(turn+1)+" turns!"
            break
        else:
            if (int(guess_row)-1 < 0 or int(guess_row)-1 > 7) or (int(guess_col)-1 < 0 or int(guess_col)-1 > 7):
                print "Oops, that's not even in the ocean."
            elif(board[int(guess_row)-1][int(guess_col)-1] == "X"):
                print "You guessed that one already."
                turn+=1
            else:
                print "You missed my battleship!"
                board[int(guess_row)-1][int(guess_col)-1] = "X"
else:
    print "That is not a valid input."
