import random

def createBoard(boardSize, boardType):
    board = [['#' for _ in range(boardSize)] for _ in range(boardSize)]
    if boardType == "player":
        print("Place your ships on the board:")
        for row in board:
            print(' '.join(row))
        for _ in range(numShips):
            while True:
                try:
                    x, y = map(int, input("Enter coordinates for your ship (x y): ").split())
                    if 0 <= x < boardSize and 0 <= y < boardSize and board[x][y] == '#':
                        board[x][y] = '*'
                        break
                    else:
                        print("Invalid input or position already occupied. Try again.")
                except ValueError:
                    print("Invalid input format. Use two numbers separated by a space.")
    return board

def printBoards(playerBoard, enemyBoard, hideEnemyShips=True):
    print("\n   Player Board           Enemy Board")
    header = "   " + " ".join(map(str, range(boardSize)))
    print(header + "    |    " + header)
    print("  " + "-" * (boardSize * 2) + "    |    " + "-" * (boardSize * 2))

    for i in range(boardSize):
        playerRow = f"{i} " + ' '.join(playerBoard[i])
        enemyRow = f"{i} " + ' '.join(' ' if hideEnemyShips and cell == '*' else cell for cell in enemyBoard[i])
        print(f"{playerRow}    |    {enemyRow}")

def placeShips(board, numShips):
    for _ in range(numShips):
        while True:
            x, y = random.randint(0, boardSize - 1), random.randint(0, boardSize - 1)
            if board[x][y] == '#':
                board[x][y] = '*'
                break

def playerTurn(enemyBoard):
    global playerHits
    while True:
        try:
            x, y = map(int, input("Enter target coordinates (x y): ").split())
            if 0 <= x < boardSize and 0 <= y < boardSize and enemyBoard[x][y] not in ['X', 'O']:
                break
            print("Invalid input or already targeted. Try again.")
        except ValueError:
            print("Invalid input format. Use two numbers separated by a space.")

    if enemyBoard[x][y] == '*':
        print("Hit!")
        enemyBoard[x][y] = 'X'
        playerHits += 1
    else:
        print("Miss!")
        enemyBoard[x][y] = 'O'

def enemyTurn(playerBoard):
    global enemyHits, enemyTargets
    x, y = enemyTargets.pop()
    if playerBoard[x][y] == '*':
        print(f"Enemy hits at ({x}, {y})!")
        playerBoard[x][y] = 'X'
        enemyHits += 1
    else:
        print(f"Enemy misses at ({x}, {y})!")
        playerBoard[x][y] = 'O'

def playGame():
    global playerHits, enemyHits
    while playerHits < numShips and enemyHits < numShips:
        print("\nGame Board:")
        printBoards(playerBoard, enemyBoard)

        print("\nYour Turn:")
        playerTurn(enemyBoard)

        if playerHits == numShips:
            print("You win!")
            break

        print("\nEnemy's Turn:")
        enemyTurn(playerBoard)

        if enemyHits == numShips:
            print("You lose!")
            break

boardSize = 6
numShips = 4

playerHits = 0
enemyHits = 0

playerBoard = createBoard(boardSize, "player")
enemyBoard = createBoard(boardSize, "enemy")

placeShips(enemyBoard, numShips)

enemyTargets = [(x, y) for x in range(boardSize) for y in range(boardSize)]
random.shuffle(enemyTargets)

playGame()