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


rct_l = Rockets('rc.png', 5, 0, 16, 106, 3)
rct_r = Rockets('rc.png', mw_w - 20, 0, 16, 106, 3)

game = True

while game:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if game:
        mw.fill((0,255,0))
        rct_l.rocket_l()
        rct_r.rocket_r()

    rct_l.reset()
    rct_r.reset()

    pygame.display.update()
    clock.tick(FPS)
