from pygame import *

class Sprite_game(sprite.Sprite):
    def __init__(self, player_image, x, y, speed1, speed2):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed1 = speed1
        self.speed2 = speed2
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player1(Sprite_game):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed1
        if keys[K_s] and self.rect.y < 445:
            self.rect.y += self.speed1

class Player2(Sprite_game):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed1
        if keys[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.speed1
            



win = display.set_mode((700, 500))
display.set_caption("Ping-pong")
cvet = transform.scale(image.load("back.jpg"), (700, 500))

player1 = Player1('hero.png', 30, 225, 2, 2) 
player2 = Player2('cyborg.png', 620, 225, 2, 2)
ball = Sprite_game('ball.png', 325, 225, 2, 2)


run = True
pobeda = False
clock = time.Clock()
FPS = 60

font.init()
font = font.SysFont('Arial', 70)
viigrish = font.render('Победил игрок 1!', True, (0, 0, 200))
proigrish = font.render('Победил игрок 2!', True, (0, 0, 200))

mixer.init()


dengi = mixer.Sound('money.ogg')
udar = mixer.Sound('kick.ogg')

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if pobeda != True:
        win.blit(cvet, (0, 0))
        player1.update()
        player2.update()
        player1.reset()
        player2.reset()
        ball.reset()
        ball.rect.x += ball.speed1
        ball.rect.y += ball.speed2

        if ball.rect.y >= 450:
            ball.speed2 *= -1
        if ball.rect.y <= 0:
            ball.speed2 *= -1
        

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball.speed1 *= -1
            udar.play()
        if ball.rect.x >= 650:
            pobeda = True
            win.blit(viigrish, (80, 200))
            dengi.play()
        if ball.rect.x <= 0:
            pobeda = True
            win.blit(proigrish, (80, 200))
            dengi.play()

    display.update()
    clock.tick(FPS)