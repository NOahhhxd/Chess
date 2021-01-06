import pygame
import random

pygame.init()
screen = pygame.display.set_mode((740, 740))
pygame.display.set_caption("test")

running = True

size = 80

feld = [["T", "S", "L", "D", "K", "L", "S", "T"], ("B " * 8).split(" ")[0:-1], ("  "*8).split(" ")[0:7], ("  "*8).split(" ")[0:7], ("  "*8).split(" ")[0:7], ("  "*8).split(" ")[0:7], ("B " * 8).split(" ")[0:-1], ["T", "S", "L", "D", "K", "L", "S", "T"]]
for f in feld:
    print(f)

WHITE = (255, 255, 255)
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
        pass


class Bishop(Figuren):
    def showPossibilities(self):
        for x in range(0, 8):
            for y in range(0, 8):
                pygame.draw.rect(screen, DGREEN, (x + self.px, y + self.px, 80, 80))


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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x = (x - 50) // 80
            y = (y - 50) // 80
            if (event.button == 3):
                print(f"x={x}, y={y}")
            if 0 <= x < 8 and 0 <= y < 8:
                selected[0] = x
                selected[1] = y

    screen.fill(GRAY)
    spielfeld()
    if selected[0] != -1:
        pygame.draw.rect(screen, GREEN, (selected[0] * size + 50, selected[1] * size + 50, size, size))
        for x in range(-7, 8):
            for y in range(-7, 8):
                if (x == y or x == -y) and -1 < (x + selected[0]) < 8 and -1 < (y + selected[1]) < 8:
                    pygame.draw.rect(screen, DGREEN,
                                     ((x + selected[0]) * size + 50, (y + selected[1]) * size + 50, size, size))
    pygame.display.update()

pygame.quit()
