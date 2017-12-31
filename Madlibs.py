	#This is a madlib story, written by Codecademy ft. Matt
	print "My story"
	
	name = raw_input("What is your name? ")
	adj1 = raw_input("What is your first adjective? ")
	adj2 = raw_input("What is your second adjective? ")
	adj3 = raw_input("What is your third adjective? ")
	verb1 = raw_input("What is your first verb? ")
	verb2 = raw_input("What is your second verb? ")
	verb3 = raw_input("What is your third verb? ")
	noun1 = raw_input("What is your first noun? ")
	noun2 = raw_input("What is your second noun? ")
	noun3 = raw_input("What is your third noun? ")
	noun4 = raw_input("What is your fourth noun? ")
	animal = raw_input("Name an animal? ")
	food = raw_input("what kind of food? ")
	fruit = raw_input("What kind of fruit? ")
	number = raw_input("How many? ")
	superhero_name = raw_input("What is the name of a superhero? ")
	country = raw_input("What is the name of a country? ")
	dessert = raw_input("What is the name of a dessert? ")
	year = raw_input("What year would you like to use? ")
	
	
	
	#The template for the story
	STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."
	
	print STORY % (adj1, name, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, name, verb3, number, name, superhero_name, superhero_name, name, country, name, dessert, name, year, noun4)
