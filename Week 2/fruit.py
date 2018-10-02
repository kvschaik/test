words = ["Orange", "Apple", "Banana", "Watermelon", "Peach"]

index = 0

fruit = input("What is your favorite fruit? ").title()

for word in words:
	if fruit in words:
		print("I don't like " + fruit + " I prefer blueberries" )
		break
	else:
		print("Nice! I like " + fruit + " too!" )
		break
		
