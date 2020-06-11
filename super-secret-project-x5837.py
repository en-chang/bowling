import time
from tabulate import tabulate

# Delay to make display slower
def delay():
    time.sleep(0.475)

class Player:
    def __init__(self, name, record = []):
        self.name = name
        self.record = record

def getPlyrNames():
    print('Please enter what you would like to be called.')
    plyrs = []
    plyrNum = 1
    allPlyrs = False
    while allPlyrs is False:
        if plyrNum == 1:
            plyrName = input(f'Player {plyrNum}: ')
            plyrs.append(plyrName)
            plyrNum += 1
        # After first player entered ask if user/users is/are done
        else:
            plyrName = input(f'If all players are entered type "Done".\nPlayer {plyrNum}: ')
            plyrs.append(plyrName)
            plyrNum += 1
            if 'done' == plyrName.lower():
                del plyrs[-1]
                allPlyrs = True
    return plyrs

def getPinsHit(plyr):
    print()
    print(f'{plyr}:')
    firstHit = getFirstHit()
    if firstHit == 10:
        delay()
        print('STRIKE!')
        # Strike is 100 to differentiate from spares
        return ('_', 'X')
    elif firstHit == 0:
        delay()
        print('HA! YOU SUCK!')
    delay()
    print()
    print(f'{plyr}:')
    secndHit = getSecndHit(firstHit)
    totalPinsHit = firstHit + secndHit
    if totalPinsHit == 10:
        delay()
        print('Spare!')
        return (firstHit, '/')
    elif totalPinsHit == 0:
        delay()
        print('HAHAHA!!!!!!')
        delay()
        print('HAHAHAHAHAHAHAAHAHAHAHAHAHAHAAHAHAHA!!')
        delay()
        print('AHAHAHAHAHAAHAHAHA!!!!')
        delay()
        print('YOUUUU')
        delay()
        print('SUCKKKK!!!')
        delay()
        print()
        print('GUTTER BAAAAAAALLLLLLLL!!!!!!!!!!')
        return 0
    elif secndHit == 0:
        delay()
        print('HA! YOU SUCK!')
    delay()
    return (firstHit, secndHit)

# Helper function for getPinsHit()
def getFirstHit():
    typo = True
    dumbInput = False
    while typo:
        try:
            if dumbInput:
                delay()
                firstHit = int(input('Please enter something not retarded (0 - 10): '))
                if firstHit < 0 or firstHit > 10:
                    raise ValueError
            else:
                firstHit = int(input('How many pins did you successfully hit? '))
                if firstHit < 0 or firstHit > 10:
                    raise ValueError
            typo = False
        except ValueError:
            delay()
            print('aRe YoU StUpiD????')
            dumbInput = True
    return firstHit

# Helper function for getPinsHit()
def getSecndHit(firstHit):
    typo = True
    dumbInput = False
    while typo:
        try:
            if dumbInput:
                delay()
                secndHit = int(input('Please enter the correct number... retard: '))
                if secndHit < 0 or secndHit > 10:
                    raise ValueError
                if (firstHit + secndHit) > 10:
                    raise ValueError
            else:
                delay()
                secndHit = int(input('How many pins did you successfully hit this time? '))
                if secndHit < 0 or secndHit > 10:
                    raise ValueError
                if (firstHit + secndHit) > 10:
                    raise ValueError
            typo = False
        except ValueError:
            delay()
            print('aRe YoU StUpiD????')
            dumbInput = True
    return secndHit

def displyRec(plyr, recrd):
    scores = calcRec(recrd)
    table = [plyr]
    for pins, score in zip(recrd, scores):
        if len(table) == 10:
            table.append(f'{pins[0]} [{pins[1]}][_]\n      {score}')
        else:
            table.append(f'{pins[0]} [{pins[1]}]\n   {score}')
    spaces = 9 - len(recrd)
    for space in range(spaces):
        table.append('_ [_]\n   __')
    if spaces >= 0:
        table.append('_ [_][_]\n      __')
    table.append(f'{scores[-1]}')
    print(tabulate([table], headers=["Name", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Total'], tablefmt="fancy_grid"))

# Helper function for displyRec()
def calcRec(recrd):
    scores = []
    for frame, pins in enumerate(recrd):
        break
    return scores

def game():
    data = []
    frame = 1
    names = getPlyrNames()
    # Create data structure for Players
    for name in names:
        data.append(Player(name))
    '''
        # Print everyones blank record
    '''
    # Start game
    # End until last frame complete
    while frame <= 10:
        print()
        print(f'Frame: {frame}')
        # Ask every player for how many pins they hit
        for i in range(len(data)):
            plyr = data[i].name
            pinsHit = getPinsHit(plyr)
            data[i].record.append(pinsHit)
            recrd = data[i].record
            delay()
            print()
            displyRec(plyr, recrd)
        frame += 1

def main():
    print()
    print('Welcome to super-secret-project-x5837')
    print()
    delay()
    game()

if __name__ == "__main__":
    main()