class Restruant:
	"""this is a restruant program"""

	def __init__(self, restruant_name, cuisine_type):
		self.restruant_name = restruant_name
		self.cuisine_type = cuisine_type


	def describe_restruant(self):
		print(self.restruant_name +"is"+ self.cuisine_type + "cuisine.")


	def open_restruant(self):
		print(self.restruant_name +"is opened.")




restruant = Restruant("Bawarchi", "Indo-arabic")

restruant.describe_restruant()
restruant.open_restruant()
