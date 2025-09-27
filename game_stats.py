class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Load the high score from file, or default to 0.
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Load the saved high score from a file, return 0 if not found or invalid."""
        try:
            with open("high_score.txt", "r") as f:
                contents = f.read().strip()
                return int(contents) if contents else 0
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        """Save the high score to a file."""
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))
