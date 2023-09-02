from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Моя перша гра")
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
LAZUR = (0,255,255)
class Card(sprite.Sprite):
    def __init__(self,width,height,x,y,color): 
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    def draw(self):
        draw.rect(window, self.fill_color, self.rect)

class Pic(sprite.Sprite):
    def __init__(self,picture,w,h,x,y): 
        super().__init__()
        self.image=transform.scale(image.load(picture),(w, h))
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

player1 = Card(100,100,100,200,LAZUR)
player2 = Pic('dog.png',100,200,500,150)

run = True
while run:
    time.delay(50)
    window.blit(background,(0,0))
    player1.draw()
    player2.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()