import pygame
import random
pygame.init()
screen_height = 600
screen_width = 1100
screen = pygame.display.set_mode((screen_width, screen_height))
BG = pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Other/Track.png")
running = [pygame.transform.scale(pygame.image.load("Assets/Dino/DinoRun1.png"), (87,94)), pygame.image.load("Assets/Dino/DinoRun1.png")]
jumping = pygame.image.load("/Users/gemma.p/Desktop/py_tutor/chrome-dinosaur/Assets/Dino/DinoRun1.png")
class dinosaur:
    x_pos = 80
    y_pos = 290
    jump_Vel = 8.5
    def __init__(self):
        self.run_img = running
        self.jump_img = jumping
        self.dino_run = True
        self.dino_jump = False
        self.step_index = 0
        self.jump_vel = self.jump_Vel
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
    def update(self, userInput):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_jump = False
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1 
    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.jump_Vel:
            self.dino_jump = False
            self.jump_vel = self.jump_Vel

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
def main():
    global game_speed, x_pos_bg, y_pos_bg
    run = True
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    player = dinosaur()
    def background():
        global x_pos_bg, y_pos_bg
        image_width  = BG.get_width()
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
        userInput = pygame.key.get_pressed()
        player.draw(screen)
        player.update(userInput)
        background()
        pygame.display.update()
    pygame.quit()
main()