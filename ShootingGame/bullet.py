import pygame
# define a class to show the functions of the bullet1
class Bullet1(pygame.sprite.Sprite):
    def __init__(self,position):
        #Initializing
        pygame.sprite.Sprite.__init__(self)
        #upload the image of bullet1
        self.image=pygame.image.load('images/bullet1.png').convert_alpha()
        # Get the rectangle where the bullet is located
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        # set the speed of the shooting bullets
        self.speed=12
        # if the bullets can shoot
        self.active=True
        # Set markers to check for collisions in non-transparent parts
        self.mask=pygame.mask.from_surface(self.image)
    # Defining the trajectory of a bullet
    def move(self):
        self.rect.top=self.rect.top-self.speed
        if self.rect.top<0:
            self.active=False
    #When the bullet hits the target, the bullet movement needs to be reinitialised
    def reset(self,position):
        self.rect.left,self.rect.top=position
        self.active=True
# define a class to show the functions of the bullet2
class Bullet2(pygame.sprite.Sprite):
    def __init__(self,position):
        #Initializing
        pygame.sprite.Sprite.__init__(self)
        #upload the image of bullet1
        self.image=pygame.image.load('images/bullet2.png').convert_alpha()
        # Get the rectangle where the bullet is located
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        # set the speed of the shooting bullets
        self.speed=30
        # if the bullets can shoot
        self.active=True
        # Set markers to check for collisions in non-transparent parts
        self.mask=pygame.mask.from_surface(self.image)
    # Defining the trajectory of a bullet
    def move(self):
        self.rect.top=self.rect.top-self.speed
        if self.rect.top<0:
            self.active=False
    #When the bullet hits the target, the bullet movement needs to be reinitialised
    def reset(self,position):
        self.rect.left,self.rect.top=position
        self.active=True
