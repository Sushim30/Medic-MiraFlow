import pygame
import threading
from healthCheck import print_screen

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BG_COLOR = (58, 71, 102)
BOX_COLOR = (220, 220, 220)
TEXT_COLOR = (255, 204, 0)
BUTTON_COLOR = (160, 50, 50)
BUTTON_TEXT_COLOR = (255, 255, 255)
TITLE_FONT = pygame.font.Font("../MIRAGAME/KnightWarrior-w16n8.otf", 64)
LABEL_FONT = pygame.font.Font("../MIRAGAME/KnightWarrior-w16n8.otf", 36)
INPUT_FONT = pygame.font.Font("../MIRAGAME/KnightWarrior-w16n8.otf", 24)
WAIT_FONT = pygame.font.Font("../MIRAGAME/KnightWarrior-w16n8.otf", 64)
INPUT_BOX_WIDTH = 300
INPUT_BOX_HEIGHT = 40

result = ""

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dr. Shishimaru")

# Input boxes and labels
input_boxes = [
    pygame.Rect(640, 240 + i * 60, INPUT_BOX_WIDTH, INPUT_BOX_HEIGHT) for i in range(7)
]
labels = ["Name", "Age", "Sex", "Weight", "Symptom1","Symptom2","Symptom3"]
inputs = [""] * 7
Doctor_image = pygame.image.load("../MIRAGAME/Group 1.png")
Doctor_rect = Doctor_image.get_rect(midleft=(0,SCREEN_HEIGHT/2))
# Button
button_rect = pygame.Rect(1000, 650, 200, 60)


def Checkdraw_gui():
    screen.fill(BG_COLOR)

    # Title
    title_surface = TITLE_FONT.render("Dr. Shishimaru", True, TEXT_COLOR)
    screen.blit(title_surface, (SCREEN_WIDTH / 2 - title_surface.get_width() / 2, 100))
    screen.blit(Doctor_image,Doctor_rect)

    # Input boxes and labels
    for i, box in enumerate(input_boxes):
        pygame.draw.rect(screen, BOX_COLOR, box)
        label_surface = LABEL_FONT.render(labels[i], True, TEXT_COLOR)
        screen.blit(label_surface, (475, 240 + i * 60))

        # Render user input text
        input_surface = INPUT_FONT.render(inputs[i], True, (0, 0, 0))
        screen.blit(input_surface, (box.x + 10, box.y + 10))

    # Submit button
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    button_surface = LABEL_FONT.render("SUBMIT", True, BUTTON_TEXT_COLOR)
    screen.blit(button_surface, (button_rect.x +50, button_rect.y + 10))

def MEDdraw_gui():
    show_wait_screen()
    

def show_wait_screen():
    screen.fill((255, 255, 0))  # Yellow background
    wait_surface = WAIT_FONT.render("Wait", True, TEXT_COLOR)
    screen.blit(wait_surface, wait_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)))
    pygame.display.update()

def show_complete_screen():
    screen.fill((0, 225, 0))  # Green background
    wait_surface = WAIT_FONT.render("Done", True, TEXT_COLOR)
    screen.blit(wait_surface, wait_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)))
    pygame.display.update()
    pygame.time.delay(2000)
    running = False

def submit_form(inputs):
    global result
    # Simulate the external function call
    try:
        result = print_screen(inputs)  # Blocking call
    except Exception as e:
        print("Error in print_screen:", e)
    finally:
        result = "done"  # Ensure result gets updated


# Main loop
running = True
active_box = None
processing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check for input box activation
            for i, box in enumerate(input_boxes):
                if box.collidepoint(event.pos):
                    active_box = i
                    break
            else:
                active_box = None

            # Check if the submit button is clicked
            if button_rect.collidepoint(event.pos) and not processing:
                processing = True
                result = ""  # Reset result
                # Start processing in a background thread
                threading.Thread(target=submit_form, args=(inputs,), daemon=True).start()

        if event.type == pygame.KEYDOWN and active_box is not None:
            if event.key == pygame.K_BACKSPACE:
                inputs[active_box] = inputs[active_box][:-1]
            elif len(inputs[active_box]) < 20:  # Limit input length
                inputs[active_box] += event.unicode

    # Display GUI or wait screen based on the processing state
    if processing and result == "" :
        show_wait_screen()
    elif result != "":
        show_complete_screen()
    else:
        processing = False  # Reset processing state if done
        Checkdraw_gui()

    pygame.display.flip()

pygame.quit()



