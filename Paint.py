import pygame
import random
from tkinter import *
from tkinter import colorchooser

pygame.init()

win_x = 800
win_y = 800

win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Paint But Python!')

# Take image as input
img = pygame.image.load('Logo.jpeg')

# Set image as icon
pygame.display.set_icon(img)

class drawing(object):

    def __init__(self):
        '''constructor'''
        self.color = (0, 0, 0)
        self.width = 16
        self.height = 16
        self.rad = 6
        self.tick = 0
        self.time = 0

    def draw(self, win, pos):
        pygame.draw.circle(win, self.color, (pos[0], pos[1]), self.rad)
        if self.color == (255, 255, 255):
            pygame.draw.circle(win, self.color, (pos[0], pos[1]), 20)
        pygame.draw.rect(win, (255, 255, 255), (699, 33, 101, 767))

    def click(self, win, list, list2):
        pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed() == (1, 0, 0) and pos[0] < 700:
            if pos[1] > 25:
                self.draw(win, pos)
        elif pygame.mouse.get_pressed() == (1, 0, 0):
            for button in list:
                if pos[0] > button.x and pos[0] < button.x + button.width:
                    if pos[1] > button.y and pos[1] < button.y + button.height:
                        self.color = button.color2
            for button in list2:
                if pos[0] > button.x and pos[0] < button.x + button.width:
                    if pos[1] > button.y and pos[1] < button.y + button.height:
                        if self.tick == 0:
                            if button.action == 1:
                                win.fill((255, 255, 255))
                                self.tick += 1
                            if button.action == 2 and self.rad > 2:
                                self.rad -= 1
                                self.tick += 1
                                pygame.draw.rect(
                                    win, (255, 255, 255), (710, 388, 80, 35))

                            if button.action == 3 and self.rad < 60:
                                self.rad += 1
                                self.tick += 1
                                pygame.draw.rect(
                                    win, (255, 255, 255), (710, 388, 80, 35))
                            if button.action == 5:
                                color_code = colorchooser.askcolor(title ="Choose color")
                                color_code = color_code[0]
                                self.color = color_code

        for button in list2:
            if button.action == 4:
                button.text = str(self.rad)

class button(object):

    def __init__(self, x, y, width, height, color, color2, outline=0, action=0, text=''):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.outline = outline
        self.color2 = color2
        self.action = action
        self.text = text

    def draw(self, win):

        pygame.draw.rect(win, self.color, (self.x, self.y,
                                        self.width, self.height), self.outline)
        font = pygame.font.SysFont('comicsansms', 30)
        text = font.render(self.text, 1, self.color2)
        win.blit(text, (int(self.x+self.width/2-text.get_width()/2),
                        int(self.y+self.height/2-text.get_height()/2)))


def drawHeader(win):
    # Drawing header space
    pygame.draw.rect(win, (175, 171, 171), (0, 0, 800, 35))
    pygame.draw.rect(win, (175, 171, 171), (699, 33, 101, 35))
    pygame.draw.rect(win, (175, 171, 171), (699, 302, 101, 35))
    pygame.draw.rect(win, (175, 171, 171), (699, 434, 101, 35))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 700, 35), 2)
    pygame.draw.rect(win, (0, 0, 0), (699, 0, 101, 35), 2)
    pygame.draw.rect(win, (0, 0, 0), (699, 33, 101, 767), 2)
    pygame.draw.rect(win, (0, 0, 0), (699, 33, 101, 35), 2)
    pygame.draw.rect(win, (0, 0, 0), (699, 302, 101, 35), 2)
    pygame.draw.rect(win, (0, 0, 0), (699, 434, 101, 35), 2)

    # Printing header
    font = pygame.font.SysFont('comicsansms', 30)

    canvasText = font.render('Canvas', 1, (0, 0, 0))
    win.blit(canvasText, (int(356 - canvasText.get_width() / 2),
                        int(30 / 2 - canvasText.get_height() / 2) + 2))

    toolsText = font.render('Tools', 1, (0, 0, 0))
    win.blit(toolsText, (int(750 - toolsText.get_width() / 2),
                        int(30 / 2 - toolsText.get_height() / 2 + 2)))

    coloursText = font.render('Colour', 1, (0, 0, 0))
    win.blit(coloursText, (int(750 - coloursText.get_width() / 2),
                        int(95 / 2 - coloursText.get_height() / 2 + 2)))

    sizeText = font.render('Size', 1, (0, 0, 0))
    win.blit(sizeText, (int(750 - sizeText.get_width() / 2),
                        int(633 / 2 - sizeText.get_height() / 2 + 2)))

    toolText = font.render('Tools', 1, (0, 0, 0))
    win.blit(toolText, (int(750 - toolText.get_width() / 2),
                        int(896 / 2 - toolText.get_height() / 2 + 2)))

def draw(win):
    player1.click(win, Buttons_color, Buttons_other)

    pygame.draw.rect(win, (0, 0, 0), (0, 0, 700, 800),
                    2) # Drawing canvas space
    drawHeader(win)

    for button in Buttons_color:
        button.draw(win)

    for button in Buttons_other:
        button.draw(win)

    pygame.display.update()


def main_loop():
    run = True
    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False

        draw(win)

        if 0 < player1.tick < 40:
            player1.tick += 1
        else:
            player1.tick = 0

        if 0 < player1.time < 4001:
            player1.time += 1
        elif 4000 < player1.time < 4004:
            gameOver()
            player1.time = 4009
        else:
            player1.time = 0
            player1.play = False

    pygame.quit()

player1 = drawing()
# Fill colored to our paint
win.fill((255, 255, 255))
pos = (0, 0)

# Defining color buttons
redButton = button(753, 40+33, 40, 40, (255, 0, 0), (255, 0, 0))
blueButton = button(707, 40+33, 40, 40, (0, 0, 255), (0, 0, 255))
greenButton = button(707, 86+33, 40, 40, (0, 255, 0), (0, 255, 0))
orangeButton = button(753, 86+33, 40, 40, (255, 192, 0), (255, 192, 0))
yellowButton = button(707, 132+33, 40, 40, (255, 255, 0), (255, 255, 0))
purpleButton = button(753, 132+33, 40, 40, (112, 48, 160), (112, 48, 160))
blackButton = button(707, 178+33, 40, 40, (0, 0, 0), (0, 0, 0))
whiteButton = button(753, 178+33, 40, 40, (0, 0, 0), (255, 255, 255), 1)
moreDisplay = button(707, 224+33, 86, 40, (201, 201, 201), (0, 0, 0), 0, 5, 'More')

smallerButton = button(707, 270+72, 40, 40, (201, 201, 201), (0, 0, 0), 0, 2, '-')
biggerButton = button(753, 270+72, 40, 40, (201, 201, 201), (0, 0, 0), 0, 3, '+')
sizeDisplay = button(707, 316+72, 86, 40, (0, 0, 0), (0, 0, 0), 1, 4, 'Size')

# Defining other buttons
clrButton = button(707, 362+113, 86, 40, (201, 201, 201), (0, 0, 0), 0, 1, 'Clear')

Buttons_color = [blueButton, redButton, greenButton, orangeButton,
                yellowButton, purpleButton, blackButton, whiteButton]
Buttons_other = [clrButton, smallerButton, biggerButton,
                sizeDisplay, moreDisplay]

main_loop()
