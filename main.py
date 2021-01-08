import time

import pygame

pygame.init()
screen = pygame.display.set_mode((740, 740))
pygame.display.set_caption("test")

running = True

size = 80

feld = [["T", "S", "", "D", "K", "L", "S", "T"],
        ["B", "B", "B", "", "B", "B", "B", "B"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "B", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["B", "B", "B", "B", "B", "B", "", "B"],
        ["T", "S", "L", "D", "K", "", "S", "T"]]

WHITE = (255, 255, 255)
PINK = (100, 100, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DGREEN = (0, 255, 100)
font = pygame.font.SysFont(None, 30)
text = font.render("a            b            c            d            e            f            g            h", True,
                   RED)


def spielfeld():
    screen.blit(text, (80, 25))
    for i in range(0, 8):
        screen.blit(font.render((i + 1).__str__(), True, RED), (25, 640 - 80 * i))
    colour = [BLACK, WHITE]
    pos = 0
    for x in range(0, 8):
        pos += 1
        for y in range(0, 8):
            pygame.draw.rect(screen, colour[pos % 2], (x * size + 50, y * size + 50, size, size))
            pos += 1


class Figuren:
    pcolour = 0
    py = 0
    px = 0

    def __init__(self, x, y, colour):
        px = x
        py = y
        pcolour = colour

    def showPossibilities(self):
        pass


class Rook(Figuren):
    def showPossibilities(self):
        for x in range(0, 8):
            if not TurmFigurdazwischen(x, "y"):
                pygame.draw.rect(screen, DGREEN,
                                 (x * size + 50 + 10, self.py * size + 50 + 10, size - 20, size - 20))
            if not TurmFigurdazwischen(x, "x"):
                pygame.draw.rect(screen, DGREEN,
                                 (self.px * size + 50 + 10, x * size + 50 + 10, size - 20, size - 20))
        """
        for x in range(0, 8):
            if not TurmFigurdazwischen(x, "y"):
                pygame.draw.rect(screen, DGREEN, (x * size + 50 + 10, selected[1] * size + 50 + 10, size - 20, size -20))
            if not TurmFigurdazwischen(x, "x"):
                pygame.draw.rect(screen, DGREEN, (selected[0] * size + 50 + 10, x * size + 50 + 10, size - 20, size -20))
        """


class Bishop(Figuren):
    def showPossibilities(self):
        for x in range(-7, 8):
            for y in range(-7, 8):
                if (x == y or x == -y) and -1 < (x + self.px) < 8 and -1 < (y + self.py) < 8:
                    if feld[y + self.py][x + self.px] == "":
                        pygame.draw.rect(screen, DGREEN,
                                         ((x + self.px) * size + 50, (y + self.px) * size + 50, size, size))


class Queen(Figuren):
    def showPossibilities(self):
        pass


class King(Figuren):
    def showPossibilities(self):
        pass


class Knight(Figuren):
    def showPossibilities(self):
        pass


class Pawn(Figuren):
    def showPossibilities(self):
        pass


selected = [-1, -1]
pos2 = [-1, -1]


def dazwischennix(x, richtung):
    boo: bool = True

    if richtung:
        for i2 in range(0, x, 1 if x > 0 else -1):
            if -1 < selected[0] + i2 < 8 and -1 < selected[1] + i2 < 8:
                if feld[selected[1] + i2][selected[0] + i2]:
                    boo = False
    else:
        for i2 in range(0, x, 1 if x > 0 else -1):
            if -1 < selected[0] - i2 < 8 and -1 < selected[1] + i2 < 8:
                if feld[selected[1] + i2][selected[0] - i2]:
                    boo = False

    return boo


def TurmFigurdazwischen(lauf, achse):
    boo: bool = False
    if achse == "y":
        for i in range(selected[0], lauf, 1 if selected[0] < lauf else -1):
            if feld[selected[1]][i] != "" and i != selected[0]:
                boo = True
    if achse == "x":
        for j in range(selected[1], lauf, 1 if selected[1] < lauf else -1):
            if feld[j][selected[0]] != "" and j != selected[1]:
                boo = True
    return boo


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x = (x - 50) // 80
            y = (y - 50) // 80
            if 0 <= x < 8 and 0 <= y < 8:
                if (event.button == 3):
                    if pos2[0] == x and pos2[1] == y:
                        pos2[0] = -1
                        pos2[1] = -1
                    elif pos2[0] != x or pos2[1] != y:
                        pos2[0] = x
                        pos2[1] = y
                    print(f"Feld2 x={x}, y={y} ist {feld[y][x].isalpha()}")
                else:
                    selected[0] = x
                    selected[1] = y
                    print(f"Feld1 x={x}, y={y} ist {feld[y][x].isalpha()}")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                for i in range(pos2[0], selected[0], 1 if pos2[0] < selected[0] else -1):
                    if feld[pos2[1]][i] != "":
                        print("Treffer1")
                for j in range(pos2[1], selected[1], 1 if pos2[1] < selected[1] else -1):
                    if feld[j][pos2[0]] != "":
                        print("Treffer2")

            if event.key == pygame.K_SPACE:

                for i in range(pos2[0], selected[0], 1 if pos2[0] < selected[0] else -1):
                    for j in range(pos2[1], selected[1], 1 if pos2[1] < selected[1] else -1):
                        if i - pos2[0] == j - pos2[1] or i - pos2[0] == -(j - pos2[1]):
                            if feld[j][i] != "":
                                pygame.draw.rect(screen, (100, 0, 123),
                                                 (i * size + 50, j * size + 50, size,
                                                  size))
                                pygame.display.update()
                                pygame.time.delay(100)

    screen.fill(GRAY)
    spielfeld()

    if selected[0] != -1:
        for i in range(-7, 8):
            if -1 < (i + selected[0]) < 8 and -1 < (i + selected[1]) < 8:
                if dazwischennix(i, True):
                    pygame.draw.rect(screen, DGREEN, ((i+ selected[0])*size + 50, (i+selected[1])*size + 50, size, size))
            if -1 < (selected[0]-i) < 8 and -1 < (i + selected[1]) < 8:
                if dazwischennix(i, False):
                    pygame.draw.rect(screen, DGREEN, ((selected[0]-i)*size + 50, (selected[1]+i)*size + 50, size, size))
        '''
        for x in range(-7, 8):
            for y in range(-7, 8):
                if (x == y or x == -y) and -1 < (x + selected[0]) < 8 and -1 < (y + selected[1]) < 8:
                        #if not dazwischennix(x, y):
                            pygame.draw.rect(screen, DGREEN,
                                         ((x + selected[0]) * size + 50, (y + selected[1]) * size + 50, size, size))
        '''
    if selected[0] != -1:
        pygame.draw.rect(screen, GREEN, (selected[0] * size + 50, selected[1] * size + 50, size, size))
    if pos2[0] != -1:
        pygame.draw.rect(screen, PINK, (pos2[0] * size + 50, pos2[1] * size + 50, size, size))

    for i in range(0, 8):
        for j in range(0, 8):
            if feld[j][i] != "":
                pygame.draw.rect(screen, (0, 123, 123), (i * size + 50 + 20, j * size + 50 + 20, size - 40, size - 40))

    pygame.display.update()

pygame.quit()
