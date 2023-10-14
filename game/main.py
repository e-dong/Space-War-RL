"""Contains the main entrypoint logic"""

import pygame

from game import module_path
from game.conf import MAX_FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player


def main():
    """Entrypoint for starting up the pygame"""
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock = pygame.time.Clock()
    delta_time = clock.tick(MAX_FPS) / 1000

    # Groups
    player_single_group = pygame.sprite.GroupSingle()
    player_single_group.add(
        Player(
            delta_time=delta_time,
            image_path=module_path() / "assets" / "player_1.png",
            start_pos=(screen.get_width() / 2, screen.get_height() / 2),
        )
    )

    running = True

    while running:
        # event loop
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        player_single_group.draw(screen)
        player_single_group.update()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()