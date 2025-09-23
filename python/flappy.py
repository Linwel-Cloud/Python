import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Game variables
FPS = 60
GRAVITY = 0.5
BIRD_JUMP_STRENGTH = -10
PIPE_SPEED = 4
PIPE_SPAWN_RATE = 1.5  # In seconds

# Bird properties
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_radius = 15
bird_velocity_y = 0

# Pipe properties
pipe_width = 70
pipe_gap = 150
pipes = []
score = 0
game_over = False
last_pipe_spawn_time = pygame.time.get_ticks()

# Fonts
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 30)

def draw_bird():
    """Draws the bird on the screen."""
    pygame.draw.circle(SCREEN, BLUE, (int(bird_x), int(bird_y)), bird_radius)

def draw_pipes():
    """Draws all the pipes on the screen."""
    for pipe in pipes:
        pygame.draw.rect(SCREEN, GREEN, pipe[0])
        pygame.draw.rect(SCREEN, GREEN, pipe[1])

def move_bird():
    """Updates the bird's position and velocity based on gravity."""
    global bird_y, bird_velocity_y
    bird_velocity_y += GRAVITY
    bird_y += bird_velocity_y

def jump_bird():
    """Makes the bird jump by setting its velocity to a negative value."""
    global bird_velocity_y
    bird_velocity_y = BIRD_JUMP_STRENGTH

def move_pipes():
    """Moves pipes to the left and removes them when they go off-screen."""
    for pipe in pipes:
        pipe[0].x -= PIPE_SPEED
        pipe[1].x -= PIPE_SPEED
    
    # Remove pipes that are off-screen
    if pipes and pipes[0][0].right < 0:
        pipes.pop(0)

def spawn_pipes():
    """Generates a new set of pipes."""
    global last_pipe_spawn_time
    current_time = pygame.time.get_ticks()
    if current_time - last_pipe_spawn_time > PIPE_SPAWN_RATE * 1000:
        last_pipe_spawn_time = current_time
        
        pipe_height = random.randint(50, SCREEN_HEIGHT - 50 - pipe_gap)
        top_pipe = pygame.Rect(SCREEN_WIDTH, 0, pipe_width, pipe_height)
        bottom_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT)
        pipes.append((top_pipe, bottom_pipe))

def check_collisions():
    """Checks for collisions with pipes or the ground/ceiling."""
    global game_over
    bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius * 2, bird_radius * 2)

    # Check for collisions with pipes
    for pipe in pipes:
        if bird_rect.colliderect(pipe[0]) or bird_rect.colliderect(pipe[1]):
            game_over = True
            return

    # Check for collisions with top and bottom of the screen
    if bird_y > SCREEN_HEIGHT or bird_y < 0:
        game_over = True

def update_score():
    """Increments the score if the bird passes a pipe."""
    global score
    for pipe in pipes:
        # Check if the bird's x position has passed the pipe's center and the score hasn't been incremented for this pipe yet
        if pipe[0].right < bird_x - bird_radius and pipe not in [p[0] for p in scored_pipes]:
            score += 1
            scored_pipes.append(pipe[0])

def draw_text(text, font, color, x, y):
    """Draws text on the screen."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    SCREEN.blit(text_surface, text_rect)

def reset_game():
    """Resets all game variables to their initial state."""
    global bird_y, bird_velocity_y, pipes, score, game_over, last_pipe_spawn_time, scored_pipes
    bird_y = SCREEN_HEIGHT // 2
    bird_velocity_y = 0
    pipes = []
    score = 0
    game_over = False
    last_pipe_spawn_time = pygame.time.get_ticks()
    scored_pipes = []

# Main game loop
running = True
clock = pygame.time.Clock()
scored_pipes = [] # Keeps track of pipes that have been passed for scoring

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                jump_bird()
            if event.key == pygame.K_SPACE and game_over:
                reset_game()

    if not game_over:
        move_bird()
        spawn_pipes()
        move_pipes()
        check_collisions()
        update_score()

    # Drawing
    SCREEN.fill(WHITE)
    draw_pipes()
    draw_bird()
    draw_text(str(score), font, BLACK, SCREEN_WIDTH // 2, 50)

    if game_over:
        draw_text("Game Over", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
        draw_text("Press SPACE to Play Again", small_font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
