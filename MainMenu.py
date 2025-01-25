import pygame, sys
from button import Button
import os

pygame.init()

# Set screen dimensions
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

# Load and scale the background image
BG = pygame.image.load("../MIRAGAME/background.jpg")
BG = pygame.transform.scale(BG, (1280, 720))  # Scale background to fit the screen size

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("../MIRAGAME/KnightWarrior-w16n8.otf", size)

def play():
    pygame.quit()  # Quit the initial pygame instance to prevent conflicts
    import inputGUI  # Import the second script here, assuming it's saved as 'quoridor_game.py'
    inputGUI.main()  # Run the main function from the Quoridor game script

def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        CREDITS_TEXT = get_font(45).render("Credits", True, "Black")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)

        # Draw underline below the Credits text
        pygame.draw.line(SCREEN, "Black", 
                         (CREDITS_RECT.left, CREDITS_RECT.bottom + 5), 
                         (CREDITS_RECT.right, CREDITS_RECT.bottom + 5), 3)

        # Render and display the honoring text
        Honouring_text = get_font(25).render("Ayush Singh (Dev)\nSushim Saini (Dev)", True, "Red")
        Honouring_rect = Honouring_text.get_rect(center=(640, 225))  # Position for honoring text
        
        Thanking_text = get_font(45).render("Credits", True, "Black")
        Thanking_rect = Thanking_text.get_rect(center = (640, 350))
        Mention_text = get_font(25).render("MIRA FLOWS", True, "Red")
        Mention_rect = Mention_text.get_rect(center=(640,425))
        
        
        SCREEN.blit(Honouring_text, Honouring_rect)
        SCREEN.blit(Thanking_text,Thanking_rect)
        SCREEN.blit(Mention_text,Mention_rect)

        CREDITS_BACK = Button(image=None, pos=(640, 690),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
        CREDITS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))  # Draw the resized background

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("../MIRAGAME/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        CREDITS_BUTTON = Button(image=pygame.image.load("../MIRAGAME/Options Rect.png"), pos=(640, 400),
                                text_input="CREDITS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../MIRAGAME/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
