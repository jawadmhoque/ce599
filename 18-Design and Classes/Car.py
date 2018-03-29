class Car(object):

	"""
	Base class for a car
	"""
	def __init(self,color,location=[0,0],direction='N'):
		self.color=color
		self.location=location
		self.x=location[0]
		self.y=location[1]
		self.direction=direction
	
	def go(self,units):
		"""
		function to move car forward
		"""
		if self.direction=='N':
			self.y=self.y+units
		elif self.direction=='S':
			self.y=self.y-units
		elif self.direction=='E':
			self.x=self.x+units
		else:
			self.x=self.x-units
		self.location=[self.x,self.y]
		
		print (self.location)
	
	def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        else:
            self.direction = 'N'
        
            
    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        else: 
            self.direction = 'S'
        
            
    def printcar(self):
        print('Car Color is ' + self.color)
        print('Car Location is ')
        print(self.location)
        print('Car Direction is ' + self.direction)