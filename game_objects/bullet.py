import phisic.vector
import game_objects.body
import serving.miniFunc as mFunc
import phisic.hitbox
import serving.write as log

#initCord, vector, speed
class Lazer:
	
	def __init__(self, initCord, aim, speed):
		self.body = game_objects.body.Rect(initCord, [-3,0],-50,6,"resource/lazer_sqr.png")
		self.body.speed = speed
		
		self.body.vec = phisic.vector.Vector(point1 = phisic.hitbox.Point(initCord),point2 = aim)
		
		if self.body.vec.isZero():#there is some bug with (0,0) vector
			self.body.vec.plus(phisic.vectssssor.Vector(0.01, 0.01))

		self.body.vec.normalize()
		self.body.drug = 0
		self.body.rotateToPointSec(aim)


	def draw(self, canvas):
		#self.body.visualDebag(canvas)
		self.body.draw(canvas)

	