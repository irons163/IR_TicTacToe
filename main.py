board = [' ' for x in range(10)]


def setupBoard(board):
    for position, letter in enumerate(board):
        board[position] = ' '


def insetLetter(board, postion, letter):
    board[postion] = letter


def playerMove(board):
    run = True
    while run:
        move = input("Please select a postion for \'X\'?")
        try:
            move = int(move)
            print(move)
            if(move > 0 & move < 10):
                if(isFreeSpace(board, move)):
                    run = False
                    insetLetter(board, move, 'x')
                else:
                    print('The space is not empty.')
            else:
                print('Please insert a proper number.')
        except:
            print('Please input a number.')


def computerMove(board):
    move = calculateComputerMove(board)
    if move != 0:
        insetLetter(board, move, 'o')


def calculateComputerMove(board):
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]
    move = 0

    letters = ['o', 'x']
    for letter in letters:
        boardCopy = board[:]
        for position in possibleMoves:
            insetLetter(boardCopy, position, letter)
            if isWinner(boardCopy, letter):
                move = position
                return move

    cornerPosition = [1, 3, 7, 9]
    cornerPossibleMoves = []
    for position in cornerPosition:
        if position in possibleMoves:
            cornerPossibleMoves.append(position)

    if len(cornerPossibleMoves) > 0:
        move = selectRandom(cornerPossibleMoves)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgePosition = [2, 4, 6, 8]
    edgePossibleMoves = []
    for position in edgePosition:
        if position in possibleMoves:
            edgePossibleMoves.append(position)

    if len(edgePossibleMoves) > 0:
        move = selectRandom(edgePossibleMoves)
        return move

    return move


def selectRandom(list):
    import random
    size = len(list)
    index = random.randrange(size)
    return list[index]


def showBoard(board):
    print('       |       |       ')
    print('   ' + board[1] + '   |   ' +
          board[2] + '   |   ' + board[3] + '   ')
    print('       |       |       ')
    print('-----------------------')
    print('       |       |       ')
    print('   ' + board[4] + '   |   ' +
          board[5] + '   |   ' + board[6] + '   ')
    print('       |       |       ')
    print('-----------------------')
    print('       |       |       ')
    print('   ' + board[7] + '   |   ' +
          board[8] + '   |   ' + board[9] + '   ')
    print('       |       |       ')


def askForInset():
    pass


def isFreeSpace(board, position):
    return board[position] == ' '


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def isWinner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter)
            or (board[4] == letter and board[5] == letter and board[6] == letter)
            or (board[7] == letter and board[8] == letter and board[9] == letter)
            or (board[1] == letter and board[4] == letter and board[7] == letter)
            or (board[2] == letter and board[5] == letter and board[8] == letter)
            or (board[3] == letter and board[6] == letter and board[9] == letter)
            or (board[1] == letter and board[5] == letter and board[9] == letter)
            or (board[3] == letter and board[5] == letter and board[7] == letter))


def main():
    setupBoard(board)
    showBoard(board)
    print('///////////////////////')
    print('///////////////////////')
    while not(isBoardFull(board)):
        if not (isWinner(board, 'x')):
            playerMove(board)
            showBoard(board)
            print('///////////////////////')
            print('///////////////////////')
        else:
            break

        if isWinner(board, 'x'):
            break

        if not (isWinner(board, 'o')):
            computerMove(board)
            showBoard(board)
            print('///////////////////////')
            print('///////////////////////')
        else:
            break

        if isWinner(board, 'o'):
            break

    if isWinner(board, 'x'):
        print('x win Game.')
    elif isWinner(board, 'o'):
        print('o win Game.')
    else:
        print('Tie Game.')


while True:
    main()
    play = input('Do you want to play again?(Y/N)')
    if play == 'Y' or play == 'y':
        pass
    else:
        break


print('End')
