import time
from tabulate import tabulate

# Delay to make display slower
def delay():
    time.sleep(0.475)

class Player:
    def __init__(self, name, record = []):
        self.name = name
        self.record = record
    
    def printNmeAndRec(self):
        print(self.name, self.record)

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

def getPinsHit(plyr, onlyOne = False):
    print()
    print(f'{plyr}:')
    firstHit = getFirstHit()
    if firstHit == 10:
        delay()
        print('STRIKE!')
        return ('_', 'X')
    elif firstHit == 0:
        delay()
        print('HA! YOU SUCK!')
    elif onlyOne is True:
        return (firstHit, 0)
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
        return (0, 0)
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

def createPlyrTble(plyr, recrd):
    scores = calcRec(recrd)
    scores = scores[:10]
    table = [plyr]
    frame = 1
    for pins, score in zip(recrd, scores):
        if frame == 10:
            if pins[1] == 'X':
                table.append(f'{pins[1]} [_][_]\n      {score}')
                frame += 1
            else:
                table.append(f'{pins[0]} [{pins[1]}][_]\n      {score}')
                frame += 1
        else:
            table.append(f'{pins[0]} [{pins[1]}]\n   {score}')
            frame += 1
    # Adjust last frame
    if len(recrd) > 9:
        if recrd[9][1] == 'X':
            if len(recrd) > 10:
                if recrd[10][1] == 'X':
                    if len(recrd) > 11:
                        # Last frame Turkey
                        if recrd[11][1] == 'X':
                            table[10] = f'{recrd[9][1]} [{recrd[10][1]}][{recrd[11][1]}]\n      {scores[-1]}'
                        # Last frame Double
                        else:
                            table[10] = f'{recrd[9][1]} [{recrd[10][1]}][{recrd[11][0]}]\n      {scores[-1]}'
                # Last frame only strike
                else:
                    table[10] = f'{recrd[9][1]} [{recrd[10][0]}][{recrd[10][1]}]\n      {scores[-1]}'
        # Last frame spare
        elif recrd[9][1] == '/':
            if recrd[10][1] == 'X':
                table[10] = f'{recrd[9][0]} [{recrd[9][1]}][{recrd[10][1]}]\n      {scores[-1]}'
            else:
                table[10] = f'{recrd[9][0]} [{recrd[9][1]}][{recrd[10][0]}]\n      {scores[-1]}'
    spaces = 9 - len(recrd)
    for space in range(spaces):
        table.append('_ [_]\n   __')
    if spaces >= 0:
        table.append('_ [_][_]\n      __')
    if len(scores) == 0:
        table.append(f'__')
    else:
        table.append(f'{scores[-1]}')
    return table

# Helper function for createPlyrTble()
def calcRec(recrd):
    scores = []
    for frame, pins in enumerate(recrd):
        # Calculate strike scores
        if pins[1] == 'X':
            # Turkey branch
            if len(recrd) > (frame + 2):
                # First frame strike
                if frame == 0:
                    # Calculate Turkey
                    if recrd[frame + 2][1] == 'X' and recrd[frame + 1][1] == 'X':
                        if len(recrd) > (frame + 2):
                            score = 30
                            scores.append(score)
                        else:
                            scores.append('__')
                    # Calculate doubles
                    elif recrd[frame + 1][1] == 'X':
                        if len(recrd) > (frame + 2):
                            score = 20 + recrd[frame + 2][0]
                            scores.append(score)
                        else:
                            scores.append('__')
                    elif recrd[frame + 1][1] == '/':
                        score = 10 + recrd[frame + 1][0] + (10 - recrd[frame + 1][0])
                        scores.append(score)
                    else:
                        score = 10 + recrd[frame + 1][0] + recrd[frame + 1][1]
                        scores.append(score)
                # Calculate Turkeys
                elif recrd[frame + 2][1] == 'X' and recrd[frame + 1][1] == 'X':
                    if len(recrd) > (frame + 2):
                        score = scores[-1] + 30
                        scores.append(score)
                    else:
                        scores.append('__')
                # Calculate doubles
                elif recrd[frame + 1][1] == 'X':
                    if len(recrd) > (frame + 2):
                        score = scores[-1] + 20 + recrd[frame + 2][0]
                        scores.append(score)
                    else:
                        scores.append('__')
                # Calculate normal strikes
                else:
                    # When calculating stirkes with a spare
                    if recrd[frame + 1][1] == '/':
                        score = scores[-1] + 20
                        scores.append(score)
                    else:
                        score = scores[-1] + 10 + recrd[frame + 1][0] + recrd[frame + 1][1]
                        scores.append(score)
            # Double branch
            elif len(recrd) > (frame + 1):
                # First frame strike
                if frame == 0:
                    # Calculate doubles
                    if recrd[frame + 1][1] == 'X':
                        if len(recrd) > (frame + 2):
                            score = 20 + recrd[frame + 2][0]
                            scores.append(score)
                        else:
                            scores.append('__')
                    elif recrd[frame + 1][1] == '/':
                        score = 10 + recrd[frame + 1][0] + (10 - recrd[frame + 1][0])
                        scores.append(score)
                    else:
                        score = 10 + recrd[frame + 1][0] + recrd[frame + 1][1]
                        scores.append(score)
                # Calculate doubles
                elif recrd[frame + 1][1] == 'X':
                    if len(recrd) > (frame + 2):
                        score = scores[-1] + 20 + recrd[frame + 2][0]
                        scores.append(score)
                    else:
                        scores.append('__')
                # Calculate normal strikes
                else:
                    # When calculating stirkes with a spare
                    if recrd[frame + 1][1] == '/':
                        score = scores[-1] + 20
                        scores.append(score)
                    else:
                        score = scores[-1] + 10 + recrd[frame + 1][0] + recrd[frame + 1][1]
                        scores.append(score)
            else:
                scores.append('__')
        # Calculate spare scores
        elif pins[1] == '/':
            if len(recrd) > (frame + 1):
                if frame == 0:
                    if recrd[frame + 1][1] == 'X':
                        score = 20
                        scores.append(score)
                    else:
                        score = 10 + recrd[frame + 1][0]
                        scores.append(score)
                else:
                    if recrd[frame + 1][1] == 'X':
                        score = scores[-1] + 20
                        scores.append(score)
                    else:
                        score = scores[-1] + 10 + recrd[frame + 1][0]
                        scores.append(score)
            else:
                scores.append('__')
        # Calculate normal scores
        else:
            if frame == 0:
                score = pins[0] + pins[1]
                scores.append(score)
            else:
                score = scores[-1] + pins[0] + pins[1]
                scores.append(score)
    return scores

def game():
    data = []
    frame = 1
    names = getPlyrNames()
    records = [[] for x in range(len(names))]
    # Create data structure for Players
    for name in names:
        data.append(Player(name))
    table = []
    for j in range(len(data)):
        plyr = data[j].name
        recrd = data[j].record
        table.append(createPlyrTble(plyr, recrd))
    delay()
    print()
    print(tabulate(table, headers=["Name", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Total'], tablefmt="fancy_grid"))
    # Start game
    # End until last frame complete
    while frame <= 10:
        print()
        print(f'Frame: {frame}')
        # Ask every player for how many pins they hit
        for i in range(len(data)):
            plyr = data[i].name
            pinsHit = getPinsHit(plyr)
            records[i].append(pinsHit)
            data[i].record = records[i]
            recrd = data[i].record
            if len(recrd) == 10:
                if recrd[9][1] == 'X':
                    pinsHit = getPinsHit(plyr)
                    data[i].record.append(pinsHit)
                    recrd = data[i].record
                    if recrd[10][1] == 'X':
                        pinsHit = getPinsHit(plyr, True)
                        data[i].record.append(pinsHit)
                        recrd = data[i].record
                elif recrd[9][1] == '/':
                    pinsHit = getPinsHit(plyr, True)
                    data[i].record.append(pinsHit)
                    recrd = data[i].record
            table = []
            for j in range(len(data)):
                plyr = data[j].name
                recrd = data[j].record
                table.append(createPlyrTble(plyr, recrd))
            delay()
            print()
            print(tabulate(table, headers=["Name", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Total'], tablefmt="fancy_grid"))
        frame += 1

def main():
    print()
    print("                               W E L C O M E    T O")
    delay()
    delay()
    print("           R E B E K A H ' S    B I R T H D A Y    E X T R A V A G A N Z A")
    delay()
    delay()
    print("                           B O W L I N G    P A R T Y !!!")
    print()
    delay()
    game()

if __name__ == "__main__":
    main()