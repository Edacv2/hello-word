from random import randint
from sense_hat import SenseHat
from time import sleep
import pygame
from pygame.locals import *


class snake():
# Uncomment to use keyboard arrows   
#     up = 0
#     down = 1
#     right = 2
#     left = 3

    bg_color = [0, 0, 0]
    snake_color = [0, 255, 0]
    apple_color = [255, 0, 0]
    
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640, 480))
        
        self.sense = SenseHat()       
        
    def startGame(self):
        self.sense.clear(self.bg_color)
        #self.sense.set_rotation(270) # rotation of the sense hat
        self.sense.low_light = True
        self.direction = self.up 
        self.length = 3
        self.tail = []
        self.tail.insert(0, [4, 4])
        self.createApple()
        self.score = 0

        playing = True
        while playing:
            sleep(0.5)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self._handle_event(event)
            playing = self.move()
            
    def _handle_event(self, event):
        if event.key == pygame.K_DOWN: 
            self.down()
        elif event.key == pygame.K_UP:
            self.up()
        elif event.key == pygame.K_LEFT:
            self.left()
        elif event.key == pygame.K_RIGHT:
            self.right()
            
    def createApple(self):
        badApple = True
        while badApple:
            x = randint(0, 7)
            y = randint(0, 7)
            badApple = self.checkCollision(x, y)
        self.apple = [x, y]
        self.sense.set_pixel(x, y, self.apple_color)

    def checkCollision(self, x, y):
        if x > 7 or x < 0 or y > 7 or y < 0:
            return True
        else:
            for segment in self.tail:
                if segment[0] == x and segment[1] == y:
                    return True
            else:
               return False
            
    def addSegment(self, x, y):
        self.sense.set_pixel(x, y, self.snake_color)
        self.tail.insert(0, [x, y])

        if len(self.tail) > self.length:
            lastSegment = self.tail[-1]
            self.sense.set_pixel(lastSegment[0], lastSegment[1], self.bg_color)
            self.tail.pop()
            
    def move(self):
        newSegment = [self.tail[0][0], self.tail[0][1]]
        if self.direction == self.up:
            newSegment[1] -= 1
        elif self.direction == self.down:
            newSegment[1] += 1
        elif self.direction == self.left:
            newSegment[0] -= 1
        elif self.direction == self.right:
            newSegment[0] += 1

        if self.checkCollision(newSegment[0], newSegment[1]):
            snakehead = self.tail[0]
            for flashHead in range (0, 5):
                self.sense.set_pixel(snakehead[0], snakehead[1], self.snake_color)
                sleep(0.2)
                self.sense.set_pixel(snakehead[0], snakehead[1], self.bg_color)
                sleep(0.2)
            self.sense.show_message("GAME OVER")
            self.sense.show_message("Score = " + str(self.score))
        else:
            self.addSegment(newSegment[0], newSegment[1])

            if newSegment[0] == self.apple[0] and newSegment[1] == self.apple[1]:
                self.length += 1
                self.score += 10
                self.createApple()

            return True
        
    def up(self):
        if self.direction != self.down:
            self.direction = self.up

    def down(self):
        if self.direction != self.up:
            self.direction = self.down

    def left(self):
        if self.direction != self.right:
            self.direction = self.left

    def right(self):
        if self.direction != self.left:
            self.direction = self.right
      
if __name__ == "__main__":
    snake = snake()
    print("Press Escape to Quit")
    print("Press Joystick to start")

    running = True

    while running:
        for event in pygame.event.get():
            print(event) #validation
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    snake.startGame()                   
