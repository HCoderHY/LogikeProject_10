# Ping - Pong
from pygame import *
from time import sleep

init()

back= (200, 255, 255)
red = (255, 0, 0)
green = (0, 255, 51)
blue = (0, 0, 255)
orange = (255, 123, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
light_green = (200, 255, 200)
light_red = (250, 128, 114)
black = (0, 0, 0)
dark_blue = (0, 0, 100)
light_blue = (80, 80, 255)
color_client = (0, 0, 100)
start_x = 5
start_y = 5
platform_x = 200
plaform_y = 400
plaform2_y = 100
count = 9
dx = 4
dy = 4
game = True

monster = []
display.set_caption("Ping-Pong")
window = display.set_mode((500, 500))
clock = time.Clock()
class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    def set_text(self, text, fsize=12, text_color=black):
        self.text = text
        self.image = font.Font(None, fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=light_blue):
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    
    def color(self, new_color):
        self.fill_color = new_color
    
    def fill(self):
        draw.rect(window, self.fill_color, self.rect)
    
    def outline(self, frame_color, thickness):
        draw.rect(window, frame_color, self.rect, thickness)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width = 100, height = 100, color = (0, 0, 0)):
        super().__init__(x, y, width, height, color)
        self.image = image.load(filename)
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 4
        elif keys[K_RIGHT]:
            self.rect.x += 4
        elif self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 400:
            self.rect.x = 380
    def move2(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= 4
        elif keys[K_d]:
            self.rect.x += 4
        elif self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 400:
            self.rect.x = 380

platform = Picture('platform.png', platform_x, plaform_y, 100, 30, (0, 0, 0))
platform2 = Picture('platform2.png', platform_x, plaform2_y, 100, 30, (0, 0, 0))
ball = Picture('ball.png', 225, 300, 100, 30, (0, 0, 0))  
louse_text = TextArea(120, 200, 0, 0, (255, 255, 255))
louse_text.set_text('Louse PLayer 1', 50, (255, 0, 0))
louse_text2 = TextArea(120, 200, 0, 0, (255, 255, 255))
louse_text2.set_text('Louse PLayer 2', 50, (255, 0, 0))

while game == True:
    window.fill(back) 
    for e in event.get():
        if e.type == QUIT:
            game = False
    platform.draw()
    platform2.draw()  
    platform.move() 
    platform2.move2()
    ball.draw()
    ball.rect.x += dx
    ball.rect.y += dy
    if  ball.rect.y < 0:
        dy *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        dx *= -1
    if ball.rect.colliderect(platform.rect):
        dy *= -1
    if ball.rect.colliderect(platform2.rect):
        dy *= -1
    if ball.rect.y >= 450:
        louse_text.draw(15, 12)
        game = False
    elif ball.rect.y <= 50:
        louse_text2.draw(15, 12)
        game = False

    display.update()
    clock.tick(60)
