import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Display Image")

# Set background color (white)
white = (255, 255, 255)

# Load an image (make sure 'my_image.png' exists in the same folder)
image = pygame.image.load("download")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(white)

 # Draw the image at a desired position (e.g., top-left)
    screen.blit(image, (100, 100))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()