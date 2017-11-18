import pyperclip

class cliplog:
	def __init__(self,address):
		self.clipboard = pyperclip.paste()
		self.temp = ''
		self.address = address

	def log(self):
		with open(self.address,'w+') as file:
			while True:
				try:
					if self.clipboard != self.temp:
						file.write(self.clipboard+'\n')
						self.temp = self.clipboard
						self.clipboard = pyperclip.paste()
					else:
						self.clipboard = pyperclip.paste()
				except KeyboardInterrupt:
					break
		print("\nThe log has been successfully saved in {}".format(self.address))
		return 0

c = input('Path to file:- ')
obj = cliplog(c)
obj.log()
