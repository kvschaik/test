calories = 42
fat = 0
carbs = 10.6
sugar = 10.6

ml = input("how much ml did you drink?")

caloriesnew = 42 / 100 * int(ml)
fatnew = fat / 100 * int(ml)
caloriesnew = calories / 100 * int(ml)
carbsnew = carbs / 100 * int(ml)

sugarnew = sugar / 100 * int(ml)
print("The " + ml + " ml of Coca Cola you've had contains: " + str(caloriesnew) + " calories, " + str(fatnew) + " grams of fat, " + str(carbsnew) + " gram carbs, and " + str(sugarnew) + " grams of sugar. "   )