import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Balloon Flight")

# Load balloon image
balloon_image = pygame.image.load("balloon.png")  # Replace "balloon.png" with your image file
balloon_image = pygame.transform.scale(balloon_image, (100, 150))  # Scale the image as needed
balloon_rect = balloon_image.get_rect()
balloon_rect.center = (screen_width // 2, screen_height - 150)  # Initial position

# Set balloon speed
balloon_speed = 0.5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move balloon upwards
    balloon_rect.y -= balloon_speed

    # Reset balloon position if it goes off-screen
    if balloon_rect.bottom < 0:
        balloon_rect.top = screen_height
        balloon_rect.centerx = screen_width // 2

    # Clear the screen
    screen.fill((135, 206, 235))  # Light blue background

    # Draw the balloon
    screen.blit(balloon_image, balloon_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
