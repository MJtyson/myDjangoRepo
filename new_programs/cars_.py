class Car:

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0


	def get_details(self):
		print(self.make+ " " +self.model+" is manufactured in "+self.year)


	def read_odometer(self):
		print("This car has "+ str(self.odometer) + " miles on it.")


	def update_odometer(self, milages):
		
		if milages >= self.odometer:
			self.odometer = milages
		else:
			print("NO change in the odometer")


	def increament_odometer(self, miles):

		self.odometer += miles

		



caras = Car("BMW", "Q4", "2016")
caras.get_details()
#caras.odometer = 24
caras.update_odometer(14)
caras.increament_odometer(20)
caras.read_odometer()