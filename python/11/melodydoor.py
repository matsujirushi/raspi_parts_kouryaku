import wiringpi as pi
import pygame.mixer
import time

DOOR_SENSOR_GPIO = 4
SOUND_FILE = "open.mp3";

def init_door_sensor():
	pi.wiringPiSetupGpio()
	
	pi.pinMode(DOOR_SENSOR_GPIO, pi.INPUT)
	pi.pullUpDnControl(DOOR_SENSOR_GPIO, pi.PUD_DOWN)

def read_door_sensor():
	return pi.digitalRead(DOOR_SENSOR_GPIO)

def init_sound():
	pygame.mixer.init()
	pygame.mixer.music.load(SOUND_FILE)

def play_sound():
	pygame.mixer.music.play()

init_door_sensor()
init_sound()

door_state = 1

while True:
	pre_door_state = door_state
	door_state = read_door_sensor()
	
	print(door_state)
	
	if pre_door_state == 1 and door_state == 0:
		print("Play sound !")
		play_sound()
	
	time.sleep(0.1)

