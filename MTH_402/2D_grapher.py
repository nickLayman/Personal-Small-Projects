import cmath
import math
import numpy
import pygame

window_width = 2.5
window_height = 2.5
pixels_width = 512
pixels_height = 512
row_width = 1
col_width = 1
show_axes = False


def f(z):
    if abs(z) > 1:
        return 0
    return z


def show(image):
    screen = pygame.display.get_surface()
    screen.blit(image, (0, 0))
    pygame.display.flip()
    while 1:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            raise SystemExit


def getAngle(x, y):
    pi = math.pi
    angle: float
    hypotenuse = getDistance(x, y)

    if y == 0 and x >= 0:
        angle = 0
    elif y == 0 and x < 0:
        angle = pi
    elif x > 0:
        angle = math.asin(y / hypotenuse)
    elif y > 0:
        angle = pi - math.asin(y / hypotenuse)
    else:
        angle = -pi - math.asin(y / hypotenuse)

    return angle


def getPureColor(x, y):
    # x and y in terms of the xy-plane, not the array
    pi = math.pi
    tr, tg, tb = 0, 0, 0
    angle = getAngle(x, y)

    # -pi/3 to pi/3
    # the right third
    if -pi / 3 <= angle <= pi / 3:
        tr = 255
        if angle > 0:
            tg = 255*angle/(pi / 3)
        else:
            tb = 255 * -angle / (pi / 3)

    # pi/3 to pi
    # top left third
    if angle > math.pi/3:
        if angle < 2*pi / 3:
            tr = 255 - 255*(angle - pi/3) / (pi/3)
        tg = 255
        if angle > 2*pi / 3:
            tb = 255*(angle - 2*pi/3) / (pi/3)

    # -pi/3 to -pi
    # bottom left third
    if angle < -pi/3:
        if angle > -2*pi / 3:
            tr = 255*(angle + 2*pi/3) / (pi/3)
        if angle < -2*pi / 3:
            tg = 255 - 255*(angle + pi) / (pi/3)
        tb = 255

    return tr, tg, tb


def getDistance(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


def getColorMultiplier(x, y) -> float:
    distance = getDistance(x, y)
    maxDist = getDistance(window_width, window_height)
    # higher -> smaller spot around zeroes
    mult = 20
    return (mult*distance / maxDist) / (1 + (mult*distance / maxDist))


def getColor(x, y):
    pure_color_r = getPureColor(x, y)[0]
    pure_color_g = getPureColor(x, y)[1]
    pure_color_b = getPureColor(x, y)[2]

    multiplier = getColorMultiplier(x, y)

    color_r = pure_color_r * multiplier
    color_g = pure_color_g * multiplier
    color_b = pure_color_b * multiplier

    return int(color_r), int(color_g), int(color_b)


def main():
    pygame.init()

    pygame.display.set_mode((pixels_width, pixels_height))
    surface = pygame.Surface((pixels_width, pixels_height))

    pygame.display.flip()

    # Create the PixelArray.
    ar = pygame.PixelArray(surface)

    # graph some complex function
    xcoords = numpy.arange(-window_width/2, window_width/2,
                           window_width/pixels_width)
    ycoords = numpy.arange(-window_height/2, window_height/2,
                           window_height/pixels_height)
    for x in range(0, pixels_width, col_width):
        for y in range(0, pixels_height, row_width):
            xc = xcoords[x]
            yc = ycoords[y]
            z = xc + yc*1j
            if not getDistance(xc, yc) == 0:
                coords = [f(z).real, f(z).imag]
                fx = coords[0]
                fy = coords[1]
            else:
                fx = 0
                fy = 0
            r, g, b = getColor(fx, fy)
            for num1 in range(col_width):
                for num2 in range(row_width):
                    if x+num1 < pixels_width and y+num2+1 < pixels_height:
                        ar[x+num1, pixels_height-1-(y+num2)] = (r, g, b)

    # draw axes
    if show_axes:
        for x in range(pixels_width):
            ar[x, pixels_height//2] = (0, 0, 0)
            ar[x, pixels_height // 2 + 1] = (0, 0, 0)
        for y in range(pixels_height):
            ar[pixels_width//2, y] = (0, 0, 0)
            ar[pixels_width // 2 + 1, y] = (0, 0, 0)
    del ar
    show(surface)


if __name__ == '__main__':
    main()
