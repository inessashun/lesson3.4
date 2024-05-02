import pygame
import random

pygame.init()

SCREEN_WIDTH = 800  # screen size
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # set screen size

pygame.display.set_caption("Game Target")  # screen name
icon = pygame.image.load("img/avatar.jpg")  # screen image
pygame.display.set_icon(icon)  # set icon

target_img = pygame.image.load("img/heart.png")
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0  # initialize score

font = pygame.font.Font(None, 36)  # font for displaying score

target_speed = 5  # speed of target movement


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():  # check actions with cycle -> for
        if event.type == pygame.QUIT:  # save in event and end
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # event type key down
            mouse_x, mouse_y = pygame.mouse.get_pos()  # mouse click position
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:  # targeting point
                score += 1  # increment score
                target_x = random.randint(0, SCREEN_WIDTH - target_width)  # random target right_left side
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)  # random target up_down side
    screen.blit(target_img, (target_x, target_y))  # image on screen

    # Display score
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()  # refresh the screen

    # Move the target
    target_x += random.randint(-target_speed, target_speed)
    target_y += random.randint(-target_speed, target_speed)
    # Ensure the target stays within the screen boundaries
    target_x = max(0, min(target_x, SCREEN_WIDTH - target_width))
    target_y = max(0, min(target_y, SCREEN_HEIGHT - target_height))

pygame.quit()

