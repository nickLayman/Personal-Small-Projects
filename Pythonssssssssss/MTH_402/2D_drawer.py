import sys
import pygame
import cmath
import math
from pygame.locals import *

pixels_width = 512*2
pixels_height = 512
input_window_width = 2*math.pi
input_window_height = 2*math.pi
output_window_width = 2*math.pi
output_window_height = 2*math.pi


def f(z):
    return cmath.log(z)


def show(image):
    screen = pygame.display.get_surface()
    screen.blit(image, (0, 0))
    pygame.display.flip()
    while 1:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            raise SystemExit


def main():
    pygame.init()
    mouse = pygame.mouse
    window = pygame.display.set_mode((pixels_width, pixels_height))
    canvas = window.copy()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    canvas.fill(WHITE)

    # draw horizontal axis
    pygame.draw.line(canvas, BLACK, (0, pixels_height//2),
                     (pixels_width-1, pixels_height//2), 2)
    # draw first vertical axis
    pygame.draw.line(canvas, BLACK, (pixels_width//4, 0),
                     (pixels_width//4, pixels_height-1), 2)
    # draw second vertical axis
    pygame.draw.line(canvas, BLACK, (pixels_width * 3 // 4, 0),
                     (pixels_width * 3 // 4, pixels_height - 1), 2)
    # draw divider
    pygame.draw.line(canvas, RED, (pixels_width // 2, 0),
                     (pixels_width // 2, pixels_height - 1), 2)

    while True:
        left_pressed, middle_pressed, right_pressed = mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif left_pressed:
                mousex = pygame.mouse.get_pos()[0]
                mousey = pygame.mouse.get_pos()[1]
                xc = mousex*input_window_width/(pixels_width / 2) - input_window_width/2
                yc = input_window_height/2 - mousey*input_window_height/pixels_height
                fxyc = f(xc + yc*1j)
                fxc = fxyc.real
                fyc = fxyc.imag
                fxp = int(pixels_width*3/4 + fxc*pixels_width/(input_window_width + output_window_width))
                fyp = int(pixels_height/2 - fyc*pixels_height/output_window_height)
                pygame.draw.circle(canvas, BLACK, (mousex, mousey), 2)
                pygame.draw.circle(canvas, BLACK, (fxp, fyp), 2)
        # window.fill(WHITE)
        window.blit(canvas, (0, 0))
        pygame.draw.circle(window, BLACK, (pygame.mouse.get_pos()), 2)
        pygame.display.update()


if __name__ == '__main__':
    main()
