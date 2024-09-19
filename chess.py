import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 640, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chess Game')

# Colors
light = (240, 217, 181)  # Light square color
dark = (181, 136, 99)    # Dark square color
text_color = (0, 0, 0)   # Text color (black)

# Size of each square
square_size = width // 8

# Font settings
pygame.font.init()
font = pygame.font.SysFont('Arial', 48)

# Your white side characters
whiteSide = [
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'k', 'q', 'b', 'k', 'r']
]

def draw_board():
    """Draws an 8x8 chessboard."""
    for row in range(8):
        for col in range(8):
            color = light if (row + col) % 2 == 0 else dark
            pygame.draw.rect(screen, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

def draw_pieces():
    """Draws the chess pieces as text characters from the whiteSide array."""
    for row in range(2):  # We only have two rows in whiteSide
        for col in range(8):
            piece = whiteSide[row][col]
            if piece:
                text_surface = font.render(piece, True, text_color)
                text_rect = text_surface.get_rect(center=(col * square_size + square_size // 2, row * square_size + square_size // 2))
                screen.blit(text_surface, text_rect)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the board and pieces
    draw_board()
    draw_pieces()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
