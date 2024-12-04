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

font = pygame.font.Font(None, 40)
text_font = pygame.font.Font(None, 60)
sub_text_font = pygame.font.Font(None, 50)
counter_font = pygame.font.Font(None, 30)

hard_questions = [
    {"question": "Какой запасной полисахарид у грибов?", "answer": "гликоген"},
    {"question": "Что является ДНК-вирусом?", "answer": "грипп"},
    {"question": "Какой орган выделяет инсулин?", "answer": "поджелудочная железа"},
    {"question": "Как называется кислородное дыхание?", "answer": "аэробное"},
    {"question": "Сколько у здорового человека хромосом?", "answer": "47"},
]

lite_questions = [
    {"question": "Какой запасной полисахарид у грибов?", "answer": "гликоген"},
    {"question": "Что является ДНК-вирусом?", "answer": "грипп"},
    {"question": "Какой орган выделяет инсулин?", "answer": "поджелудочная железа"},
    {"question": "Как называется кислородное дыхание?", "answer": "аэробное"},
    {"question": "Сколько у здорового человека хромосом", "answer": "46"},
]

current_question = 0
user_input = ""
show_congratulation = False
answer_complete = False
game_over = False
incorrect_steps = 0
score = 0

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


def draw_question(question, user_input, background_color, button_color):
    screen.fill(background_color)
    question_surface = text_font.render(question, True, BLACK)
    question_rect = question_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(question_surface, question_rect)
    input_surface = text_font.render(user_input, True, BLACK)
    input_rect = input_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(screen, button_color, input_rect.inflate(20, 20))
    screen.blit(input_surface, input_rect)


def draw_congratulation():
    screen.fill(GREEN)
    congrats_surface = text_font.render("Правильно!", True, BLACK)
    congrats_rect = congrats_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(congrats_surface, congrats_rect)
    subtext_surface = sub_text_font.render("Нажмите любую клавишу для продолжения...", True, BLACK)
    subtext_rect = subtext_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(subtext_surface, subtext_rect)
    r = "Ваше количество очков:" + str(current_question + 1)
    counter_surface = counter_font.render(r, True, BLACK)
    counter_rect = counter_surface.get_rect(center=(WIDTH // 3, HEIGHT // 2 + 150))
    screen.blit(counter_surface, counter_rect)


def draw_game_over():
    screen.fill(SALMON)
    end_text = text_font.render("И вы называете себя БМом?!", True, BLACK)
    end_text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(end_text, end_text_rect)
    end_sub_text = counter_font.render("Ваше количество очков: 4 - 1000", True, BLACK)
    sub_text_rect = end_sub_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(end_sub_text, sub_text_rect)


def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main_menu():
    global WIDTH, HEIGHT, screen
    background_color = WHITE
    button_color = BLUE
    user_name = ""
    input_active = False
    selected_difficulty = None
    selected_background_color = WHITE
    selected_button_color = BLUE
    blink_timer = 0
    blink_interval = 500
    lite_selected = False
    hard_selected = False

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

        # lite_button_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2, 150, 50)
        # hard_button_rect = pygame.Rect(WIDTH // 2 + 50, HEIGHT // 2, 150, 50)

        lite_button_rect = pygame.Rect(WIDTH // 2 - 230, HEIGHT // 2, 150, 50)
        hard_button_rect = pygame.Rect(WIDTH // 2 + 120, HEIGHT // 2, 150, 50)

        draw_button(lite_button_rect, "Lite", button_color, LIGHT_GRAY, lite_selected)
        draw_button(hard_button_rect, "Hard", button_color, LIGHT_GRAY, hard_selected)

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

                if lite_button_rect.collidepoint(event.pos):
                    selected_difficulty = "lite"
                    lite_selected = True
                    hard_selected = False

                elif hard_button_rect.collidepoint(event.pos):
                    selected_difficulty = "hard"
                    hard_selected = True
                    lite_selected = False

                elif bg_color_button_rect.collidepoint(event.pos):
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


def lite_mode(background_color, button_color):
    global WIDTH, HEIGHT, screen, score
    running = True
    escape_speed = 300
    current_question = 0
    button_positions = [
        # (WIDTH // 2 - 400, HEIGHT // 2),
        # (WIDTH // 2 + 200, HEIGHT // 2),
        # (WIDTH // 2 - 400, HEIGHT // 2 + 200),
        # (WIDTH // 2 + 200, HEIGHT // 2 + 200)

        (WIDTH // 2 - 450, HEIGHT // 2),
        (WIDTH // 2 + 80, HEIGHT // 2),
        (WIDTH // 2 - 450, HEIGHT // 2 + 200),
        (WIDTH // 2 + 80, HEIGHT // 2 + 200)
    ]

    buttons = [
        pygame.Rect(pos[0], pos[1], BUTTON_WIDTH, BUTTON_HEIGHT)
        for pos in button_positions
    ]

    while running:
        screen.fill(background_color)

        question_surface = font.render(lite_questions[current_question]["question"], True, BLACK)
        question_rect = question_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(question_surface, question_rect)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for i, button in enumerate(buttons):
            if i == 0:
                draw_button(button, lite_questions[current_question]["answer"], button_color, LIGHT_GRAY)
            else:
                draw_button(button, "Неправильный ответ", button_color, LIGHT_GRAY)

        for button in buttons:
            if current_question < len(lite_questions) - 1:
                if button.collidepoint(mouse_x, mouse_y) and button != buttons[0]:
                    button.x += random.randint(-escape_speed, escape_speed)
                    button.y += random.randint(-escape_speed, escape_speed)
                    button.x = max(0, min(WIDTH - BUTTON_WIDTH, button.x))
                    button.y = max(0, min(HEIGHT - BUTTON_HEIGHT, button.y))
            else:
                if button.collidepoint(mouse_x, mouse_y) and button == buttons[0]:
                    button.x += random.randint(-escape_speed, escape_speed)
                    button.y += random.randint(-escape_speed, escape_speed)
                    button.x = max(0, min(WIDTH - BUTTON_WIDTH, button.x))
                    button.y = max(0, min(HEIGHT - BUTTON_HEIGHT, button.y))

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(event.pos) and current_question < len(lite_questions) - 1:
                    score += 1
                    current_question += 1
                    if current_question == len(lite_questions):
                        running = False
                        draw_game_over()
                        pygame.display.flip()
                        pygame.time.wait(3000)
                    else:
                        random.shuffle(button_positions)
                        for i, pos in enumerate(button_positions):
                            buttons[i].topleft = pos
                else:
                    for i, button in enumerate(buttons):
                        if button.collidepoint(event.pos) and i == 0:
                            pass
                        elif button.collidepoint(event.pos):
                            current_question += 1
                            score -= 9999
                            if current_question == len(lite_questions):
                                running = False
                                draw_game_over()
                                pygame.display.flip()
                                pygame.time.wait(3000)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def hard_mode(background_color, button_color):
    global current_question, user_input, show_congratulation, answer_complete, game_over, incorrect_steps, WIDTH, HEIGHT, screen, score

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

            elif event.type == pygame.KEYDOWN:
                if game_over:
                    continue
                if show_congratulation:
                    show_congratulation = False
                    user_input = ""
                    answer_complete = False
                    current_question += 1
                    score += 1
                    if current_question >= len(hard_questions):
                        running = False
                        draw_game_over()
                        pygame.display.flip()
                        pygame.time.wait(3000)
                else:
                    correct_answer = hard_questions[current_question]["answer"]
                    if current_question < len(hard_questions) - 1:
                        if not answer_complete:
                            if len(user_input) < len(correct_answer):
                                user_input += correct_answer[len(user_input)]
                            if user_input == correct_answer:
                                answer_complete = True
                        else:
                            show_congratulation = True
                    elif current_question == len(hard_questions) - 1:
                        if len(user_input) < len(correct_answer):
                            user_input += correct_answer[len(user_input)]
                        else:
                           game_over = True

        if game_over:
            draw_game_over()
        elif current_question < len(hard_questions):
            if show_congratulation:
                draw_congratulation()
            else:
                draw_question(hard_questions[current_question]["question"], user_input, background_color, button_color)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


def main():
    user_name, background_color, button_color, selected_difficulty = main_menu()
    print(f"User Name: {user_name}")
    print(f"Background Color: {background_color}")
    print(f"Button Color: {button_color}")
    print(f"Selected Difficulty: {selected_difficulty}")

    if selected_difficulty == "lite":
        lite_mode(background_color, button_color)
    elif selected_difficulty == "hard":
        hard_mode(background_color, button_color)


if __name__ == "__main__":
    main()
