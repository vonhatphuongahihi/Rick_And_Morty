import pygame
import sys
from settings import *
import ui
import image
from moviepy.editor import VideoFileClip

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.background = VideoFileClip('assets/videos/menu_bg.mp4')
        self.background.set_duration(self.background.duration)
        self.background_frame = self.background.get_frame(0)
        self.start_time = pygame.time.get_ticks()
        self.click_sound_start = pygame.mixer.Sound(f"assets/sounds/game_start.mp3")
        self.click_sound_quit = pygame.mixer.Sound(f"assets/sounds/game_quit.mp3")

        self.video_width, self.video_height = self.background.size
        self.x_offset = (SCREEN_WIDTH - self.video_width) // 2
        self.y_offset = (SCREEN_HEIGHT - self.video_height) // 2

        self.start_clicked = False
        self.quit_clicked = False
        self.start_click_time = 0
        self.quit_click_time = 0

    def draw(self):
        current_time = (pygame.time.get_ticks() - self.start_time) / 1000.0
        self.background_frame = self.background.get_frame(current_time % self.background.duration)
        frame_surface = pygame.surfarray.make_surface(self.background_frame.swapaxes(0, 1))
        self.surface.blit(frame_surface, (self.x_offset, self.y_offset))

    def update(self):
        self.draw()
        if self.start_clicked:
            if pygame.time.get_ticks() - self.start_click_time > 5000:  
                return "game"
        elif self.quit_clicked:
            if pygame.time.get_ticks() - self.quit_click_time > 5000:  
                pygame.quit()
                sys.exit()
        else:
            if ui.button(self.surface, 320, "Start", click_sound=self.click_sound_start):
                self.start_clicked = True
                self.start_click_time = pygame.time.get_ticks()
            if ui.button(self.surface, 320 + BUTTONS_SIZES[1] * 1.5, "Quit", click_sound=self.click_sound_quit):
                self.quit_clicked = True
                self.quit_click_time = pygame.time.get_ticks()
                self.click_sound_quit.play()
        return "menu"