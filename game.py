import pygame
import time
import random
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
from morty import Morty
from rick import Rick
import cv2
import ui
class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background('assets/images/background/game_bg.jpg')
        self.cap = cv2.VideoCapture(0)
        self.sounds = {}
        self.sounds["im_out"] = pygame.mixer.Sound("assets/sounds/Combo.wav")
    def reset(self): 
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.rms = []
        self.rms_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()
    def spawn_rms(self):
        t = time.time()
        if t > self.rms_spawn_timer:
            self.rms_spawn_timer = t + MORTY_SPAWN_TIME
            nb = (GAME_DURATION-self.time_left)/GAME_DURATION * 100  / 2
            if random.randint(0, 100) < nb:
                self.rms.append(Rick())
            else:
                self.rms.append(Morty())
            if self.time_left < GAME_DURATION/2:
                self.rms.append(Morty())
    def load_camera(self):
        _, self.frame = self.cap.read()
    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)
    def draw(self):
        self.background.draw(self.surface)
        for rm in self.rms:
            rm.draw(self.surface)
        self.hand.draw(self.surface)
        ui.draw_text(self.surface, f"Score : {self.score}", (5, 5), COLORS["score"], font=FONTS["medium"],
                    shadow=False)
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"]
        ui.draw_text(self.surface, f"Time left : {self.time_left}", (SCREEN_WIDTH//2 + 50, 5),  timer_text_color, font=FONTS["medium"],
                    shadow=False)

    def game_time_update(self):
        self.time_left = int(GAME_DURATION - (time.time() - self.game_start_time))
        if self.time_left < 0:
            self.time_left = 0
    def update(self):
        self.load_camera()
        self.set_hand_position()
        self.game_time_update()
        self.draw()
        if self.time_left > 0:
            self.spawn_rms()
            (x, y) = self.hand_tracking.get_hand_center()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.hand_closed
            if self.hand.left_click:
                self.hand.image = self.hand.image_smaller.copy()
            else:
                self.hand.image = self.hand.orig_image.copy()
            self.score = self.hand.kill_rms(self.rms, self.score, self.sounds)
            for rm in self.rms:
                rm.move()
        else:
            if ui.button(self.surface, 540, "Continue", click_sound=self.sounds["im_out"]):
                return "menu"
        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
