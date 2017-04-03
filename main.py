import pygame
import carmodule
import random
from block import Block



def crash(score):
    pygame.quit()
    print("You crashed!")
    print("Final Score is : ",str(score))
    quit()

def main():
    pygame.init()   #Initialize Pygame

	#Initializing display resolution variables
    display_width = 800
    display_height = 600

	#Initializing color tuples in format (r, g, b)
    black = (0, 0, 0)
    white = (255, 255, 255)

    game_display = pygame.display.set_mode((display_width, display_height))   #Initialize Main screen size
    pygame.display.set_caption('Codecell Wars')   #Game's Name (Comes in title bar)
    clock = pygame.time.Clock() #Time with respect to game

    '''
        Pygame works in a loop
        The exit_game variable is a boolean flag to indicate if the loop needs\
                to be exited.
    '''

    exit_game = False 

    car_image = pygame.image.load('racecar.png')    #Load car sprite
    car_dimensions = car_image.get_rect().size    #Get car dimensions in form of a tuple
    mycar = carmodule.car(car_image, (display_width*0.45), (display_height*0.8), boundary_left = 100, boundary_right = 700 - car_dimensions[0])    #Create object for first car with default key_bindings
    '''
        Add two player functionality
    '''
    #random obstacles
    block_startx = random.randrange(0,display_width)
    block_starty = -600
    block_speed = 7
    block_width = 100
    block_height = 100

    dodged = 0
    


    while not exit_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
        mycar.move_car(event)
        game_display.fill(white)
        mycar.draw_car(game_display)

        #def __init__(self, X,Y, width, height, speed, color,game_display):
        block = Block(block_startx, block_starty, block_width,
         block_height, block_speed, black, game_display)
       
        block_starty += block_speed 

        if(x>display_width-car_width or x<0):
            crash()
        if(thing_starty>display_height):
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged+=1
            #thing_speed +=0.5 increase speed
            thing_width+= (dodged * 1.2)

        if y<thing_starty+thing_height:
            if x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
                crash() 
        
        pygame.display.update() #Update the screen
                                #If parameter is mentioned, update only that part

        block.draw(block_starty)
        clock.tick(60)  #Frames per second

    pygame.quit() #Exit pygame
    quit() #Exit program overall

if __name__ == "__main__":
    main()
