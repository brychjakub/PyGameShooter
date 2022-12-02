import pygame, random, math

#Use 2D vectors
vector = pygame.math.Vector2

#Initialize pygame
pygame.init()

FPS = 60
clock = pygame.time.Clock()

#Set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

OBJECT_WIDTH = 80
OBJECT_HEIGHT = 80
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("fly and shoot")

velocity = 5        #toto asi k ničemu není, je to v pplayerovi ve vektorech
angle = 0

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load("space.png"),(WINDOW_WIDTH, WINDOW_HEIGHT))
BACKGROUND_IMAGE_RECT = BACKGROUND_IMAGE.get_rect()

green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

PLANET_HIT = pygame.USEREVENT + 3

i = [0,0]     #spojujee pohyb šipek se směrem střelby
j = 0       #určuje barvu strely


class Player1(pygame.sprite.Sprite):
    def __init__(self, velocity, bullet_group):
        super().__init__()
        self.image = pygame.image.load("player1/spaceship_left.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0,WINDOW_WIDTH//2)
        x = self.rect.centerx
        self.rect.bottom = WINDOW_HEIGHT//2
        y = self.rect.bottom
        self.rect.topleft = (x, y)
        self.velocity = velocity
        self.angle = angle
        self.bullet_group = bullet_group
        
        
        
        
        #Kinematics vectors (first value is the x, second value is the y)
        self.position = vector(x, y)
        self.velocity = vector(0, 0)        #0 aby ze začátku nikam nezrychloval
        self.acceleration = vector(0, 0)

        #Kinematic constants
        self.HORIZONTAL_ACCELERATION = 2       #toto je zrychlení při rozjezdu
        self.HORIZONTAL_FRICTION = 0.15     #takto rychle brzdí rozjetej
        

    def update(self):
        self.move()
        self.rotate()
        self.collisions()
     
       
         



    def rad_to_offset(radians, offset): # insert better func name. Nevim co s tim ale třeba na otáčení by to mohlo být lepší
        pass
     #   x = cos(radians) * offset
      #  y = sin(radians) * offset
       # return [x, y]
    # from https://web.archive.org/web/20121126060528/http://eli.thegreenplace.net/2008/12/13/writing-a-game-in-python-with-pygame-part-i/


    def move(self):  
        #Set the accleration vector to (0, 0) so there is initially no acceleration
        #If there is no force (no key presses) acting on the player then accerlation should be 0
        #Vertical accelration (gravity) is present always regardless of key-presses
        self.acceleration = vector(0, 0)     
        
        #If the user is presseing a key, set the x-component of the accleration vector to a non zero value.
        keys = pygame.key.get_pressed()
          #0 = left, 1 = right, 2 = down, 3 = up
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -1*self.HORIZONTAL_ACCELERATION
            self.image = pygame.image.load("player1/spaceship_left.png")
            i[0] = 0
           
          
        if keys[pygame.K_RIGHT]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            self.image = pygame.image.load("player1/spaceship_right.png")
            i[0] = 1

        if keys[pygame.K_UP]:
            self.acceleration.y = -1*self.HORIZONTAL_ACCELERATION
            self.image = pygame.image.load("player1/spaceship_up.png")
            i[0] = 2

        if keys[pygame.K_DOWN]:
            self.acceleration.y = self.HORIZONTAL_ACCELERATION
            self.image = pygame.image.load("player1/spaceship.png")
            i[0] = 3
           
                  

        
         #Calculate new kinematics values (2, 5) + (1, 6) = (3, 11)
        self.acceleration.x -= self.velocity.x*self.HORIZONTAL_FRICTION
        self.acceleration.y -= self.velocity.y*self.HORIZONTAL_FRICTION

        self.velocity += self.acceleration
        self.position += self.velocity + 0.5*self.acceleration

         #Update new rect based on kinematic calculations
        self.rect.center = self.position

        if self.position.x < 0:
            self.position.x = WINDOW_WIDTH
        elif self.position.x > WINDOW_WIDTH:
            self.position.x = 0
        elif self.position.y < 0:
            self.position.y = WINDOW_HEIGHT
        
        elif self.position.y > WINDOW_HEIGHT:
            self.position.y = 0

 
    def rotate(self):       #nevim co s tim
        pass
        """ keys = pygame.key.get_pressed()
        
        if keys[K_q]:
                self.angle += 6            
                mx, my = self.rect.centerx, self.rect.centery
                img_copy = pygame.transform.rotate(self.image, self.angle)
                display_surface.blit(img_copy, (mx - int(img_copy.get_width() / 2), my - int(img_copy.get_height() / 2)))
                
        if keys[K_e]:
                self.angle -= 6            
                mx, my = self.rect.centerx, self.rect.centery
                img_copy = pygame.transform.rotate(self.image, self.angle)
                display_surface.blit(img_copy, (mx - int(img_copy.get_width() / 2), my - int(img_copy.get_height() / 2)))
 """
        
    def shooting(self):
      
            #self.shoot_sound.play()      #zatím bez omezení počtu střel
            PlayerBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)
    
     
        
                  
    def collisions(self):
        pass
        """ collide_planet = pygame.sprite.spritecollide(self, planet_group, False)
        if collide_planet:
            self.position.y = collide_planet[0].rect.top + 1
            self.velocity.y = 0 """

           #Check for collisions with the water tiles
        if pygame.sprite.spritecollide(self, planet_group, False):
            self.velocity.x = 0
            self.velocity.y = 0
             
class Player2(pygame.sprite.Sprite):
    def __init__(self, velocity, bullet_group):
        super().__init__()
        self.image = pygame.image.load("player2/spaceship_left.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(WINDOW_WIDTH//2, WINDOW_WIDTH-OBJECT_WIDTH)
        x = self.rect.centerx
        self.rect.bottom = WINDOW_HEIGHT//2
        y = self.rect.bottom
        self.rect.topleft = (x, y)
        self.velocity = velocity
        self.angle = angle
        self.bullet_group = bullet_group
        
        #Kinematics vectors (first value is the x, second value is the y)
        self.position = vector(x, y)
        self.velocity = vector(0, 0)        #0 aby ze začátku nikam nezrychloval
        self.acceleration = vector(0, 0)

        #Kinematic constants
        self.HORIZONTAL_ACCELERATION = 2       #toto je zrychlení při rozjezdu
        self.HORIZONTAL_FRICTION = 0.15     #takto rychle brzdí rozjetej
        

    def update(self):
        self.move()
        self.collisions()
     
       
    def move(self):  
        self.acceleration = vector(0, 0)     
        
        keys = pygame.key.get_pressed()
          #0 = left, 1 = right, 2 = down, 3 = up
        if keys[pygame.K_a]:
            self.acceleration.x = -1*self.HORIZONTAL_ACCELERATION
            self.image = pygame.image.load("player2/spaceship_left.png")
            i[1] = 0
                 
        if keys[pygame.K_d]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            self.image = pygame.image.load("player2/spaceship_right.png")
            i[1] = 1

        if keys[pygame.K_w]:
            self.acceleration.y = -1*self.HORIZONTAL_ACCELERATION
            self.image = pygame.image.load("player2/spaceship_up.png")
            i[1] = 2

        if keys[pygame.K_s]:
            self.acceleration.y = self.HORIZONTAL_ACCELERATION
            self.image = pygame.image.load("player2/spaceship.png")
            i[1] = 3
           
         #Calculate new kinematics values (2, 5) + (1, 6) = (3, 11)
        self.acceleration.x -= self.velocity.x*self.HORIZONTAL_FRICTION
        self.acceleration.y -= self.velocity.y*self.HORIZONTAL_FRICTION

        self.velocity += self.acceleration
        self.position += self.velocity + 0.5*self.acceleration

        #Update new rect based on kinematic calculations
        self.rect.center = self.position

        if self.position.x < 0:
            self.position.x = WINDOW_WIDTH
        elif self.position.x > WINDOW_WIDTH:
            self.position.x = 0
        elif self.position.y < 0:
            self.position.y = WINDOW_HEIGHT
        elif self.position.y > WINDOW_HEIGHT:
            self.position.y = 0


    def shooting(self):
      
            #self.shoot_sound.play()      #zatím bez omezení počtu střel
            Player2Bullet(self.rect.centerx, self.rect.bottom, self.bullet_group)
    
     
    def collisions(self):
        pass
        """ collide_planet = pygame.sprite.spritecollide(self, planet_group, False)
        if collide_planet:
            self.position.y = collide_planet[0].rect.top + 1
            self.velocity.y = 0 """
      
           #Check for collisions with the water tiles
        if pygame.sprite.spritecollide(self, planet_group, False):
            self.velocity.x = 0
            self.velocity.y = 0

        if pygame.sprite.spritecollide(self, my_player_bullet_group, True):
                pass


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        self.image = pygame.image.load("player1/green_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.i = i
        self.velocity = 100
        bullet_group.add(self)

    def update(self):
        """Update the bullet"""
        #0 = left, 1 = right, 2 = down, 3 = up
        if self.i[0] == 0:   
            self.rect.x -= self.velocity
        if self.i[0] == 1:
            self.rect.x += self.velocity
        if self.i[0] == 2:
            self.rect.y -= self.velocity
        if self.i[0] == 3:
            self.rect.y += self.velocity


        #If the bullet is off the screen, kill it
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.kill()
        if self.rect.bottom <= 0:
            self.kill()
        if self.rect.centerx <= 0:
            self.kill()
        if self.rect.centerx >= WINDOW_WIDTH:
            self.kill()
    
        if pygame.sprite.spritecollide(self, player_group, True):
             explosion = Explosion(self.rect.centerx,self.rect.centery)
             explosion_group.add(explosion)   

class Player2Bullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the player"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        self.image = pygame.image.load("player2/red_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.i = i
        self.velocity = 100
        bullet_group.add(self)

    def update(self):
        """Update the bullet"""
        #0 = left, 1 = right, 2 = down, 3 = up
        if self.i[1] == 0:  
            self.rect.x -= self.velocity
        if self.i[1] == 1:
            self.rect.x += self.velocity
        if self.i[1] == 2:
            self.rect.y -= self.velocity
        if self.i[1] == 3:
            self.rect.y += self.velocity


        #If the bullet is off the screen, kill it
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.kill()
        if self.rect.bottom <= 0:
            self.kill()
        if self.rect.centerx <= 0:
            self.kill()
        if self.rect.centerx >= WINDOW_WIDTH:
            self.kill()

        if pygame.sprite.spritecollide(self, player_group, True):
             explosion = Explosion(self.rect.centerx,self.rect.centery)
             explosion_group.add(explosion)

             

class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"exp/exp{num}.png")
			img = pygame.transform.scale(img, (100, 100))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0

	def update(self):
        
		explosion_speed = 4
		#update explosion animation
		self.counter += 1

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#if the animation is complete, reset animation index
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()

  

class Planet(pygame.sprite.Sprite):
    def __init__(self, rnd_width_from, rnd_width_to, rnd_height_from, rnd_height_to):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("planet.png"),(OBJECT_WIDTH, OBJECT_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(rnd_width_from,rnd_width_to-OBJECT_WIDTH), random.randint(rnd_height_from,rnd_height_to-OBJECT_HEIGHT))
    
         
    def update(self):
        if pygame.sprite.spritecollide(self, my_player_bullet_group, True):
           explosion = Explosion(self.rect.centerx,self.rect.centery)
           explosion_group.add(explosion)


   

my_player_bullet_group = pygame.sprite.Group()

   
player_group = pygame.sprite.Group() 
player1 = Player1(velocity, my_player_bullet_group)
player2 = Player2(velocity, my_player_bullet_group)
player_group.add(player1, player2)


planet_group = pygame.sprite.Group()
planet1 = Planet(0+OBJECT_WIDTH,WINDOW_WIDTH//2,0+OBJECT_HEIGHT,WINDOW_HEIGHT//2)
planet2 = Planet(WINDOW_WIDTH//2+OBJECT_WIDTH,WINDOW_WIDTH-OBJECT_WIDTH,0+OBJECT_HEIGHT, WINDOW_HEIGHT//2)
planet3 = Planet(0+OBJECT_WIDTH,WINDOW_WIDTH//2-OBJECT_HEIGHT,WINDOW_HEIGHT//2+OBJECT_HEIGHT, WINDOW_HEIGHT-OBJECT_HEIGHT)
planet4 = Planet(WINDOW_WIDTH//2+OBJECT_WIDTH,WINDOW_WIDTH-OBJECT_WIDTH,WINDOW_HEIGHT//2+OBJECT_HEIGHT,WINDOW_HEIGHT-OBJECT_HEIGHT)
planet_group.add(planet1, planet2, planet3, planet4)

explosion_group = pygame.sprite.Group()



running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    j = 1
                    player1.shooting()
            if event.key == pygame.K_LCTRL:
                    j = 2
                    player2.shooting()
    

    
    display_surface.blit(BACKGROUND_IMAGE, BACKGROUND_IMAGE_RECT)

    
    
    my_player_bullet_group.update()
    my_player_bullet_group.draw(display_surface)

   
    player_group.update()
    player_group.draw(display_surface)

    planet_group.update()
    planet_group.draw(display_surface)

    explosion_group.draw(display_surface)
    explosion_group.update()

    
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()