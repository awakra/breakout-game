# Screen
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Paddle
PADDLE_WIDTH = 200
PADDLE_HEIGHT = 20
PADDLE_SPEED = 800  # pixels per second for delta time movement

# Ball
BALL_RADIUS = 10
BALL_SPEED = 600  # pixels per second

# Bricks
BRICK_COLS = 12
BRICK_ROWS = 5
BRICK_WIDTH = 139  # calculated for 12 cols centered
BRICK_HEIGHT = 40
BRICK_PADDING = 5
BRICK_OFFSET_TOP = 60
BRICK_COLORS = [
    (255, 0, 0),      # Red
    (255, 165, 0),    # Orange
    (255, 255, 0),    # Yellow
    (0, 255, 0),      # Green
    (0, 0, 255)       # Blue
]

# Metrics
INITIAL_LIVES = 3
FONT_SIZE = 30