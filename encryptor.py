from ruamel.yaml import YAML 

yaml = YAML()

class Encryptor():
	rawFile = open('settings.yml', 'r').read()
	file = yaml.load(rawFile)
	chars = []
	numsArr = []
	asciiChars = 'abcdefghijklmnopqrstuvwwxyz'
	nums = '1234567890'

	def __init__(self):
		print('Encryptor loaded')
		for k, v in self.file['dictionary'].items():
			pair = [k, self.file['dictionary'][k]]
			self.chars.append(pair)
		for k, v in self.file['nums'].items():
			pair = [k, self.file['nums'][k]]
			self.numsArr.append(pair)

	def loadFile(self, string):
		with open(string, 'r') as file:
			data = file.read()
			return data

	def getChars(self):
		return self.chars

	def encrypt(self, chars):
		new = list(map(self.encryptChars, chars.lower()))
		return new

	def encryptChars(self, char):
		if self.asciiChars.count(char) > 0:
			for i in range(len(self.asciiChars)):
				if char == self.asciiChars[i - 1]:
					new = self.chars[i - 1][1]
		elif self.nums.count(char) > 0:
			for i in range(len(self.nums)):
				if char == self.nums[i]:
					new = self.numsArr[i][1]
		return new

	def decrypt(self, chars):
		new = list(map(self.decryptChars, chars))
		return new

	def decryptChars(self, char):
		for i in range(len(self.chars)):
			if self.chars[i][1] == char:
				new = self.chars[i][0]
		for i in range(len(self.numsArr)):
			if self.numsArr[i][1] == char:
				new = self.numsArr[i][0]
		return new