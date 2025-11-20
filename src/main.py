import pygame
import cv2
import numpy as np

from vector import Vector,add_vec

pygame.init()

GRID_SIZE = 25

WIDTH_SCREEN = 800*2
HEIGHT_SCREEN = 450*2

FPS = 60


clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH_SCREEN,HEIGHT_SCREEN))


def draw_background():
    gridw = int(WIDTH_SCREEN/GRID_SIZE)
    gridh = int(HEIGHT_SCREEN/GRID_SIZE)


    for x in range(gridw):
        for y in range(gridh):
            pygame.draw.rect(screen, (120,120,150), (x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE),1)


new_vec = Vector(0,-300, -2,-4)
new_vec.update_direction(2,4)
new_vec.update_size(80)
new_vec2 = Vector(
    0,-300, 1,-2
)
new_vec2.update_direction(-1,2)
new_vec2.update_size(50)

vec_sum = add_vec(new_vec,new_vec2)

def draw():
    draw_background()

    new_vec.draw(screen, (255,50,50))
    new_vec2.draw(screen, (50,255,50))
    vec_sum.draw(screen, (50,50,255))


run=True
frame_count = 0
frame_render_max = FPS*2
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter("vid/Test.mp4", fourcc, FPS, (WIDTH_SCREEN, HEIGHT_SCREEN))

export_video = True

while run:
    if frame_count > frame_render_max:
        run=False
        break
    clock.tick(FPS)
    

    pygame.display.set_caption(f"Test.mp4 - FPS: {round(clock.get_fps())}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    new_vec.update_size(new_vec.size+2)
    new_vec2.update_size(new_vec2.size+1)
    vec_sum = add_vec(new_vec,new_vec2)
    screen.fill((10,10,60))
    draw()

    if export_video:
        frame = pygame.surfarray.array3d(screen)
        frame = np.rot90(frame, -1)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.flip(frame, 1)
        video.write(frame)
    frame_count+=1
    pygame.display.flip()


video.release()
pygame.quit()
