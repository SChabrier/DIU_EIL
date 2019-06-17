
class point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	    
	def getx(self):
		return self.x
	
	def gety(self):
		return self.y
	   
	def __eq__(self,other):
		return self.x == other.getx() and self.y == other.gety()


def test_equality():
	p1 = point(1 ,3)
	p2 = point(1 ,3)
	p3 = point(2 ,5)
	p4 = point(6 ,45)
    
	assert p1 == p1
	assert p1 == p2
	assert p2 == p1
	assert p1 != p3
