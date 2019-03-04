import keyboard #Using module keyboard
import pyautogui

#buy 100 catnip: 1000, 200
#astronomical event: 1200, 185
#buy catnip field: 575, 250
#buy barn: 575, 300
#buy a library: 875, 250
def soloCat():
	print pyautogui.position()
	# 100 catnip
	pyautogui.moveTo(1000, 200)
	pyautogui.PAUSE = 0.5
	pyautogui.click()
	# astronomical event
	pyautogui.moveTo(1200, 185)
	pyautogui.click()
	# buy catnip field
	pyautogui.moveTo(575, 250)
	pyautogui.click()
	# buy barn
	pyautogui.moveTo(575, 300)
	pyautogui.click()
	# buy a library
	pyautogui.moveTo(875, 250)
	pyautogui.click()
	pyautogui.PAUSE = 30

#320, 700 - 320, 680 - 320, 660 - 320, 640 - 320, 620 - 870, 705 - 870, 660
def multiCat():
	print pyautogui.position()
	# Steel
	pyautogui.moveTo(320, 700)
	pyautogui.PAUSE = 0.5
	pyautogui.click()
	# Plate
	pyautogui.moveTo(320, 680)
	pyautogui.click()
	# Slab
	pyautogui.moveTo(320, 660)
	pyautogui.click()
	# Beam
	pyautogui.moveTo(320, 640)
	pyautogui.click()
	# Wood
	pyautogui.moveTo(320, 620)
	pyautogui.click()
	# Promotions
	pyautogui.moveTo(870, 705)
	pyautogui.click()
	# Hunters
	pyautogui.moveTo(65, 560)
	pyautogui.click()
	# Astronomy
	pyautogui.moveTo(1250, 215)
	pyautogui.click()
	# Wait timer
	pyautogui.PAUSE = 600



active = False
pyautogui.PAUSE = 1
while True:#making a loop
	if keyboard.is_pressed('q') and not active:#if key 'q' is pressed 
		active = True
	elif keyboard.is_pressed('e') and active:
		active = False
	elif keyboard.is_pressed('esc'):
		exit()
	if active:
		multiCat()
	
