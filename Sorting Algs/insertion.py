import pygame, random

def visual(i, j):
	width, height = 1800, 900
	n = 4
	n = n - (width % n)
	print(n)

	win = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Game Test")

	clock = pygame.time.Clock()
					
	values = []
	for _ in range(int(width / n)):
		values.append(int(random.random() * height))
			

	#values.sort()
	running = True
	while running:
		#clock.tick(100)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		
		
		win.fill((0, 0, 0))
		for k in range(int(width / n)):
			# x = k, y = height - 1 (reverse height minus 1)
			# w = width of the object, h = reverse height of the object
			if k == j and i < int(width / n):
				pygame.draw.rect(win, (255, 0, 0), (k * n, height - 1, n, -values[k])) # Line
				#pygame.draw.rect(win, (255, 0, 0), (k, height - values[k], 1, -1)) # pixel
			else:
				pygame.draw.rect(win, (255, 255, 255), (k * n, height - 1, n, -values[k])) # Line
				#pygame.draw.rect(win, (255, 255, 255), (k, height - values[k], 1, -1)) # pixel
		pygame.display.update()
		
		if i < int(width / n):
			if j == 0:
				j = i
			if j > 0 and values[j - 1] > values[j]:
				print(values[j - 1], values[j])
				values[j], values[j - 1] = values[j - 1], values[j]
				j -= 1
			else:
				j = 0
				i += 1
			
		

def main():
	j = 0
	i = 1
	pygame.init()
	
	visual(i, j)
	
	pygame.quit()


if __name__=="__main__":
    main()
