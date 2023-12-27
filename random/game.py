import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grid Click Example")

# Define grid parameters
rows, cols = 6, 6
cell_width = width // cols
cell_height = (height-100) // rows

board = [['' for _ in range(cols)] for _ in range(rows)]
player_turn = 1

# Function to draw the grid
def draw_grid():
    for row in range(1, rows):
        pygame.draw.line(screen, (255, 255, 255), (0, row * cell_height + 100), (width, row * cell_height + 100), 2)
    for col in range(1, cols):
        pygame.draw.line(screen, (255, 255, 255), (col * cell_width, 100), (col * cell_width, height), 2)

    for row in range(rows):
        for col in range(cols):
            symbol = board[row][col]
            if symbol == 'X':
                pygame.draw.line(screen, (255, 255, 255), (col * cell_width, row * cell_height + 100),
                                 ((col + 1) * cell_width, (row + 1) * cell_height + 100), 2)
                pygame.draw.line(screen, (255, 255, 255), ((col + 1) * cell_width, row * cell_height + 100),
                                 (col * cell_width, (row + 1) * cell_height + 100), 2)
            elif symbol == 'O':
                pygame.draw.circle(screen, (255, 255, 255),
                                   (col * cell_width + cell_width // 2, row * cell_height + cell_height // 2 + 100),
                                   cell_width // 2, 2)

            elif symbol == -1:
                # fill cell with white color
                pygame.draw.rect(screen, (255, 255, 255), (col * cell_width + 1, row * cell_height + 100 + 1,
                                                           cell_width - 1, cell_height - 1))

# Function to convert mouse coordinates to grid coordinates
def screen_to_grid(mouse_x, mouse_y):
    col = mouse_x // cell_width
    row = (mouse_y-100) // cell_height
    return row, col

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row, col = screen_to_grid(mouse_x, mouse_y)
            if 0 <= row < rows and 0 <= col < cols:
                if board[row][col] == '':
                    if player_turn:
                        board[row][col] = 'X'
                    else:
                        board[row][col] = 'O'
                    player_turn = 1 - player_turn

                print(f"Clicked on grid position: ({row}, {col})")

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the grid
    draw_grid()

    # Update the display
    pygame.display.flip()
