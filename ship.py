import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen

        image = pygame.image.load('images/aircraft.jpg')
        self.image = pygame.transform.scale(image, (80,60))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed

        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx

