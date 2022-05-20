import pygame
# define a class of the plane
class MyPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        #Initializing
        pygame.sprite.Sprite.__init__(self)
        #upload the image of plane 1 and plane 2
        self.image1=pygame.image.load('images/plane1.png').convert_alpha()
        self.image2=pygame.image.load('images/plane2.png').convert_alpha()
        # get the function of destroy()
        self.destroy_images=list()
        self.destroy_images.extend([\
            pygame.image.load('images/plane2_destroy1.png').convert_alpha(),\
            pygame.image.load('images/plane2_destroy2.png').convert_alpha(),\
            pygame.image.load('images/plane2_destroy3.png').convert_alpha(),\
            pygame.image.load('images/plane2_destroy3.png').convert_alpha()\
            ])
        # Get the rectangle where the plane is located
        self.rect=self.image1.get_rect()
        #get the size of the background
        self.width,self.height=bg_size[0],bg_size[1]
        #set the position of the plane_image
        self.rect.left,self.rect.top=(self.width-self.rect.width)//2,\
                                      self.height-self.rect.height-60
        # set the speed of the moving myplane
        self.speed=10
        # if the enemy-plane can still be alive
        self.active=True
        # setting safe-period for reset myplane
        self.invincible=False
        # Set markers to check for collisions in non-transparent parts
        self.mask=pygame.mask.from_surface(self.image1)
    # Check if the plane will move beyond the upper end of the background
    def moveup(self):
        if self.rect.top>0:
            self.rect.top=self.rect.top-self.speed
        else:
            self.rect.top=0
    # Check if the plane will move beyond the bottom of the background
    def movedown(self):
        if self.rect.bottom<self.height-60:
            self.rect.top=self.rect.top+self.speed
        else:
            self.rect.bottom=self.height-60
    #Check if the plane will move beyond the left of the background
    def moveleft(self):
        if self.rect.left>0:
            self.rect.left=self.rect.left-self.speed
        else:
            self.rect.left=0
    # Check if the plane will move beyond the right of the background
    def moveright(self):
        if self.rect.right<self.width:
            self.rect.left=self.rect.left+self.speed
        else:
            self.rect.right=self.width
    # reset the lives of myplane
    def reset(self):
        #set the position of the plane_image
        self.rect.left,self.rect.top=(self.width-self.rect.width)//2,\
                                      self.height-self.rect.height-60
        self.active=True
        self.invincible=True 
