import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
import os

#================================================

# AlienInvasion class - Manages all game assets and behavior
# Initialization (__init__):

# Initializes Pygame
# Creates a game clock for controlling frame rate
# Loads game settings from a Settings class
# Sets up fullscreen display mode
# Updates screen dimensions in settings
# Sets window caption to "Alien Invasion"
# Creates a ship instance
# Creates a sprite group to manage bullets

# Main Game Loop (run_game):

# Runs continuously at 60 FPS
# Checks for events (keyboard/mouse input)
# Updates ship position
# Updates bullet positions
# Prints bullet count (for debugging)
# Redraws the screen

# Event Handling Methods:

# _check_event() - Monitors all game events (quit, key presses/releases)
# _check_keydown_events() - Handles key presses:

# Right arrow: move ship right
# Left arrow: move ship left
# Q key: quit game
# Spacebar: fire bullet


# _check_keyup_events() - Handles key releases (stops ship movement)

# Bullet Management:

# _fire_bullet() - Creates new bullet and adds it to the bullets group
# _update_bullets() - Updates bullet positions and removes bullets that go off-screen (top)

# Screen Updates (_update_screen):

# Fills screen with background color
# Draws all bullets
# Draws the ship
# Updates the display

# Program Entry Point:

# Creates game instance and starts the game loop

# Key concepts:

# Game loop: Continuous cycle that updates game state and redraws screen
# Sprite groups: Efficient way to manage multiple game objects
# Event-driven programming: Responds to user input
# Frame rate control: clock.tick(60) limits game to 60 FPS
# Modular design: Separate methods for different responsibilities

# This is a classic shoot-em-up game structure where the player controls a ship and fires bullets!

#================================================
class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        
        # MAKE AN INSTANCE OF THE pygame CLOCK
        self.clock = pygame.time.Clock()
        
        self.settings = Settings()
        
        # self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_event()
            self.ship.update()
            self._update_bullets()
            print(len(self.bullets))
            
            self._update_screen()
            self.clock.tick(60)
            
    def _check_event(self):
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                

                        
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
         #REDRAW THE SCREEN DUING EACH PASS THROUGH THE LOOP
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

