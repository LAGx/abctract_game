import phisic.hitbox
import phisic.vector
import pygame
import serving.miniFunc as mFunc
import copy
import math

class Rect:
	#initCenter is main point(absolute cord), all body rotate around this
	#initHitbox is relative by initCenter
	#picture drawing by center on initCenter
	def __init__(self, initCenter, initHitbox, lenthHitbox, widthHitbox, image):
		#HITBOX block
		self.hitboxStart = phisic.hitbox.Rect(mFunc.plusLists(initHitbox, initCenter), lenthHitbox, widthHitbox)
		self.hitboxStart.center = phisic.hitbox.Point(initCenter)
		self.hitbox = copy.deepcopy(self.hitboxStart)
		#image block
		self.image = pygame.image.load(image)
		self.image.set_colorkey((0,0,0))
		self.imageForRotate = self.image
		self.rect = self.image.get_rect()
		#vector block
		self.vec = phisic.vector.Vector()
		self.drug_vec = phisic.vector.Vector()

		#scalar 
		self.rotate_degree = 0 
		self.delta_rotate = 0	# -clockwise +counter-clockwise

		self.speed = 1
		self.drug = 1


	def vectorMachine(self):
		self.drug_vec.changeXEx(self.vec.posX)
		self.drug_vec.changeYEx(self.vec.posY)
		self.drug_vec.multiply(self.drug)
		self.drug_vec.invert()
		self.vec.plus(self.drug_vec)


	def rotating(self, setDelta = None):
		if setDelta != None:
			self.delta_rotate = setDelta
		if self.rotate_degree > 360:
			self.rotate_degree = 0
		else:
			self.rotate_degree += self.delta_rotate

		self.toTurn(self.rotate_degree)

	def toTurn(self, setAngle): #setting by normal position
		self.hitbox = copy.deepcopy(self.hitboxStart)
		self.rotate_degree = setAngle
		self.imageForRotate = pygame.transform.rotate(self.image, -self.rotate_degree)
		self.rect = self.imageForRotate.get_rect(center=self.rect.center)
		self.hitbox.rotate(self.hitboxStart.center, self.rotate_degree)

	def rotateToPointFirst(self, point):
		vec_player_aim = phisic.vector.Vector(point1 = self.hitboxStart.center, point2 = point)
		if point.p[0] > self.hitboxStart.center.p[0]:
			self.toTurn(math.degrees(math.acos(phisic.vector.getScalar(self.hitboxStart.getAndUpdateVector(),vec_player_aim))))
		else:
			self.toTurn(math.degrees(-math.acos(phisic.vector.getScalar(self.hitboxStart.getAndUpdateVector(),vec_player_aim))))

	def rotateToPointSec(self, point):
		vec_player_aim = phisic.vector.Vector(point1 = self.hitboxStart.center, point2 = point)
		if point.p[0] > self.hitboxStart.center.p[0]:
			self.toTurn(math.degrees(math.acos(-phisic.vector.getScalar(self.hitboxStart.getAndUpdateVector(),vec_player_aim))))
		else:
			self.toTurn(math.degrees(-math.acos(-phisic.vector.getScalar(self.hitboxStart.getAndUpdateVector(),vec_player_aim))))

	def move(self, xy):
		self.hitboxStart.move(xy, "add")
		self.hitboxStart.center.change(xy, "add")

	def teleport(self, xy):
		self.hitboxStart.move(xy, "instead")
		self.hitboxStart.center.change(xy, "instead")

	def draw(self, canvas):

		self.rotating()
		self.vectorMachine()
		self.move(self.vec.multiplyAndGetCordList(self.speed))

		canvas.blit(self.imageForRotate, (self.hitboxStart.center.p[0] - (self.image.get_width()/2)+self.rect.x-self.vec.posX, self.hitboxStart.center.p[1] - (self.image.get_height()/2)+self.rect.y-self.vec.posY)) #add in cords self.rect.(x, y)


	def visualDebag(self, canvas, color = (200,20,2)):
		pygame.draw.circle(canvas, color, [int(self.hitboxStart.center.p[0]),int(self.hitboxStart.center.p[1])], 4) #hitboxCenter
		self.hitbox.draw(canvas, color)#hitbox
		pygame.draw.circle(canvas, color, [int(self.hitboxStart.center.p[0] - (self.image.get_width()/2)+self.rect.x),int(self.hitboxStart.center.p[1] - (self.image.get_height()/2)+self.rect.y)], 1)#start of drawing picture




class Circle:

	#initCenter is main point(absolute cord), all body rotate around this
	#initHitbox is relative by initCenter
	#picture drawing by center on initCenter
	def __init__(self, initCenter, initHitbox, radius, image):
		#HITBOX block
		self.hitboxStart = phisic.hitbox.Circle(mFunc.plusLists(initHitbox, initCenter), radius)
		self.hitboxStart.center = phisic.hitbox.Point(initCenter)
		self.hitbox = copy.deepcopy(self.hitboxStart)
		#image block
		self.image = pygame.image.load(image)
		self.image.set_colorkey((0,0,0))
		self.imageForRotate = self.image
		self.rect = self.image.get_rect()
		#vector block
		self.vec = phisic.vector.Vector()
		self.drug_vec = phisic.vector.Vector()

		self.rotate_degree = 0 
		self.delta_rotate = 0	# -clockwise +counter-clockwise

		self.speed = 1
		self.drug = 1


	def vectorMachine(self):  
		self.drug_vec.changeXEx(self.vec.posX)
		self.drug_vec.changeYEx(self.vec.posY)
		self.drug_vec.multiply(self.drug)
		self.drug_vec.invert()
		self.vec.plus(self.drug_vec)


	def rotating(self, setDelta = None):
		if setDelta != None:
			self.delta_rotate = setDelta
		if self.rotate_degree > 360:
			self.rotate_degree = 0
		else:
			self.rotate_degree += self.delta_rotate

		self.toTurn(self.rotate_degree)

	def toTurn(self, setAngle): #setting by normal position
		self.hitbox = copy.deepcopy(self.hitboxStart)
		self.rotate_degree = setAngle
		self.imageForRotate = pygame.transform.rotate(self.image, -self.rotate_degree)
		self.rect = self.imageForRotate.get_rect(center=self.rect.center)
		self.hitbox.rotate(self.hitboxStart.center, self.rotate_degree)


	def move(self, xy):
		self.hitboxStart.move(xy)
		self.hitboxStart.center.change(xy, "add")


	def draw(self, canvas):

		self.rotating()
		self.vectorMachine()
		self.move(self.vec.multiplyAndGetCordList(self.speed))

		canvas.blit(self.imageForRotate, (self.hitboxStart.center.p[0] - (self.image.get_width()/2)+self.rect.x, self.hitboxStart.center.p[1] - (self.image.get_height()/2)+self.rect.y)) #add in cords self.rect.(x, y)


	def visualDebag(self, canvas, color = (200,20,2)):
		pygame.draw.circle(canvas, color, [int(self.hitboxStart.center.p[0]),int(self.hitboxStart.center.p[1])], 4) #hitboxCenter
		self.hitbox.draw(canvas, color)#hitbox
		pygame.draw.circle(canvas, color, [int(self.hitboxStart.center.p[0] - (self.image.get_width()/2)+self.rect.x),int(self.hitboxStart.center.p[1] - (self.image.get_height()/2)+self.rect.y)], 1)#start of drawing picture

