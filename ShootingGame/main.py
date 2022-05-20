import pygame
import sys
import traceback
import myplane
import bullet
import enemy
import supply
from random import *
# Initializing pygame module
pygame.init()
# set background size, screen and title of this game
bg_size=width,height=480,700
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption('Shooting Game -- <Plane>')
# upload the background
background=pygame.image.load('images/background.png').convert()
# define the color of blood trough
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)
# define a function to add small enemy plane into the background
def add_small_enemies(group1,group2,num):
    for i in range(num):
        e1=enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)
# define a function to add middle enemy plane into the background
def add_mid_enemies(group1,group2,num):
    for i in range(num):
        e2=enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)
# define a function to add big enemy plane into the background
def add_big_enemies(group1,group2,num):
    for i in range(num):
        e3=enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)
# define a function to show the increasing speed
def increase_speed(target,inc):
    for each in target:
        each.speed=each.speed+inc
# define a main function to run this game
def main():
    # initializing an object of myplane
    me=myplane.MyPlane(bg_size)
    # initializing an object of enemy-plane
    enemies=pygame.sprite.Group()
    # Generate small enemy planes
    small_enemies=pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,15)
    # Generate middle enemy planes
    mid_enemies=pygame.sprite.Group()
    add_mid_enemies(mid_enemies,enemies,4)
    # Generate big enemy planes
    big_enemies=pygame.sprite.Group()
    add_big_enemies(big_enemies,enemies,2)
    # generate the bullet1
    bullet1=list()
    bullet1_index=0
    bullet1_num=4
    for piece_bullet in range(bullet1_num):
        bullet1.append(bullet.Bullet1(me.rect.midtop))
    # generate the bullet2
    bullet2=list()
    bullet2_index=0
    bullet2_num=8
    for i in range(bullet2_num):
        bullet2.append(bullet.Bullet2(me.rect.midtop))

    #Setting frame rate
    clock=pygame.time.Clock()
    # Index of pictures after being shot
    enemy1_destroy_index=0
    enemy2_destroy_index=0
    enemy3_destroy_index=0
    plane2_destroy_index=0
    # calculating the player's score
    score=0
    # define the font
    score_font=pygame.font.Font(None,36)
    # set the images to show if the game was paused
    paused=False
    pause_nor_image=pygame.image.load('images/pause_nor.png').convert_alpha()
    pause_pressed_image=pygame.image.load('images/pause_pressed.png').convert_alpha()
    resume_nor_image=pygame.image.load('images/resume_nor.png').convert_alpha()
    resume_pressed_image=pygame.image.load('images/resume_pressed.png').convert_alpha()
    paused_rect=pause_nor_image.get_rect()
    paused_rect.left,paused_rect.top=width-paused_rect.width-10,10
    paused_image=pause_nor_image
    # set the difficulty levels
    level=1
    # set the bombs
    bomb_image=pygame.image.load('images/bomb.png').convert_alpha()
    bomb_rect=bomb_image.get_rect()
    bomb_font=pygame.font.Font(None,48)
    bomb_num=3
    # Trigger a resupply pack every 30 seconds
    bullet_supply=supply.Bullet_Supply(bg_size)
    bomb_supply=supply.Bomb_Supply(bg_size)
    supply_time=pygame.USEREVENT
    pygame.time.set_timer(supply_time,30*1000)
    # setting the timer for bullet2
    bullet2_time=pygame.USEREVENT+1
    #setting to show if the player will use the bullet2
    is_bullet2=False
    # Unlock the timer for the safety period of my plane
    invincible_time=pygame.USEREVENT+2

    # numbers of myplane's lives
    life_image=pygame.image.load('images/life.png').convert_alpha()
    life_rect=life_image.get_rect()
    life_num=3
    # setting to limit the times of recording score
    recorded=False

    # ending of the game
    gameover_font=pygame.font.Font(None,48)
    again_image=pygame.image.load('images/again.png').convert_alpha()
    again_rect=again_image.get_rect()
    gameover_image=pygame.image.load('images/gameover.png').convert_alpha()
    gameover_rect=gameover_image.get_rect()

    # change myplanes between plane1 and plane2
    switch_image=True
    #Set delay time for switching images
    delay=100

    running=True
    # when the game starts:
    while running:
        # ending the game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            # check if player pressed the pause button
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1 and paused_rect.collidepoint(event.pos):
                    paused=not paused
                    if paused:
                        pygame.time.set_timer(supply_time,0)
                    else:
                        pygame.time.set_timer(supply_time,30*1000)
            # set the images of the pause motion
            elif event.type==pygame.MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image=resume_pressed_image
                    else:
                        paused_image=pause_pressed_image
                else:
                    if paused:
                        paused_image=resume_nor_image
                    else:
                        paused_image=pause_nor_image
            # setting for using the bombs
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if bomb_num:
                        bomb_num=bomb_num-1
                        for each in enemies:
                            if each.rect.bottom>0:
                                each.active=False
            # setting for Triggering a resupply pack (bombs)
            elif event.type==supply_time:
                if choice([True,False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
            # setting for Triggering a resupply pack (bullet2)
            elif event.type==bullet2_time:
                is_bullet2=False
                pygame.time.set_timer(bullet2_time,0)

            elif event.type==invincible_time:
                me.invincible=False
                pygame.time.set_timer(invincible_time,0)

        # Increasing difficulty depending on the player's score
        if level==1 and score>500:
            level=2
            # in level2,adding 3 small planes,2 mid-planes and one big plane
            add_small_enemies(small_enemies,enemies,3)
            add_mid_enemies(mid_enemies,enemies,2)
            add_big_enemies(big_enemies,enemies,1)
            # increase the speed of the small planes
            increase_speed(small_enemies,1)
        elif level==2 and score>1000:
            level=3
            # in level3,adding 5 small planes,3 mid-planes and 2 big plane
            add_small_enemies(small_enemies,enemies,5)
            add_mid_enemies(mid_enemies,enemies,3)
            add_big_enemies(big_enemies,enemies,2)
            # increase the speed of the small planes and mid_planes
            increase_speed(small_enemies,1)
            increase_speed(mid_enemies,1)
        elif level==3 and score>1500:
            level=4
            # in level4,adding 5 small planes,3 mid-planes and 2 big plane
            add_small_enemies(small_enemies,enemies,5)
            add_mid_enemies(mid_enemies,enemies,3)
            add_big_enemies(big_enemies,enemies,2)
            # increase the speed of the small planes and mid_planes
            increase_speed(small_enemies,1)
            increase_speed(mid_enemies,1)
        elif level==4 and score>2000:
            level=5
            # in level5,adding 5 small planes,3 mid-planes and 2 big plane
            add_small_enemies(small_enemies,enemies,5)
            add_mid_enemies(mid_enemies,enemies,3)
            add_big_enemies(big_enemies,enemies,2)
            # increase the speed of the small planes and mid_planes
            increase_speed(small_enemies,1)
            increase_speed(mid_enemies,1)

        # set the background
        screen.blit(background,(0,0))
        if life_num and not paused:
            # check and follow the keyboard movements by player
            key_pressed=pygame.key.get_pressed()
            if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
                me.moveup()
            elif key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
                me.movedown()
            elif key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
                me.moveleft()
            elif key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
                me.moveright()

            # adding resupply-bombs and checking if the player receives the supply
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image,bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply,me):
                    if bomb_num<3:
                        bomb_num=bomb_num+1
                    bomb_supply.active=False
            # adding resupply-bullets and checking if the player receives the supply
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image,bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply,me):
                    is_bullet2=True
                    pygame.time.set_timer(bullet2_time,18*1000)
                    bullet_supply.active=False

            #Set so that bullets are fired in sequence
            if not(delay%10):
                if is_bullet2:
                    bullets=bullet2
                    bullets[bullet2_index].reset(me.rect.midtop)

                    bullet2_index=(bullet2_index+1)%bullet2_num
                else:
                    bullets=bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index=(bullet1_index+1)%bullet1_num
            #Checking whether a bullet has hit an enemy planes
            for each_bullet in bullets:
                if each_bullet.active:
                    each_bullet.move()
                    screen.blit(each_bullet.image,each_bullet.rect)
                    enemy_hit=pygame.sprite.spritecollide(each_bullet,enemies,False,pygame.sprite.collide_mask)
                    if enemy_hit:
                        each_bullet.active=False
                        for each_enemy in enemy_hit:
                            #each_enemy.active=False

                            if each_enemy in mid_enemies or each_enemy in big_enemies:
                                each_enemy.hit=True
                                each_enemy.energy=each_enemy.energy-1
                                if each_enemy.energy==0:
                                    each_enemy.active=False
                            else:
                                each_enemy.active=False


            # add big enemy plane on the background
            for each in big_enemies:
                # if the enemy-plane can still be alive
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit,each.rect)
                        each.hit=False
                    else:
                        if switch_image:
                            screen.blit(each.image1,each.rect)
                        else:
                            screen.blit(each.image2,each.rect)
                    # Drawing the blood trough
                    pygame.draw.line(screen,black,(each.rect.left,each.rect.top-5),\
                                                  (each.rect.right,each.rect.top-5),4)
                    # When the remaining energy is greater than 20%, the blood tank shows green
                    # otherwise it shows red
                    energy_remain=each.energy/enemy.BigEnemy.energy
                    if energy_remain>0.2:
                        energy_color=green
                    else:
                        energy_color=red
                    pygame.draw.line(screen,energy_color,\
                                    (each.rect.left,each.rect.top-5),\
                                    (each.rect.left+each.rect.width*energy_remain,\
                                     each.rect.top-5),4)
                else:
                    # if the enemies was shot down
                    if not (delay%3):
                        screen.blit(each.destroy_images[enemy3_destroy_index],each.rect)
                        #There are six images in total
                        #When a picture index value divisible by 6 is obtained, a new cycle will start
                        enemy3_destroy_index=(enemy3_destroy_index+1)%6
                        if enemy3_destroy_index==0:
                            score=score+100
                            each.reset()
            # add middle enemy plane on the background
            for each in mid_enemies:
                # if the enemy-plane can still be alive
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit,each.rect)
                        each.hit=False
                    else:
                        screen.blit(each.image,each.rect)
                    # Drawing the blood trough
                    pygame.draw.line(screen,black,(each.rect.left,each.rect.top-5),\
                                                  (each.rect.right,each.rect.top-5),4)
                    # When the remaining energy is greater than 20%, the blood tank shows green
                    # otherwise it shows red
                    energy_remain=each.energy/enemy.MidEnemy.energy
                    if energy_remain>0.2:
                        energy_color=green
                    else:
                        energy_color=red
                    pygame.draw.line(screen,energy_color,\
                                    (each.rect.left,each.rect.top-5),\
                                    (each.rect.left+each.rect.width*energy_remain,\
                                     each.rect.top-5),4)
                else:
                    # if the enemies was shot down
                    if not (delay%3):
                        screen.blit(each.destroy_images[enemy2_destroy_index],each.rect)
                        #There are four images in total
                        #When a picture index value divisible by 4 is obtained, a new cycle will start
                        enemy2_destroy_index=(enemy2_destroy_index+1)%4
                        if enemy2_destroy_index==0:
                            score=score+50
                            each.reset()
            # add small enemy plane on the background
            for each in small_enemies:
                # if the enemy-plane can still be alive
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                else:
                    # if the enemies was shot down
                    if not (delay%3):
                        screen.blit(each.destroy_images[enemy1_destroy_index],each.rect)
                        #There are four images in total
                        #When a picture index value divisible by 4 is obtained, a new cycle will start
                        enemy1_destroy_index=(enemy1_destroy_index+1)%4
                        if enemy1_destroy_index==0:
                            score=score+10
                            each.reset()
            # check if my plane was hit
            collision=pygame.sprite.spritecollide(me,enemies,False,pygame.sprite.collide_mask)
            if collision and not me.invincible:
                me.active=False
                for each_collision in collision:
                    each_collision.active=False
            # add myplane on the background
            if me.active:
                if switch_image:
                    screen.blit(me.image1,me.rect)
                else:
                    screen.blit(me.image2,me.rect)
            else:
                # if the enemies was shot down
                if not (delay%3):
                    screen.blit(me.destroy_images[plane2_destroy_index],me.rect)
                    #There are four images in total
                    #When a picture index value divisible by 4 is obtained, a new cycle will start
                    plane2_destroy_index=(plane2_destroy_index+1)%4
                    if plane2_destroy_index==0:
                        life_num=life_num-1
                        me.reset()
                        pygame.time.set_timer(invincible_time,3*1000)
            # setting for the left numbers of the bombs
            bomb_text=bomb_font.render(f'* {bomb_num}',True,black)
            text_rect=bomb_text.get_rect()
            screen.blit(bomb_image,(10,height-10-bomb_rect.height))
            screen.blit(bomb_text,(20+bomb_rect.width,height-5-text_rect.height))
            # setting for the left numbers of myplane's lives
            if life_num:
                for l in range(life_num):
                    screen.blit(life_image,(width-10-(l+1)*life_rect.width,\
                                            height-10-life_rect.height))
        # setting for the game ending
        elif life_num==0:
            # stop all the supplies
            pygame.time.set_timer(supply_time,0)

            if not recorded:
                recorded=True
                # getting the history record
                with open('record.txt','r') as f:
                    record_score=f.read()
                if int(score)>int(record_score):
                    with open('record.txt','w') as f:
                        f.write(str(score))
            # adding the ending of the game
            record_score_text=score_font.render(f'Best: {record_score}',True,red)
            screen.blit(record_score_text,(50,50))

            gameover_text1=gameover_font.render('Your Score',True,black)
            gameover_text1_rect=gameover_text1.get_rect()
            gameover_text1_rect.left,gameover_text1_rect.top=\
                (width-gameover_text1_rect.width)//2,height+50
            screen.blit(gameover_text1,gameover_text1_rect)

            gameover_text2=gameover_font.render(str(score),True,green)
            gameover_text2_rect=gameover_text2.get_rect()
            gameover_text2_rect.left,gameover_text2_rect.top=\
                (width-gameover_text2_rect.width)//2,gameover_text1_rect.bottom+10
            screen.blit(gameover_text2,gameover_text2_rect)

            #again_rect.left,again_rect.top=(width-again_rect.width)//2,gameover_text2_rect.bottom+50
            again_rect.left,again_rect.top=(width-again_rect.width)//2,gameover_text2_rect.bottom+50
            screen.blit(again_image,again_rect)

            gameover_rect.left,gameover_rect.top=(width-again_rect.width)//2,again_rect.bottom+10
            screen.blit(gameover_image,gameover_rect)
            # checking the options by the mouse
            # if the player chose the left-button of the mouse
            if pygame.mouse.get_pressed()[0]:
                # get the position of the mouse
                pos=pygame.mouse.get_pos()
                #if the player chose the restart the game
                if again_rect.left<pos[0]<again_rect.right and \
                    again_rect.top<pos[1]<again_rect.bottom:

                    # calling the function of 'main()' and restart the game
                    main()
                # if the player chose to end the game
                elif gameover_rect.left<pos[0]<gameover_rect.right and \
                    gameover_rect.top<pos[1]<gameover_rect.bottom:

                    # game ends
                    pygame.quit()
                    sys.exit()

        # add the score front
        score_text=score_font.render(f'Score: {str(score)} ',True,black)
        screen.blit(score_text,(10,5))
        # Drawing the pause button
        screen.blit(paused_image,paused_rect)
        # switching images
        if not (delay%5):
            switch_image=not switch_image
        delay=delay-1
        if not delay:
            delay=100

        pygame.display.flip()
        # if the game screen will update itself 60 times per min
        clock.tick(60)

if __name__=='__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
