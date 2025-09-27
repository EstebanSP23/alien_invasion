import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties for the button.
        self.width, self.height = 200, 50
        self.button_color = (135, 135, 135)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The message button needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_instructions(self):
        """Draw instructions on screen."""
        font = pygame.font.SysFont(None, 28)
        text_color = (255, 255, 255)

        instructions = [
            "INSTRUCTIONS:",
            "- Move with LEFT and RIGHT arrows",
            "- Shoot with SPACE",
            "- Press Q to quit",
            "- Only 3 bullets allowed at all times",
            "Goal: Destroy all aliens before they reach the bottom!"
        ]

        # Starting y-position (just below the button)
        y_offset = self.rect.bottom + 90

        for line in instructions:
            msg_image = font.render(line, True, text_color)
            msg_rect = msg_image.get_rect()
            msg_rect.centerx = self.screen_rect.centerx
            msg_rect.top = y_offset
            self.screen.blit(msg_image, msg_rect)
            y_offset += 30  # Space between lines