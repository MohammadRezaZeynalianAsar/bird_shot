import pygame
import random
pygame.init()
#pygame.mixer.init()
screen = pygame.display.set_mode((820, 500))
running = True
clock = pygame.time.Clock()
bg=pygame.image.load('Pictur/bg.jpg')
class Bird:
    def __init__(self):
        self.images=pygame.image.load('Pictur/duck.png')
        self.r=10
        self.speed=1
       
        self.y=random.randint(0,250)
        self.direction =random.choice(['ltr','rtl'])
        if self.direction == "ltr":
            self.x = -50
        if self.direction == 'rtl':
            self.x = 870
        self.rect = self.images.get_rect()
        
    def show(self):
        #screen.blit(self.images,(self.x,self.y))
        if self.direction=="ltr":
            screen.blit(self.images,(self.x,self.y))
        if self.direction=="rtl": 
            screen.blit(pygame.transform.flip(self.images,True,False),(self.x,self.y)) 
    def fly(self):
        if self.direction=='ltr':
            self.x+=self.speed
        if self.direction=='rtl':
            self.x-=self.speed             
class Cloudy: 
    def __init__(self):
        self.images=pygame.image.load('Pictur/clouds.png')
        self.y = random.randint(0,200)
        self.direction =random.choice(['ltr','rtl'])
        self.speed=1
        if self.direction == "ltr":
            self.x = -50
        if self.direction == 'rtl':
            self.x = 870
    def show(self):
        if self.direction=="ltr":
           screen.blit(self.images,(self.x,self.y))
        if self.direction=="rtl": 
           screen.blit(pygame.transform.flip(self.images,True,False),(self.x,self.y))    
    def move(self)  :
        if self.direction=='ltr':
            self.x+=self.speed
        if self.direction=='rtl':
            self.x-=self.speed
class Gun:
    def __init__(self):
        self.x=800/2
        self.y=500/2
        self.image=pygame.image.load('Pictur/shooter.png')
        self.score=1
        self.shot=5
        #self.sound=pygame.mixer.Sound('Music/shotgun.wav')
        self.shot=5
        self.rect=self.image.get_rect()
    def show(self):
        screen.blit(self.image,(self.x,self.y))
    def kill(self,bird):
        if pygame.Rect.colliderect(self.rect,bird.rect):
            return True
gun=Gun()  
cloud = [Cloudy()]
birds = [Bird()]
          
while running:
    pygame.mouse.set_visible(False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            gun.x = pygame.mouse.get_pos()[0]
            gun.y = pygame.mouse.get_pos()[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            for bird in birds:
                if gun.kill(bird):
                    birds.remove(bird)
                    gun.score+=1
                    gun.shot-=1
                    break
    if random.random()>0.99:
        birds.append(Bird())
    if random.random()>0.99:
        cloud.append(Cloudy())   
    screen.blit(bg,(0,0))
    for bird in birds:
        bird.show()
        bird.fly()
    for cl in cloud:
        cl.show()
        cl.move()  
    clock.tick(50)
    gun.show()
    font=pygame.font.SysFont("comicsansms",25)
    txt_score=font.render("score:"+str(gun.score),True,[200,50,10])
    txt_shot=font.render("shot:"+str(gun.shot),True,[200,40,10])
    screen.blit(txt_score,[150,300])
    screen.blit(txt_shot,[100,100])
    if gun.shot==0:
        

    a=pygame.image.load("Pictur/GameOver.jpg")
    screen.blit(a,(0,0))
        
    pygame.display.update()
