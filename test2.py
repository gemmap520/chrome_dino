import pygame
import random
pygame.init()

screen_height = 600
screen_width = 1100
screen = pygame.display.set_mode((screen_width, screen_height))

BG = pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Other/Track.png")

############ 2 ###########
RUNNING = [
    # pygame.transform.scale(pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Dino/DinoRun1.png"), (80,80)),
    pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Dino/DinoRun1.png"), 
    pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Dino/DinoRun2.png")
]
JUMPING = pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Dino/DinoJump.png")
DUCKING = [pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Dino/DinoDuck1.png"),
           pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Dino/DinoDuck2.png")]
######################


############ 3 ###########
SMALL_CACTUS = [pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Cactus/SmallCactus1.png"),
                pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Cactus/SmallCactus2.png")]
LARGE_CACTUS = [pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Cactus/LargeCactus1.png"),
                pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Cactus/LargeCactus2.png")]
BIRD = [pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Bird/Bird1.png"),
        pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Bird/Bird2.png")]
##########################


############ 2 ###########
class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
######################


############ 3 ###########
class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_width

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, len(image) - 1)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, len(image) - 1)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1
#################################

def main():
    global game_speed, x_pos_bg, y_pos_bg, obstacles, points
           ############# 1 ############# #### 3 #### ## 4 ##
    run = True
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380

    ########### 4 ###############
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    #############################

    ########## 5 #############
    clock = pygame.time.Clock()
    death_count = 0
    ##########################

    ############# 2 ############
    player = Dinosaur()
    ############################
    
    ############# 3 ##############
    obstacles = []
    ##############################

    ############ 4 ###############
    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        screen.blit(text, textRect)
    #############################

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        screen.blit(BG, (x_pos_bg, y_pos_bg))
        screen.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            screen.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.fill((255,255,255))

        ############ 2 ###########
        userInput = pygame.key.get_pressed()
        player.draw(screen)
        player.update(userInput)
        #######################


        ############ 3 ###########
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()
            ############## 4 #############################
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)
            ###############################################
        ##########################

        background()

        ########## 4 ############
        score()
        #########################

        ######### 5 ###########
        clock.tick(30)
        ######################
        pygame.display.update()
    
################ 5 remove ############
    pygame.quit()
main()
######################################

################# 5 ##################
def menu(death_count):
    global points
    run = True
    while run:
        screen.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (screen_width // 2, screen_height // 2 + 50)
            screen.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (screen_width // 2, screen_height // 2)
        screen.blit(text, textRect)
        screen.blit(RUNNING[0], (screen_width // 2 - 20, screen_height // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)
#################################