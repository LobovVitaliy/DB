class Airplanes(list):
	def append(self, airplane):
		if (airplane not in self):
			super(Airplanes, self).append(airplane)

	def __str__(self):
		return '\n'.join(str(i) for i in self)

class Airplane():
	def __init__(self, number, pilot):
		self.number = number
		self.pilot  = pilot

	def __str__(self):
		return 'Number: %s, Pilot: %s' % (self.number, self.pilot)