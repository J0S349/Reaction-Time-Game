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

''' This class is designed to allow the images to be bouncing off the sides of the GUI that is created. Each one of the objects that are created will have, in most cases
	a different starting point and different slopes. This will make the objects seem as if they are moving at different speeds across the screen which will make it more 
	difficult for the user to keep track of what is happening. 
'''
class BouncingBall:
    def __init__(self, picture_location, radius, length, height, NewImages):	#This constructer will be used to initialize the different objects
        self.radius = radius
        self.length = length
        self.height = height
        self.index = 1
		
		#This will be used to initiate the starting position for the objects
        self.startingx = random.randint(self.radius, self.length - self.radius)
        self.startingy = random.randint(self.radius, self.height - self.radius)
		#This bottom code will be used to initialize the different slopes for each objects
        self.change_in_x = random.randint(1, 15)	
        self.change_in_y = random.randint(1, 10)

        self.center = (self.startingx, self.startingy)
        self.x = self.center[0]
        self.y = self.center[1]
        self.image = pygame.image.load(NewImages[picture_location])
		#since we want to have the object start moving, we need to predefine the way it should move
        self.GoingDown = True
        self.GoingRight = True

		#Since the object is going to be starting somewhere in the middle of the GUI, it still hasn't hit a wall yet so we need to 
		#initialize each one of the objects to false
        self.HitRightCorner = False
        self.HitLeftCorner = False
        self.HitTopCorner = False
        self.HitButtomCorner = False
	
		#this function will create create the objects and plot them on the GUI
    def MakeBall(self, screen):
        screen.blit(self.image, (self.center[0], self.center[1]))
        pygame.display.update()

		#this functon will be used to check where the object is currently at and whether it has hit any of the sides
    def MovingBall(self, screen):

        self.temp_x = self.center[0]
        self.temp_y = self.center[1]
        self.x = self.center[0]
        self.y = self.center[1]

        if(self.y >= self.height - self.radius):	#we need to check the objects current central position and see whether it has hit or passed one of the 
        											#edges
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

		#this function will be used to change the direction that the object is going to go. Within this function we need to check to 
		# see what direction and corner the object hit and change its direction which is based on the directions the object was moving
		# before and what side it hit
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

		#this function will use the directions of the object and use it to calculate update its next position
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
		
		#this function will be called whenever the object itself has not yet hit any walls and is just on moving in between the GUI
    def jumpingAround(self, screen):
        if((self.y <= self.height - self.radius and self.y >= self.radius) and (self.x <= self.length - self.radius and self.x >= self.radius)):
            self.x += self.change_in_x
            self.y += self.change_in_y
            self.center = (self.x, self.y)
 
        else:
            self.x -= self.change_in_x
            self.y -= self.change_in_y
            self.center = (self.x, self.y)
		#Once we have updated the objects current position, then we need to plot the object in the new position
        screen.blit(self.image, (self.center[0], self.center[1]))
        
        #this function will be called when the object has hit the buttom of the screen. Once it has hit it, the program will then have it 'bounce' off the 
        #screen and move in a different direction which is based on the direction that it was going before it hit the wall
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

	#this function will be called when the object has hit the right side of the GUI. The program will then need to change the direction of where
	#the object will be moving towards. The direction of where the object will move will be based completely on the previous direction of where it was going
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
        #since the object's center position has changed, we need to update this change to the GUI
        screen.blit(self.image, (self.center[0], self.center[1]))
	
	#this function will be called when the object has hit the Left side of the GUI
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
        
	#This function will be called when the objects has hit the top of the GUI. It will then recalculate the direction that the object will move. The new direction that
	#it will go will be based on what direction it was previously going
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
#this function will be used to convert the picture into a 3 dimensal array 
def getPixelArray(filename):
    """ Open file, load image and convert it to 3D pixel array. """
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        print "Cannot load image:", filename
        raise SystemExit, message

    return pygame.surfarray.array3d(image)
''' In the main is where all the objects will be created and is where the image manipulation will be happening '''
def main():

	#before we start to use our GUI, we need to first create the instance of it.
    screen = pygame.display.set_mode((length, height))
    list = []	#we create a list because it will be used to store our objects in and will allow for us to access it simpler
    x = random.randint(4, 10)	#the x will be used to determine how many objecst we will crete
    while(x % 2 != 0):		#this while loop will make sure that the number that is generated is divisable by two because a whole image will consist of two parts
        x = random.randint(4, 10)
	
	#This list will store different parts of the object that will be used to create the function
    OriginalPictures = []
    Images = []
    SplitImagesArray = []
    NewImages = []
	
	#we need to start by storing all the information from the image into a more usable form. Such as a 3D array 
    First_picture = getPixelArray('example.jpg')
    Second_picture = getPixelArray('puppy.jpg')
    Third_picture = getPixelArray('GoldenGateBridge.jpg')
    Fourth_picture = getPixelArray('Family_Picture.jpg')
    Fifth_picture = getPixelArray('Goat.jpg')
	
	#we then add these arrays into the list
    OriginalPictures.append(First_picture)
    OriginalPictures.append(Second_picture)
    OriginalPictures.append(Third_picture)
    OriginalPictures.append(Fourth_picture)
    OriginalPictures.append(Fifth_picture)
	
	#we then add the images into a list for later use
    Images.append('example.jpg')
    Images.append('puppy.jpg')
    Images.append('GoldenGateBridge.jpg')
    Images.append('Family_Picture.jpg')
    Images.append('Goat.jpg')

    for i in range(len(OriginalPictures)):	#this loop will be used to split the 
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
        for event in pygame.event.get():			#this loop is used for canceling the program when the user presses the X on the top right of the GUI
                    if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
                       
        background = pygame.Surface(screen.get_size())	#this will get the dimension of the GUI 
        screen.fill(colors[4])
        pygame.draw.rect(screen, colors[5], (150, height/2, 300, 100))
		
		#These new few lines of code will be used to create shapes within the GUI that will mak it more appealing for the user when playing
        font = pygame.font.Font(None, 36)
        text = font.render("Let's Start", 1, colors[0])
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx - 20
        textpos.centery = background.get_rect().centery + 50
        screen.blit(text, textpos)
        #These new few lines of code will be used to create shapes within the GUI that will mak it more appealing for the user when playing
        text = font.render("Welcome", 1, colors[5])
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        screen.blit(text, textpos)
        text = font.render("This game is designed to test your ability", 1 , colors[5])
        textpos = text.get_rect()
        textpos.centery = background.get_rect().centery - 100
        textpos.centerx = background.get_rect().centerx
        screen.blit(text, textpos)
        text = font.render("to recognize a picture when split in two pieces", 1, colors[5])
        textpos = text.get_rect()
        textpos.centery = background.get_rect().centery - 70
        textpos.centerx = background.get_rect().centerx
        screen.blit(text, (textpos))
		#Within this game, we are also using the computers mouse location and whether they clicked it or not to determine whether they clicked the "Let's Start" button
		#in the GUI
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
        screen.fill(colors[4])

        for i in range(len(list)):		#this will print out all the objects into the screen
            list[i].MovingBall(screen)

        for event in pygame.event.get():		#again, we want to allow the user the ability to close the window while the program is running
                    if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
        msElapse = clock.tick(FPS)	
        pygame.display.update()
    screen.fill(colors[5])
    pygame.display.update()
    
    #At this point, I am going to be asking the user how many whole pictures they saw moving around
    screen.fill(colors[4])
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
    #The code below is used for getting the user's input. The user can only insert information to the program from within the terminal 
    #The code below also contains the code for the scoring system
    
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
    
    
    play_again = raw_input("Would you like to play again (Y or N): ")		#if the user would like to play again, they should have the option to do so. 
    																		#Since the program uses a GUi, the user cannot forget to go back to the pygame window 
    if(play_again == "y" or play_again == "Y"):
    	main()
    	
    print "Thanks for playing. Hope to see you soon"
    pygame.quit()
    sys.exit()	

if __name__ == "__main__":
    main()
