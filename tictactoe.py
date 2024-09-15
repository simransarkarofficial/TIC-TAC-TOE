import cv2
import numpy as np
import random

# Initialize the Tic-Tac-Toe grid
grid_size = 600
cell_size = grid_size // 3

# Create a black canvas
canvas = np.zeros((grid_size, grid_size, 3), dtype=np.uint8)

# Function to draw the Tic-Tac-Toe grid
def draw_grid():
    line_color = (255, 255, 255)  # White color
    line_thickness = 5
    cv2.line(canvas, (cell_size, 0), (cell_size, grid_size), line_color, line_thickness)
    cv2.line(canvas, (2 * cell_size, 0), (2 * cell_size, grid_size), line_color, line_thickness)
    cv2.line(canvas, (0, cell_size), (grid_size, cell_size), line_color, line_thickness)
    cv2.line(canvas, (0, 2 * cell_size), (grid_size, 2 * cell_size), line_color, line_thickness)

# Function to get the grid cell based on click coordinates
def get_cell(x, y):
    row = y // cell_size
    col = x // cell_size
    return row, col

# Function to draw X or O on the grid
def draw_move(row, col, player):
    center = (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
    if player == 'human':
        cv2.putText(canvas, 'X', center, cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5, cv2.LINE_AA)
    else:
        cv2.putText(canvas, 'O', center, cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 5, cv2.LINE_AA)

# Function to check if a cell is empty
def is_empty(row, col):
    return game_board[row][col] == ''

# Function to check for a win
def check_winner(player):
    for row in range(3):
        if all([game_board[row][col] == player for col in range(3)]):
            return True
    for col in range(3):
        if all([game_board[row][col] == player for row in range(3)]):
            return True
    if all([game_board[i][i] == player for i in range(3)]) or all([game_board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Function for AI to make a random move
def ai_move():
    empty_cells = [(r, c) for r in range(3) for c in range(3) if is_empty(r, c)]
    if empty_cells:
        row, col = random.choice(empty_cells)
        game_board[row][col] = 'O'
        draw_move(row, col, 'ai')
        if check_winner('O'):
            cv2.putText(canvas, 'AI Wins!', (50, grid_size // 2), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5, cv2.LINE_AA)
            return True
    return False

# Mouse click callback function
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        row, col = get_cell(x, y)
        if is_empty(row, col):
            game_board[row][col] = 'X'
            draw_move(row, col, 'human')
            if check_winner('X'):
                cv2.putText(canvas, 'You Win!', (50, grid_size // 2), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5, cv2.LINE_AA)
                return
            if not ai_move():
                pass

# Initialize the game board (3x3 grid)
game_board = [['' for _ in range(3)] for _ in range(3)]

# Draw the initial grid
draw_grid()

# Set up the OpenCV window and mouse callback
cv2.imshow('Tic-Tac-Toe', canvas)
cv2.setMouseCallback('Tic-Tac-Toe', click_event)

# Main loop
while True:
    cv2.imshow('Tic-Tac-Toe', canvas)
    if cv2.waitKey(1) & 0xFF == 27:  # Exit on ESC key
        break

cv2.destroyAllWindows()






