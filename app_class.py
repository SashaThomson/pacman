import pygame
import sys 
from settings import *
from player_class import *

pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = MAZE_WIDTH//28
        self.cell_height = MAZE_HEIGHT//30
        self.player = Player(self, PLAYER_START_POS)
        self.walls = []
        self.coins = []

        self.load()

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(FPS)   
        pygame.quit()
        sys.exit()   


######################## HELPER FUNCTIONS ###################

def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(words, False, colour)
    text_size = text.get_size()
    if centered: 
        pos[0] = pos[0]-text_size[0]//2
        pos[1] = pos[1]-text_size[1]//2
    screen.blitz(text, pos)

def load(self):
    self.background = pygame.image.load('background.png')
    self.background = pygame.transform.scale(scale.background, (MAZE_WIDTH, MAZE_HEIGHT))

#Opening walls file 
#Creating walls list with co-ords of walls 
#Stored as a vector 
    with open("walls.txt", "r") as file:
        for yidx, line in enumerate(file):
            for xidx, char in enumerate(line):
                if char == "1":
                    self.walls.append(vec(xidx, yidx))
                elif char == "c":
                    self.coins.append(vec(xidx, yidx))
    #print(self.walls)
     
def draw_grid(self):
    for x in range(WIDTH//self.cell_width):
        pygame.draw.line(self.background, GREY, (x*self.cell_width, 0), (x*self.cell_width, HEIGHT))
    for x in range(HEIGHT//self.cell_height):
        pygame.draw.line(self.background, GREY, (0, x*self.cell_height), (WIDTH, x*self.cell_height))

    for coin in self.coins:
        pygame.draw.rect(self.background, (167, 179, 34), (coin9.x*self.cell_width, coin.y*self.cell_height, self.cell_width, self.cell_height ))
######################### INTRO functions ####################

    def start_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state == 'playing'


    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        #self.draw_text('PUSH SPACE BAR'self.screen, (WIDTH//2, HEIGHT//2), START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        #self.draw_text('1 PLAYER ONLY'self.screen, (WIDTH//2, HEIGHT//2+50), START_TEXT_SIZE, (44, 167, 1598), START_FONT, centered=True)
        #self.draw_text('HIGH SCORE'self.screen, (5,0), START_TEXT_SIZE, (255,255,255), START_FONT)
        pygame.display.update()
