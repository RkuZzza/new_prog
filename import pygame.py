from pygame import *

# Цвета
BLUE = (200,255,255)

# Создаем экран
width = 900
height = 700
win = display.set_mode((width, height))
win.fill(BLUE)
clock = time.Clock()


# Класс персонажей
class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_width, player_heigth, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_heigth))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
	# Метод перерисовки персонажа
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player_RIGHT(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < height - self.rect.height: # исправить высоту персонажа
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 

class Player_LEFT(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < height - self.rect.height: # исправить высоту персонажа
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 

ball = GameSprite("ball.png", (width/2-25), (height/2-25), 25, 25, 5)
platform_right = Player_RIGHT("platform.png", 5, 300, 20, 100, 5)
platform_left = Player_LEFT("platform.png", 875, 300, 20, 100, 5)


run = True
while run:
    win.fill(BLUE)
    ball.reset()
    platform_left.reset()
    platform_right.reset()
    
    for e in event.get():
        if e.type == QUIT:
            run = False

    platform_left.update()
    platform_right.update()


    display.update()
    clock.tick(40)