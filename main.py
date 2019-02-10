from encryptor import Encryptor

encryptor = Encryptor()
encrypted = ''

#string = input('Enter string to be encrypted: ')
string = encryptor.loadFile('text.txt')

chars = encryptor.getChars()
newChars = encryptor.encrypt(string)

for i in range(len(newChars)):
	print(newChars[i])

for i in range(len(newChars)):
	encrypted += newChars[i]


decrypted = encryptor.decrypt(encrypted)

for i in range(len(newChars)):
	print(decrypted[i])