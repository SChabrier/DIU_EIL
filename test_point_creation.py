def test_point_creation():
	p = point(22,7)

	def test_access_x_and_y():
		assert 22 == getx(p)
		assert 7 == gety(p)
