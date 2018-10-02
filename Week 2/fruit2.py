words = ["nasty", "apples", "gross", "yellow", "healthy"]

index = 0

fruit = input("Why don't you like bananas? ").split(" ")


for word in fruit:
	if word in words:
		print("Watch your language please")
		break
else:
	print("Nice!")
		
		





#	print(' ,'.join(fruit))