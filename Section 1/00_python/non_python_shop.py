# Just Experience it python

class Chai:
# Open up a factory, there is method knows as "__init__"
# class init ==> means class initialize
	def __init__(self, sweetness, milk_level): 
		self.sweetness = sweetness
		self.milk_level = milk_level
	
	# Set up a factory --> Create method or function
	def sip(self):
		print("Sipping chai")

  # Set up another factory
	def add_sugar(self, amount):
		print("added the sugar")
  
my_chai = Chai(sweetness=3, milk_level=2)

my_chai.add_sugar(3)