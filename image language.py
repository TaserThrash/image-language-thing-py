import pygame
pygame.init()
from math import *
from random import *

code = ""


width = 500
height = 500

run = True

while run:
    print("""insert the code z is the brightness overflow at 256
type "stop" to stop""")
    pcode = code
    code = ""
    while True:
      c = input("");
      if c == "stop":
        if code != "":
            break
        else:
            run = False
      code += c + "\n"

    win = pygame.display.set_mode((width,height));

    for x in range(width):
        for y in range(height):
            try:
                exec(code)
                z = abs(z)
                pygame.draw.rect(win, (z % 255, z % 255, z % 255), (x, y, 1, 1));
            except:
                pass
        #pygame.display.update()
    pygame.display.update()

code = pcode
sx = 0
sy = 0
zoom = 1
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    zoom = int(input("zoom"))
    for x in range(width):
        for y in range(height):
            try:
                exec(code)
                z = abs(z)
                pygame.draw.rect(win, (z % 255, z % 255, z % 255), (sx + x / zoom, sy + y / zoom, 1, 1));
            except:
                pass
