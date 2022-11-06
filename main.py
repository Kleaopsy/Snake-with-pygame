import pygame
import random

pygame.init()
squSize = 50
mapLength = 11
screenSize = mapLength * squSize
screen = pygame.display.set_mode((screenSize, screenSize))

colorThemes = [
    (142, 195, 176),
    (158, 213, 197),
    (165, 42, 42),
    (0, 255, 255),
    (186, 32, 32)
]
pygame.display.set_caption('Snake')


def createMap():
    screen.fill(colorThemes[0])

    # gameMap
    countSingle = 0
    for i in range(mapLength):
        for j in range(mapLength):
            countSingle += 1
            if countSingle % 2 == 0:
                pygame.draw.rect(screen, colorThemes[1], pygame.Rect(
                    i*squSize, j * 50, squSize, squSize))


createMap()
pygame.display.flip()

running = True
movementWay = [-1]
oldMovementWay = -1
isAppleCreated = False
snakeEatingSelf = False
_snakeX = [(screenSize-squSize)/2 + 5]
_snakeY = [(screenSize-squSize)/2 + 5]
_appleX = -50
_appleY = -50
time = pygame.time.Clock()


# game loop
while running:
    createMap()
    time.tick(4)

    # leaving Area X
    if _snakeX[0] < 0 or _snakeX[0] > mapLength * squSize:
        running = False
    # leaving Area Y
    elif _snakeY[0] < 0 or _snakeY[0] > mapLength * squSize:
        running = False
    # snake eating self
    elif snakeEatingSelf:
        running = False
    # snake eating apple
    elif _snakeX[0] == _appleX and _snakeY[0] == _appleY:
        isAppleCreated = False
        movementWay.insert(0, oldMovementWay)
        if oldMovementWay == 0:
            _snakeX.append(_snakeX[len(_snakeX) - 1] + 50)
            _snakeY.append(_snakeY[len(_snakeY) - 1])
        elif oldMovementWay == 1:
            _snakeX.append(_snakeX[len(_snakeX) - 1])
            _snakeY.append(_snakeY[len(_snakeY) - 1] + 50)
        elif oldMovementWay == 2:
            _snakeX.append(_snakeX[len(_snakeX) - 1] - 50)
            _snakeY.append(_snakeY[len(_snakeY) - 1])
        elif oldMovementWay == 3:
            _snakeX.append(_snakeX[len(_snakeX) - 1])
            _snakeY.append(_snakeY[len(_snakeY) - 1] - 50)
    # take controls
    for event in pygame.event.get():

        # game Close
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and oldMovementWay != 2:
                movementWay[0] = 0
            elif event.key == pygame.K_w and oldMovementWay != 3:
                movementWay[0] = 1
            elif event.key == pygame.K_d and oldMovementWay != 0:
                movementWay[0] = 2
            elif event.key == pygame.K_s and oldMovementWay != 1:
                movementWay[0] = 3

    # apple
    if not isAppleCreated and movementWay != -1:
        _x = -50
        _y = -50
        while True:
            _x = random.randint(0, 10) * 50 + 5
            _y = random.randint(0, 10) * 50 + 5
            _selectPosition = True
            for i in range(len(_snakeX)):
                for j in range(len(_snakeY)):
                    if _snakeX[i] == _x and _snakeY[j] == _y:
                        _selectPosition = False

            if _selectPosition:
                break
        _appleX = _x
        _appleY = _y
        isAppleCreated = True
    pygame.draw.rect(screen, colorThemes[4], pygame.Rect(
        _appleX, _appleY, squSize - 10, squSize - 10))

    # movement
    for i in range(len(_snakeX)):
        index = len(_snakeX) - (i + 1)
        if index == 0:
            continue
        _snakeX[index] = _snakeX[index - 1]
        _snakeY[index] = _snakeY[index - 1]

    if movementWay[0] == 0:
        _snakeX[0] -= 50
        oldMovementWay = 0
    elif movementWay[0] == 1:
        _snakeY[0] -= 50
        oldMovementWay = 1
    elif movementWay[0] == 2:
        _snakeX[0] += 50
        oldMovementWay = 2
    elif movementWay[0] == 3:
        _snakeY[0] += 50
        oldMovementWay = 3

    for i in range(len(_snakeX)):
        pygame.draw.rect(screen, colorThemes[3], pygame.Rect(
            _snakeX[i], _snakeY[i], squSize-10, squSize-10))

    # snakeEatSelf
    counter = 0
    for i in range(len(_snakeX)):
        if _snakeX[0] == _snakeX[i] and _snakeY[0] == _snakeY[i] and not i == 0:
            snakeEatingSelf = True

    if not running == False:
        pygame.display.update()
