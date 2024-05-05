import pygame
pygame.init()
screen = pygame.display.set_mode((600,800))
clock = pygame.time.Clock()
running = True
spritesheet = pygame.image.load('images/clubs.png').convert_alpha()
pygame.display.set_caption('Duren')
def get_image(sheet, width, height, scale, x,y):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,0),((x),(y), width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    return image

card_1 = get_image(spritesheet, 90, 128, 1, 0, 0)
card_2  = get_image(spritesheet, 90, 128, 1, 90, 0)
card_3 = get_image(spritesheet, 90, 128, 1, 180, 0)
card_4 = get_image(spritesheet, 90, 128, 1, 270, 0)
card_5 = get_image(spritesheet, 90, 128, 1, 360, 0)
card_6 = get_image(spritesheet, 90, 128, 1, 0, 128)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("red")
    screen.blit(card_1,(0,0))
    screen.blit(card_2,(90,0))
    screen.blit(card_3,(180,0))
    screen.blit(card_4,(270,0))
    screen.blit(card_5,(360,0))
    screen.blit(card_6,(450,0))

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()