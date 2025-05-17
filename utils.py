import pygame
from sprites.brick import Brick
from constants import *

def game_loop_step(
    screen,
    framerate,
    scoreboard,
    lives,
    all_sprites,
    paddle,
    ball,
    collision_manager,
    waiting_for_launch,
    running,
    FPS
):
    dt = framerate.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    paddle.update(keys, dt)

    if waiting_for_launch:
        ball.attach_to_paddle(paddle)
        if keys[pygame.K_UP]:
            waiting_for_launch = False
            ball.launch()
    else:
        ball.update(dt)

    hit_blocks = collision_manager.handle_collisions()
    if hit_blocks:
        points = len(hit_blocks) * 10
        scoreboard.add_points(points)

    if ball.speed_x == 0 and ball.speed_y == 0:
        if not waiting_for_launch:
            lives.lose_life()
        waiting_for_launch = True

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    framerate.draw()
    scoreboard.draw()
    lives.draw()
    pygame.display.flip()

    return waiting_for_launch, running

def reset_game_state(
    all_sprites,
    bricks_group,
    paddle,
    ball,
    scoreboard,
    lives
):
    # Remove all bricks from groups
    for brick in bricks_group:
        brick.kill()
    # Create new bricks and add to groups
    new_bricks = Brick.create_wall()
    for brick in new_bricks:
        bricks_group.add(brick)
        all_sprites.add(brick)
    # Reset paddle and ball positions
    paddle.rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40)
    paddle.pos_x = float(paddle.rect.x)
    ball.reset(paddle)
    # Reset score and lives
    scoreboard.reset()
    lives.reset()
    return bricks_group