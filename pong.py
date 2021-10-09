from pygame import *



mw_width = 500
mw_hieght = 500

mw = display.set_mode((mw_width, mw_hieght))
mw.fill((0,255,0))

clock = time.Clock()
FPS = 60


class Sprite():
    def __init__(self, image_name, cor_x, cor_y, width, hieght, speed = 0):
        self.image = transform.scale(image.load(image_name), (width, hieght))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = cor_x
        self.rect.y = cor_y
    
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

    def collide(self, obj):
        self.rect.colliderect(obj)
    
class Rocket(Sprite):
    def rocket_l(self):
        key_ = key.get_pressed()
        if key_[K_w]:
            self.rect.y -= self.speed
        if key_[K_s]:
            self.rect.y += self.speed

    def rocket_r(self):
        key_ = key.get_pressed()
        if key_[K_UP]:
            self.rect.y -= self.speed
        if key_[K_DOWN]:
            self.rect.y += self.speed

class Ball(Sprite):
    def __init__(self, image_name, cor_x, cor_y, width, hieght, speed_x, speed_y):
        super().__init__(self, image_name, cor_x, cor_y, width, hieght)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y



a = Rocket('rc.png', 5,0, 16, 100, 4)
b = Rocket('rc.png', 475,0, 16, 100, 4)
ball = Ball('ball.png', 250, 250, 26,26, 3, 3)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if game:
        mw.fill((0,255,0))
        a.rocket_l()
        b.rocket_r()
        ball.move()
    
    if ball.collide(a):
        ball.speed_x *= -1

    a.draw()
    b.draw()
    ball.draw()

    display.update()
    clock.tick(FPS)
