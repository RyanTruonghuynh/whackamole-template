import pygame
import random



if __name__ == "__main__":
    try:
        pygame.init()
        print()
        # You can draw the mole with this snippet
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0


        while running:
            # Fills screen with green
            screen.fill("light green")
        # Drawing the Grid
            # vertical lines
            for x in range(0, 640, 32):
                pygame.draw.line(screen, "orange", (x, 0), (x, 512))
            # horizontal lines
            for y in range(0, 512, 32):
                pygame.draw.line(screen, "orange", (0, y), (640, y))
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))

            #Pygame Clicking
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    if mole_x < click_x < mole_x +32 and mole_y < click_y < mole_y +32:
                        # move mole to random location
                        mole_x = random.randrange(0, 20) * 32
                        mole_y = random.randrange(0, 16) * 32
            #clear screen
            screen.fill("light green")
            #vertical lines
            for x in range(0, 640, 32):
                pygame.draw.line(screen, "orange", (x, 0), (x, 512))
            # horizontal lines
            for y in range(0, 512, 32):
                pygame.draw.line(screen, "orange", (0, y), (640, y))

            #draws new mole
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))


            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()
