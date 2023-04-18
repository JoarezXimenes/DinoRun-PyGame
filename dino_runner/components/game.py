import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

FONT_STYLE = "freesansbold.ttf"


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.score = 0
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.score = 0
        self.game_speed = 20
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
    
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit (text, text_rect)

    def draw_death_count(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Deaths: {self.death_count}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (850, 50)
        self.screen.blit (text, text_rect)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill('#FFFFFF')
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_death_count()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def daw_menu_text(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render("Press any key to start", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        self.screen.blit(text, text_rect)

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.daw_menu_text()
        else:
            self.screen.blit(ICON, (half_screen_width - 20, half_screen_height - 140))
            self.daw_menu_text()
            self.draw_score()
            ##OK mostrar mensagem de "Press any key to restart"
            ##OK mostrar score atingido
            ##OK mostrar death_count

            ###OK Resetar score e game_speed quando o jogo for 'restartado' 
            ###OK Criar método para remover a repetição de código para o texto

        pygame.display.flip()  # .update()

        self.handle_events_on_menu()