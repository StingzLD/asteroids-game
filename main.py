import pygame
from constants import *


def main():
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    pygame.init()
    clock = pygame.time.Clock
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if user clicked on window's close button
                return

        pygame.Surface.fill(screen, "black")

        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000


if __name__ == "__main__":
    main()
