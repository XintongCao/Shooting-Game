import pygame
from random import *
# define a class of small enemy-plane
class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        #Initializing
        pygame.sprite.Sprite.__init__(self)
        #upload the image of small enemy-planes
        self.image=pygame.image.load('images/enemy1.png').convert_alpha()
        # get the function of destroy()
        self.destroy_images=list()
        self.destroy_images.extend([\
            pygame.image.load('images/enemy1_down1.png').convert_alpha(),\
            pygame.image.load('images/enemy1_down2.png').convert_alpha(),\
            pygame.image.load('images/enemy1_down3.png').convert_alpha(),\
            pygame.image.load('images/enemy1_down4.png').convert_alpha()\
            ])
        # Get the rectangle where the enemy-plane is located
        self.rect=self.image.get_rect()
        #get the size of the background
        self.width,self.height=bg_size[0],bg_size[1]
        # set the speed of the moving enemy-plane
        self.speed=2
        # if the enemy-plane can still be alive
        self.active=True
        #set the position of the plane_image
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),\
                                     randint(-5*self.height,0)
        # Set markers to check for collisions in non-transparent parts
        self.mask=pygame.mask.from_surface(self.image)
    # define a function to show how the enemy-plane moves
    def move(self):
        if self.rect.top<self.height:
            self.rect.top=self.rect.top+self.speed
        else:
            # Initializing the position of the enemy-planes
            self.reset()
    # define a function to reset the position of the enemy planes
    def reset(self):
        # if the enemy-plane can still be alive
        self.active=True
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),\
                                     randint(-5*self.height,0)

# define a class of middle-size enemy-plane
class MidEnemy(pygame.sprite.Sprite):
    #define the energy that a plane can carry
    energy=8
    def __init__(self,bg_size):
        #Initializing
        pygame.sprite.Sprite.__init__(self)
        #upload the image of middle-size enemy-planes
        self.image=pygame.image.load('images/enemy2.png').convert_alpha()
        self.image_hit=pygame.image.load('images/enemy2_hit.png').convert_alpha()
        # get the function of destroy()
        self.destroy_images=list()
        self.destroy_images.extend([\
            pygame.image.load('images/enemy2_down1.png').convert_alpha(),\
            pygame.image.load('images/enemy2_down2.png').convert_alpha(),\
            pygame.image.load('images/enemy2_down3.png').convert_alpha(),\
            pygame.image.load('images/enemy2_down4.png').convert_alpha()\
            ])
        # Get the rectangle where the enemy-plane is located
        self.rect=self.image.get_rect()
        #get the size of the background
        self.width,self.height=bg_size[0],bg_size[1]
        # set the speed of the moving enemy-plane
        self.speed=1
        # if the enemy-plane can still be alive
        self.active=True
        #set the position of the plane_image
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),\
                                     randint(-10*self.height,-self.height)
        # Set markers to check for collisions in non-transparent parts
        self.mask=pygame.mask.from_surface(self.image)
        # set the energy variable
        self.energy=MidEnemy.energy
        # setting if no hitting
        self.hit=False
    # define a function to show how the enemy-plane moves
    def move(self):
        if self.rect.top<self.height:
            self.rect.top=self.rect.top+self.speed
        else:
            # Initializing the position of the enemy-planes
            self.reset()
    # define a function to reset the position of the enemy planes
    def reset(self):
        # if the enemy-plane can still be alive
        self.active=True
        self.energy=MidEnemy.energy
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),\
                                     randint(-10*self.height,-self.height)
# define a class of big enemy-plane
class BigEnemy(pygame.sprite.Sprite):
    #define the energy that a plane can carry
    energy=20
    def __init__(self,bg_size):
        #Initializing
        pygame.sprite.Sprite.__init__(self)
        #upload the image of big enemy-planes
        self.image1=pygame.image.load('images/enemy3_n1.png').convert_alpha()
        self.image2=pygame.image.load('images/enemy3_n2.png').convert_alpha()
        self.image_hit=pygame.image.load('images/enemy3_hit.png').convert_alpha()
        # get the function of destroy()
        self.destroy_images=list()
        self.destroy_images.extend([\
            pygame.image.load('images/enemy3_down1.png').convert_alpha(),\
            pygame.image.load('images/enemy3_down2.png').convert_alpha(),\
            pygame.image.load('images/enemy3_down3.png').convert_alpha(),\
            pygame.image.load('images/enemy3_down4.png').convert_alpha(),\
            pygame.image.load('images/enemy3_down5.png').convert_alpha(),\
            pygame.image.load('images/enemy3_down6.png').convert_alpha()\
            ])
        # Get the rectangle where the enemy-plane is located
        self.rect=self.image1.get_rect()
        #get the size of the background
        self.width,self.height=bg_size[0],bg_size[1]
        # set the speed of the moving enemy-plane
        self.speed=1
        # if the enemy-plane can still be alive
        self.active=True
        #set the position of the plane_image
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),\
                                     randint(-15*self.height,-5*self.height)
        # Set markers to check for collisions in non-transparent parts
        self.mask=pygame.mask.from_surface(self.image1)
        # set the energy variable
        self.energy=BigEnemy.energy
        # setting if no hitting
        self.hit=False
    # define a function to show how the enemy-plane moves
    def move(self):
        if self.rect.top<self.height:
            self.rect.top=self.rect.top+self.speed
        else:
            # Initializing the position of the enemy-planes
            self.reset()
    # define a function to reset the position of the enemy planes
    def reset(self):
        # if the enemy-plane can still be alive
        self.active=True
        self.energy=BigEnemy.energy
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),\
                                     randint(-15*self.height,-5*self.height)
