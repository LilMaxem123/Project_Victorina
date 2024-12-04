import random
import sys

import pygame

pygame.init()

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("кр по биологии")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
GRAY = (200, 200, 200)
SALMON = (250, 128, 114)
LIGHT_GRAY = (220, 220, 220)
LIGHT_BLUE = (135,206,250)

font = pygame.font.Font(None, 40)
text_font = pygame.font.Font(None, 60)
sub_text_font = pygame.font.Font(None, 50)
counter_font = pygame.font.Font(None, 30)

# buttons questions
BUTTON_WIDTH, BUTTON_HEIGHT = 420, 50

button_pressed = False


def draw_button(rect, text, color, hover_color=None, pressed=False):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if rect.collidepoint(mouse_x, mouse_y) and hover_color:
        pygame.draw.rect(screen, hover_color, rect, border_radius=7)
        pygame.draw.rect(screen, BLACK, rect, width=2, border_radius=7)
    elif pressed:
        pygame.draw.rect(screen, 'GREEN', rect, border_radius=7)
        pygame.draw.rect(screen, BLACK, rect, width=2, border_radius=7)

    else:
        pygame.draw.rect(screen, color, rect, border_radius=7)
        pygame.draw.rect(screen, BLACK, rect, width=2, border_radius=7)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main_menu():
    global WIDTH, HEIGHT, screen
    background_color = LIGHT_BLUE
    button_color = BLUE
    user_name = ""
    input_active = False
    selected_difficulty = None
    selected_background_color = WHITE
    selected_button_color = BLUE
    blink_timer = 0
    blink_interval = 500

    while True:
        screen.fill(background_color)

        title_surface = text_font.render("кр по биологии", True, BLACK)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title_surface, title_rect)

        input_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 100, 400, 50)
        pygame.draw.rect(screen, GRAY, input_rect)
        input_surface = text_font.render(user_name, True, BLACK)
        screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(400, input_surface.get_width() + 10)

        bg_color_button_rect = pygame.Rect(WIDTH // 2 - 280, HEIGHT // 2 + 100, 250, 50)
        button_color_button_rect = pygame.Rect(WIDTH // 2 + 50, HEIGHT // 2 + 100, 290, 50)

        draw_button(bg_color_button_rect, "Цвет фона", selected_background_color, selected_background_color, False)
        draw_button(button_color_button_rect, "Цвет кнопок", selected_button_color, selected_button_color, False)

        start_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 200, 200, 50)
        draw_button(start_button_rect, "Начать", button_color, LIGHT_GRAY)

        if input_active and pygame.time.get_ticks() % (blink_interval * 2) < blink_interval:
            cursor_surface = text_font.render("|", True, BLACK)
            screen.blit(cursor_surface, (input_rect.x + input_surface.get_width() + 10, input_rect.y + 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if input_rect.collidepoint(event.pos):
                    input_active = not input_active
                else:
                    input_active = False

                if bg_color_button_rect.collidepoint(event.pos):
                    selected_background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                elif button_color_button_rect.collidepoint(event.pos):
                    selected_button_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                if start_button_rect.collidepoint(event.pos):
                    if user_name and selected_difficulty:
                        return user_name, selected_background_color, selected_button_color, selected_difficulty
                    elif user_name and not selected_difficulty:
                        screen.fill(WHITE)
                        draw_text("Выберите уровень сложности", WIDTH//2, HEIGHT//2, RED)
                        pygame.display.flip()
                        pygame.time.wait(2000)
                    elif not user_name and not selected_difficulty:
                        screen.fill(WHITE)
                        draw_text("Выберите уровень сложности и введите имя", WIDTH//2, HEIGHT//2, RED)
                        input_active = True
                        pygame.display.flip()
                        pygame.time.wait(2000)
                    elif not user_name and  selected_difficulty:
                        screen.fill(WHITE)
                        draw_text("Введите имя", WIDTH//2, HEIGHT//2, RED)
                        input_active = True
                        pygame.display.flip()
                        pygame.time.wait(2000)

            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        user_name = user_name[:-1]
                    else:
                        user_name += event.unicode

        pygame.display.flip()
        clock.tick(60)

def main():
    user_name, background_color, button_color, selected_difficulty = main_menu()
    print(f"User Name: {user_name}")
    print(f"Background Color: {background_color}")
    print(f"Button Color: {button_color}")
    print(f"Selected Difficulty: {selected_difficulty}")


if __name__ == "__main__":
    main()