import pygame


class Sprite():
    def __init__(self, x, y, width, height, sprites):
        self.sprites = sprites
        self.width = width
        self.height = height
        self.frames = self.load_sprites(1)
        self.current_frame = 0
        self.rect = pygame.Rect(x, y, width, height)

    def load_sprites(self, scale):
        frames = []
        for sprite in self.sprites:
            frame = pygame.image.load(sprite).convert_alpha()
            frame = pygame.transform.scale(frame, (self.width * scale, self.height * scale))
            frames.append(frame)
        return frames

    def update(self):
        screen.blit(self.frames[self.current_frame], (self.rect.x, self.rect.y))

    def next_frame(self):
        if self.current_frame >= len(self.frames) - 1:
            self.current_frame = 0
        else:
            self.current_frame += 1


class Mouse(Sprite):
    def __init__(self, x, y, width, height, sprites):
        super().__init__(x, y, width, height, sprites)
        self.jumping = False
        self.velocity_y = 0
        self.gravity = 1


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.velocity_y = -19

        if self.jumping:
            self.rect.y += self.velocity_y
            self.velocity_y += self.gravity

            if self.rect.y >= 220:
                self.rect.y = 220
                self.jumping = False
                self.velocity_y = 0


class Cat(Sprite):
    def __init__(self, x, y, width, height, sprites):
        super().__init__(x, y, width, height, sprites)
        self.speed = 3

    def move(self):
        if self.rect.x > -100:
            self.rect.x -= self.speed
        else:
            self.rect.x = 600

    def colliderect(self, cat):
        if self.rect.colliderect(cat.rect):
            return True
        else:
            return False



pygame.init()
screen = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()
background = pygame.image.load("background.jpg")
mouse_sprites = ["sprite_run0.png", "sprite_run1.png", "sprite_run2.png",
                 "sprite_run3.png", "sprite_run4.png", "sprite_run5.png"]

cat_sprites = ["cat_0.png", "cat_1.png", "cat_2.png", "cat_3.png",
               "cat_4.png", "cat_5.png", "cat_6.png", "cat_7.png"]

mouse = Mouse(0, 220, 150, 150, mouse_sprites)
mouse.rect = pygame.Rect(0, 220, 100, 100)
cat = Cat(600, 250, 75, 60, cat_sprites)
cloud = Cat(300, 10, 150, 100, ["cloud.jpg"])
cheese = Cat(700, 60, 150, 100, ["cheese.jpg"])
score_font = pygame.font.SysFont("Arial", 26, bold=True)

cat.speed = 8
wait = 0
score = 0
wait_score = 0
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if cat.colliderect(mouse):
        break

    screen.blit(background, (0,0))

    cat.move()
    cat.update()

    cloud.move()
    cloud.update()

    cheese.move()
    cheese.update()

    screen.blit(score_font.render(f"Score: {score}", True, (0, 0, 0)), (10, 0))

    mouse.move()
    mouse.update()


    if wait == 5:
        mouse.next_frame()
        cat.next_frame()
        wait = 0
    else:
        wait += 1

    if wait_score == 60:
        score += 1
        wait_score = 0
    else:
        wait_score += 1
    pygame.display.update()
    clock.tick(60)



screen.blit(background, (0, 0))
screen.blit(score_font.render("You Lose!", True, (255, 0, 0)), (200, 200))
screen.blit(score_font.render(f"Score: {score}", True, (0, 0, 0)), (200, 220))

pygame.quit()

