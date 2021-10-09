import pygame
pygame.init()

mw_w = 500
mw_h = 500

mw = pygame.display.set_mode((mw_w, mw_h))
mw.fill((0,255,0))
clock = pygame.time.Clock()
FPS = 60

class Sprite:
    def __init__(self, image_name, x, y, width, hight, speed):
        self.image = pygame.transform.scale(
            pygame.image.load(image_name), (width, hight))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Rockets(Sprite):
    def rocket_l(self):
        key_ = pygame.key.get_pressed()
        if key_[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_[pygame.K_s] and self.rect.y < mw_h - 106:
            self.rect.y += self.speed

    def rocket_r(self):
        key_ = pygame.key.get_pressed()
        if key_[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_[pygame.K_DOWN] and self.rect.y < mw_h - 106:
            self.rect.y += self.speed

class Ball(Sprite):

    def inst_speed(self):
        self.Speed_x = self.speed
        self.Speed_y = self.speed

    def move(self):
        self.rect.x += self.Speed_x
        self.rect.y += self.Speed_y
        if self.rect.x > mw_w - 26 or self.rect.x < 0:
            self.Speed_x *= -1 
        if self.rect.y > mw_h - 26 or self.rect.y < 0:
            self.Speed_y *= -1 


rct_l = Rockets('rc.png', 5, 0, 16, 106, 3)
rct_r = Rockets('rc.png', mw_w - 20, 0, 16, 106, 3)
ball = Ball('ball.png', 10, 50, 26, 26, 4)

game = True
ball.inst_speed()
while game:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if game:
        mw.fill((0,255,0))
        rct_l.rocket_l()
        rct_r.rocket_r()
        ball.move()

    rct_l.reset()
    rct_r.reset()
    ball.reset()

    pygame.display.update()
    clock.tick(FPS)
