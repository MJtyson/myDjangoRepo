class User:

	def __init__(self, first_name , last_name ):

		self.first_name = first_name
		self.last_name = last_name
		self.login_attemts = 0


	def get_user(self):
		print(self.first_name + self.last_name + " is logged in.")


	def increments_login_attemts(self):
		self.login_attemts += 1



	def reset_login(self):

		if self.login_attemts >= 5 :
			self.login_attemts = 0

		else :
			None


while True:
	user = User(input(), input())
	user.get_user()
	user.increments_login_attemts()
	user.increments_login_attemts()
	user.increments_login_attemts()
	user.increments_login_attemts()
	user.increments_login_attemts()
	user.increments_login_attemts()
	print(user.login_attemts)
	user.reset_login()
