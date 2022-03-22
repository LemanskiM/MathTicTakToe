import random
import pygame

pygame.init()
WIDTH, HEIGHT = 900,600
BGCOLOR = (255,255,255)
COLOR_LINE = (0,0,0)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WIN.fill(BGCOLOR)
FONT = pygame.font.SysFont('comicsans', 40)

image_o = pygame.image.load("o.png")
image_x = pygame.image.load("x.png")

#list of numbers
NUMBERS = []
# 1 number in equation
LIST1 = []
# 2 number in equation
LIST2 = []
# score of equation
SCORE = []
# equation to print
EQUATION_PRINT = []

TEXT = []

PLAYER1 = 1

def createNumbers():
	# create list of numbers
	for i in range (0,15):
		NUMBERS.append(i+1)
		i+=1

	# create list of elements equation
	for i in range (0,9):
		LIST1.append(random.randint(NUMBERS[0], len(NUMBERS)))
		LIST2.append(random.randint(NUMBERS[0], len(NUMBERS)))

	# create score and equation
	for i in range (0,9):
		SCORE.append(LIST1[i]*LIST2[i])
		EQUATION_PRINT.append(f"{LIST1[i]} * {LIST2[i]}")

def drawLines():
	lines = [200,400]
	for i in range(0,2):
		pygame.draw.line(WIN, COLOR_LINE, (0,lines[i]) , (WIDTH-300, lines[i]))
		pygame.draw.line(WIN, COLOR_LINE, (lines[i],0) , (lines[i], HEIGHT))

def drawEquation():

	text1 = FONT.render(EQUATION_PRINT[0], 1, COLOR_LINE)
	text2 = FONT.render(EQUATION_PRINT[1], 1, COLOR_LINE)
	text3 = FONT.render(EQUATION_PRINT[2], 1, COLOR_LINE)
	text4 = FONT.render(EQUATION_PRINT[3], 1, COLOR_LINE)
	text5 = FONT.render(EQUATION_PRINT[4], 1, COLOR_LINE)
	text6 = FONT.render(EQUATION_PRINT[5], 1, COLOR_LINE)
	text7 = FONT.render(EQUATION_PRINT[6], 1, COLOR_LINE)
	text8 = FONT.render(EQUATION_PRINT[7], 1, COLOR_LINE)
	text9 = FONT.render(EQUATION_PRINT[8], 1, COLOR_LINE)


	WIN.blit(text1, (40, 70))
	WIN.blit(text2, (240, 70))
	WIN.blit(text3, (440, 70))
	WIN.blit(text4, (40, 270))
	WIN.blit(text5, (240, 270))
	WIN.blit(text6, (440, 270))
	WIN.blit(text7, (40, 470))
	WIN.blit(text8, (240, 470))
	WIN.blit(text9, (440, 470))



class InputBox:

	def __init__(self,x,y,w,h,text = ""):
		self.rect = pygame.Rect(x,y,w,h)
		self.color = COLOR_INACTIVE
		self.text = text
		self.txt_surface = FONT.render(text, True, self.color)
		self.active = False
	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(event.pos):
				self.active = not self.active
			else:
				self.active = False
			self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
		if event.type == pygame.KEYDOWN:
			if self.active:
				if event.key == pygame.K_RETURN:
					print(self.text)
					TEXT.append(self.text)
					self.text = ""
					global PLAYER1
					PLAYER1 *= -1
				elif event.key == pygame.K_BACKSPACE:
					self.text = self.text[:-1]
				else:
					self.text +=event.unicode
				self.txt_surface = FONT.render(self.text, True, self.color)
	def update(self):
		width = max(200, self.txt_surface.get_width()+10)
		self.rect.w = width

	def draw(self, screen):
		screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
		pygame.draw.rect(screen, self.color, self.rect, 2)

	def check(list1,list2,score,text):
		number = text[0]
		for l in range(0,9):
			if int(number) == score[l] and score[l] == list1[l]*list2[l]:
				if PLAYER1 == -1:
					EQUATION_PRINT[l] = "0"
				else:
					EQUATION_PRINT[l] = "x"
				SCORE[l] = "0"

				if len(TEXT) != 0:
					TEXT.clear()
			else:
				if len(TEXT) != 0:
					TEXT.clear()
	def checkplayer(player):
		if player == 1:
			player1text = FONT.render("PLAYER 1", 1, ("blue"))
			WIN.blit(player1text, (650, 400))
		elif player == -1:
			player1text = FONT.render("PLAYER 2", 1, ("red"))
			WIN.blit(player1text, (650, 400))

	def winCheck():

		if EQUATION_PRINT[0] == "0":
			WIN.blit(image_o, (40,50))
		elif EQUATION_PRINT[0] == "x":
			WIN.blit(image_x, (40,50))

		if EQUATION_PRINT[1] == "0":
			WIN.blit(image_o, (240,50))
		elif EQUATION_PRINT[1] == "x":
			WIN.blit(image_x, (240,50))

		if EQUATION_PRINT[2] == "0":
			WIN.blit(image_o, (440,50))
		elif EQUATION_PRINT[2] == "x":
			WIN.blit(image_x, (440,50))

		if EQUATION_PRINT[3] == "0":
			WIN.blit(image_o, (40,250))
		elif EQUATION_PRINT[3] == "x":
			WIN.blit(image_x, (40,250))

		if EQUATION_PRINT[4] == "0":
			WIN.blit(image_o, (240,250))
		elif EQUATION_PRINT[4] == "x":
			WIN.blit(image_x, (240,250))

		if EQUATION_PRINT[5] == "0":
			WIN.blit(image_o, (440,250))
		elif EQUATION_PRINT[5] == "x":
			WIN.blit(image_x, (440,250))

		if EQUATION_PRINT[6] == "0":
			WIN.blit(image_o, (40,450))
		elif EQUATION_PRINT[6] == "x":
			WIN.blit(image_x, (40,450))

		if EQUATION_PRINT[7] == "0":
			WIN.blit(image_o, (240,450))
		elif EQUATION_PRINT[7] == "x":
			WIN.blit(image_x, (240,450))

		if EQUATION_PRINT[8] == "0":
			WIN.blit(image_o, (440,450))
		elif EQUATION_PRINT[8] == "x":
			WIN.blit(image_x, (440,450))

		if EQUATION_PRINT[0] == "0" and EQUATION_PRINT[1] == "0" and EQUATION_PRINT[2] == "0":
			pygame.draw.line(WIN, COLOR_LINE, (20,100) , (560, 100))
		elif EQUATION_PRINT[3] == "0" and EQUATION_PRINT[4] == "0" and EQUATION_PRINT[5] == "0":
			pygame.draw.line(WIN, COLOR_LINE, (20,300) , (560, 300))
		elif EQUATION_PRINT[6] == "0" and EQUATION_PRINT[7] == "0" and EQUATION_PRINT[8] == "0":
			pygame.draw.line(WIN, COLOR_LINE, (20,500) , (560, 500))
		elif EQUATION_PRINT[0] == "0" and EQUATION_PRINT[3] == "0" and EQUATION_PRINT[6] == "0":
			pygame.draw.line(WIN, COLOR_LINE, (90,20) , (90, 560))
		elif EQUATION_PRINT[1] == "0" and EQUATION_PRINT[4] == "0" and EQUATION_PRINT[7] == "0":
			pygame.draw.line(WIN, COLOR_LINE, (290,20) , (290, 560))
		elif EQUATION_PRINT[2] == "0" and EQUATION_PRINT[5] == "0" and EQUATION_PRINT[8] == "0":
			pygame.draw.line(WIN, COLOR_LINE, (490,20) , (490, 560))
		elif EQUATION_PRINT[0] == "0" and EQUATION_PRINT[4] == "0" and EQUATION_PRINT[8] == "0":
			pygame.draw.line(WIN, COLOR_LINE, (60,60) , (540, 540))
		elif EQUATION_PRINT[2] == "0" and EQUATION_PRINT[4] == "0" and EQUATION_PRINT[6] == "0":
			pygame.draw.line(WIN, COLOR_LINE, (40,560) , (560, 30))

		if EQUATION_PRINT[0] == "x" and EQUATION_PRINT[1] == "x" and EQUATION_PRINT[2] == "x":
			pygame.draw.line(WIN, COLOR_LINE, (20,100) , (560, 100))
		elif EQUATION_PRINT[3] == "x" and EQUATION_PRINT[4] == "x" and EQUATION_PRINT[5] == "x":
			pygame.draw.line(WIN, COLOR_LINE, (20,300) , (560, 300))
		elif EQUATION_PRINT[6] == "x" and EQUATION_PRINT[7] == "x" and EQUATION_PRINT[8] == "x":
			pygame.draw.line(WIN, COLOR_LINE, (20,500) , (560, 500))
		elif EQUATION_PRINT[0] == "x" and EQUATION_PRINT[3] == "x" and EQUATION_PRINT[6] == "x":
			pygame.draw.line(WIN, COLOR_LINE, (90,20) , (90, 560))
		elif EQUATION_PRINT[1] == "x" and EQUATION_PRINT[4] == "x" and EQUATION_PRINT[7] == "x":
			pygame.draw.line(WIN, COLOR_LINE, (290,20) , (290, 560))
		elif EQUATION_PRINT[2] == "x" and EQUATION_PRINT[5] == "x" and EQUATION_PRINT[8] == "x":
			pygame.draw.line(WIN, COLOR_LINE, (490,20) , (490, 560))
		elif EQUATION_PRINT[0] == "x" and EQUATION_PRINT[4] == "x" and EQUATION_PRINT[8] == "x":
			pygame.draw.line(WIN, COLOR_LINE, (60,60) , (540, 540))
		elif EQUATION_PRINT[2] == "x" and EQUATION_PRINT[4] == "x" and EQUATION_PRINT[6] == "x":
			pygame.draw.line(WIN, COLOR_LINE, (40,560) , (560, 30))


def main():

	clock = pygame.time.Clock()

	input_box1 = InputBox(610, 30, 1, 80,)
	input_boxes = [input_box1,]


	pygame.display.flip()
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			for box in input_boxes:
				box.handle_event(event)


		for box in input_boxes:
			box.update()

		if len(TEXT)== 0:
			pass
		else:
			InputBox.check(LIST1,LIST2,SCORE,TEXT)
			InputBox.winCheck()


		WIN.fill((BGCOLOR))
		for box in input_boxes:
			box.draw(WIN)


		createNumbers()
		drawLines()
		drawEquation()
		InputBox.checkplayer(PLAYER1)
		InputBox.winCheck()
#		WIN.blit(image_o, (50,100))
		pygame.display.flip()
		clock.tick(30)


main()
