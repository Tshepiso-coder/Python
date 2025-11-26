class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialise the game's settings"""
        # SCREEN SETTINGS
        self.width = 1200
        self.height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 3
        
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3