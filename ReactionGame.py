'''
Filename: ReactionGame.py
Author: Jose Sanchez-Garcia
Created: March 2015
Summary: This program was created to test the reaction time and cognitive abilities of the user in recognizing the number of whole
		images found at a at a single time. All the images that will be shown have been preloaded are will be used by the program. 
		This program will also be creating the images when it sees that they are not avaiable to it. If they are avaiable to grab, 
		then it will choose them.
'''

import pygame		#this will be used when creating the Graphical User Interface as well as manipulating the images that are present
import time as t
from pygame import *
import random
import sys

pygame.init()
mixer.init()
clock = pygame.time.Clock()

length = 640	#this be used to initiate the size of the window
height = 480
FPS = 50
''' 
These are some of the colors that will be used when creating GUI for the user. This will simplify the work and allow for easier 
management of code as well as less code
'''
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)
#By using a dictionary, it will be easier to access all the different colors defined and accessing this information would be simple
colors = {0 : red, 1 : green, 2 : blue, 3 : darkBlue, 4 : black, 5 : white, 6 : pink}

class BouncingBall:
    def __init__(self, picture_location, radius, length, height, NewImages):
        self.radius = radius
        self.length = length
        self.height = height
        self.index = 1

        self.startingx = random.randint(self.radius, self.length - self.radius)
        self.startingy = random.randint(self.radius, self.height - self.radius)

        self.change_in_x = random.randint(1, 15)
        self.change_in_y = random.randint(1, 10)

        self.center = (self.startingx, self.startingy)
        self.x = self.center[0]
        self.y = self.center[1]
        self.image = pygame.image.load(NewImages[picture_location])

        self.GoingDown = True
        self.GoingRight = True

        self.HitRightCorner = False
        self.HitLeftCorner = False
        self.HitTopCorner = False
        self.HitButtomCorner = False

    def MakeBall(self, screen):

        screen.blit(self.image, (self.center[0], self.center[1]))
        pygame.display.update()


    def playSound():
        mixer.music.load('blip.ogg')
        mixer.music.play()


    def MovingBall(self, screen):

        self.temp_x = self.center[0]
        self.temp_y = self.center[1]
        self.x = self.center[0]
        self.y = self.center[1]

        if(self.y >= self.height - self.radius):
            self.HitTopCorner = False
            self.HitButtomCorner = True
            self.HitRightCorner = False
            self.HitLeftCorner = False

        if(self.y <= self.radius):
            self.HitButtomCorner = False
            self.HitTopCorner = True
            self.HitLeftCorner = False
            self.HitRightCorner = False

        if(self.x >= self.length - self.radius):
            self.HitLeftCorner = False
            self.HitRightCorner = True
            self.HitTopCorner = False
            self.HitButtomCorner = False

        if(self.x <= self.radius):
            self.HitRightCorner = False
            self.HitLeftCorner = True
            self.HitTopCorner = False
            self.HitButtomCorner = False

        self.CheckDirection(screen)
        self.Direction()

    def Direction(self):
        if(self.temp_x < self.x and self.temp_y > self.y):
            self.GoingRight = True
            self.GoingDown = True
        elif(self.temp_x > self.x and self.temp_y > self.y):
            self.GoingRight = False
            self.GoingDown = True
        elif(self.temp_x < self.x and self.temp_y < self.y):
            self.GoingRight = True
            self.GoingDown = False
        else:
            self.GoingRight = False
            self.GoingDown = False

    def CheckDirection(self, screen):
        if(self.HitButtomCorner == True):
            self.hitButtomSide(screen)

        elif(self.HitRightCorner == True):
            self.hitRightSide(screen)

        elif(self.HitLeftCorner == True):
            self.hitLeftSide(screen)

        elif(self.HitTopCorner == True):
            self.hitTopSide(screen)

        else:
            self.jumpingAround(screen)

    def jumpingAround(self, screen):
        if((self.y <= self.height - self.radius and self.y >= self.radius) and (self.x <= self.length - self.radius and self.x >= self.radius)):
            self.x += self.change_in_x
            self.y += self.change_in_y
            self.center = (self.x, self.y)
 
        else:
            self.x -= self.change_in_x
            self.y -= self.change_in_y
            self.center = (self.x, self.y)

        screen.blit(self.image, (self.center[0], self.center[1]))
    def hitButtomSide(self, screen):

        if(self.GoingRight == True):
            if((self.y > self.radius) and (self.x <= self.length - self.radius)):
                self.y -= self.change_in_y
                self.x += self.change_in_x
                self.center = (self.x, self.y)

            else:
                self.y += self.change_in_y
                self.y -= self.change_in_x
                self.center = (self.x, self.y)


        else:
            if((self.y >= self.radius) and (self.x <= self.length - self.radius)):

                self.y -= self.change_in_y
                self.x -= self.change_in_x
                self.center = (self.x, self.y)

            else:

                self.y += self.change_in_y
                self.x += self.change_in_x
                self.center = (self.x, self.y)
        screen.blit(self.image, (self.center[0], self.center[1]))

    def hitRightSide(self, screen):
        if(self.GoingDown == True):
            if((self.x >= self.radius) and ((self.y <= self.height - self.radius) and (self.y >= self.radius))):

                self.x -= self.change_in_x
                self.y -= self.change_in_y
                self.center = (self.x, self.y)
                
            else:
                self.x += self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)


        else:
            if((self.x >= self.radius) and ((self.y <= self.height - self.radius) and ( self.y >= self.radius))):
                self.x -= self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)


            else:
                self.x += self.change_in_x
                self.y -= self.change_in_y
                self.center = (self.x, self.y)
        screen.blit(self.image, (self.center[0], self.center[1]))

    def hitLeftSide(self, screen):

        if(self.GoingDown == False):
            if((self.x <= self.length - self.radius) and (self.y >= self.radius and self.y <= self.height - self.radius)):
                self.x += self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)

            else:
                self.x -= self.change_in_x
                self.y -= self.change_in_y
                self.center = (self.x, self.y)

        else:
            if((self.x <= self.length - self.radius) and ((self.y >= self.radius) and (self.y <= self.height - self.radius))):

                self.x += self.change_in_x
                self.y -= self.change_in_y
                self.center = (self.x, self.y)
            else:
                self.x -= self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)
        screen.blit(self.image, (self.center[0], self.center[1]))

    def hitTopSide(self, screen):
        if(self.GoingRight == False):
            if((self.y <= abs(self.height - self.radius)) and (self.y >= self.radius) and (self.x > self.radius) and (self.x <= abs(self.height - self.radius))):
                self.x -= self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)
                
            else:
                self.x -= self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)

        else:
            if((self.y >= self.radius) and (self.x >= self.radius)):
                self.x += self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)

            else:
                self.x += self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)

        screen.blit(self.image, (self.center[0], self.center[1]))


def getPixelArray(filename):
    """ Open file, load image and convert it to 3D pixel array. """
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        print "Cannot load image:", filename
        raise SystemExit, message

    return pygame.surfarray.array3d(image)

def main():
    length = 640
    height = 480
    screen = pygame.display.set_mode((length, height))
    list = []
    x = random.randint(4, 10)
    while(x % 2 != 0):
        x = random.randint(4, 10)

    OriginalPictures = []
    Images = []
    SplitImagesArray = []
    NewImages = []

    First_picture = getPixelArray('example.jpg')
    Second_picture = getPixelArray('puppy.jpg')
    Third_picture = getPixelArray('GoldenGateBridge.jpg')
    Fourth_picture = getPixelArray('Family_Picture.jpg')
    Fifth_picture = getPixelArray('Goat.jpg')

    OriginalPictures.append(First_picture)
    OriginalPictures.append(Second_picture)
    OriginalPictures.append(Third_picture)
    OriginalPictures.append(Fourth_picture)
    OriginalPictures.append(Fifth_picture)

    Images.append('example.jpg')
    Images.append('puppy.jpg')
    Images.append('GoldenGateBridge.jpg')
    Images.append('Family_Picture.jpg')
    Images.append('Goat.jpg')

    for i in range(len(OriginalPictures)):

        LoadImage = pygame.image.load(Images[i])
        ImageDimension = LoadImage.get_rect().size
        temp1 = OriginalPictures[i][ImageDimension[0]/2: , : , :]
        temp2 = OriginalPictures[i][ :ImageDimension[1]/2, :, : ]
        AlteredImage1 = pygame.surfarray.make_surface(temp1)
        AlteredImage2 = pygame.surfarray.make_surface(temp2)

        AlteredImage1 = pygame.transform.scale(AlteredImage1, (100, 100))
        AlteredImage2 = pygame.transform.scale(AlteredImage2, (100, 100))

        SplitImagesArray.append(AlteredImage1)
        SplitImagesArray.append(AlteredImage2)

    pygame.image.save(SplitImagesArray[0], 'Flower1.jpg')
    pygame.image.save(SplitImagesArray[1], 'Flower2.jpg')
    pygame.image.save(SplitImagesArray[2], 'Puppy1.jpg')
    pygame.image.save(SplitImagesArray[3], 'Puppy2.jpg')
    pygame.image.save(SplitImagesArray[4], 'GoldenBridge1.jpg')
    pygame.image.save(SplitImagesArray[5], 'GoldenBridge2.jpg')
    pygame.image.save(SplitImagesArray[6], 'Family_picture1.jpg')
    pygame.image.save(SplitImagesArray[7], 'Family_picture2.jpg')
    pygame.image.save(SplitImagesArray[8], 'Goat1.jpg')
    pygame.image.save(SplitImagesArray[9], 'Goat2.jpg')

    NewImages.append('Flower1.jpg')
    NewImages.append('Flower2.jpg')
    NewImages.append('Puppy1.jpg')
    NewImages.append('Puppy2.jpg')
    NewImages.append('GoldenBridge1.jpg')
    NewImages.append('GoldenBridge2.jpg')
    NewImages.append('Family_picture1.jpg')
    NewImages.append('Family_picture2.jpg')
    NewImages.append('Goat1.jpg')
    NewImages.append('Goat2.jpg')


    for i in range(x):
        list.append(BouncingBall(i, 25, length, height, NewImages))
    for ball in range(len(list)):
        list[ball].MakeBall(screen)

    Ready = False
    pygame.display.set_caption("Basic Pygame Program")
    while (Ready == False):
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
        background = pygame.Surface(screen.get_size())
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (150, height/2, 300, 100))

        font = pygame.font.Font(None, 36)
        text = font.render("Let's Start", 1, (255, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx - 20
        textpos.centery = background.get_rect().centery + 50
        screen.blit(text, textpos)
        
        text = font.render("Welcome", 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        screen.blit(text, textpos)
        text = font.render("This game is designed to test your ability", 1 ,(255, 255, 255))
        textpos = text.get_rect()
        textpos.centery = background.get_rect().centery - 100
        textpos.centerx = background.get_rect().centerx
        screen.blit(text, textpos)
        text = font.render("to recognize a picture when split in two pieces", 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.centery = background.get_rect().centery - 70
        textpos.centerx = background.get_rect().centerx
        screen.blit(text, (textpos))

        mouse_position_x = pygame.mouse.get_pos()[0]
        mouse_position_y = pygame.mouse.get_pos()[1]

        if(mouse_position_x > 200 and mouse_position_x < 500 and mouse_position_y > 240 and mouse_position_y < 340):
            if(pygame.mouse.get_pressed() == (1, 0, 0)):
                Ready = True
            else:
                Ready = False
        pygame.display.update()

    pygame.time.wait(1000)
    stop = t.time() + 10    #this gives the user 10 seconds to look at the pictures
	
    while t.time() < stop:  #will run depending on whether the condition is still true
        screen.fill((0, 0, 0))

        for i in range(len(list)):
            list[i].MovingBall(screen)

        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
        msElapse = clock.tick(FPS)
        pygame.display.update()
    screen.fill((255, 255, 255))
    pygame.display.update()
    
    #At this point, I am going to be asking the user how many whole pictures they saw moving around
    text = font.render("Now that you have seen all the pictures", 1, colors[3])
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery - 20
    screen.blit(text, textpos)
    
    text = font.render("How many whole pictures did you see?", 1, colors[0])
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery + 20
    screen.blit(text, textpos)
    
    pygame.display.update()
    
    var = 0
    counter = 0
    while(var != len(list)/2):                      
    	var = int(input("How many whole images did you see: "))
    	counter += 1
    	
    if(counter == 1):
    	print "Wow, you are really good at this. Hope you can come back and play again"
    elif(counter > 1 and counter < len(list)/2):
    	print "You are are almost there. Keep playing to improve you skills"
    else: 
    	print "It seems that you still have room for improvement because you attempted it %d times where there was only %d images" % (counter, len(list)/2)
    	
    pygame.quit()
    sys.exit()	

if __name__ == "__main__":
    main()
