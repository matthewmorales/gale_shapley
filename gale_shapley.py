
rank_file = open("list.txt","r")
lines = rank_file.readlines()
rank_file.close()

rankLists = []
boyLikes  = []
girlLikes = []

for line in lines:
	rankLists.append(map(int, line.rstrip('\n').split('<')))

for x in range(0, len(lines)/2):
	boyLikes.append(rankLists[x])

for x in range(len(lines)/2, len(lines)):
	girlLikes.append(rankLists[x])

print "\nBOYS AND THEIR PREFERENCES: \n"
for index, item in enumerate(boyLikes):
        print("Boy (%s): %s" % (index, item))

print "\nGIRLS AND THEIR PREFERENCES \n"
for index, item in enumerate(girlLikes):
        print("Girl (%s): %s" % (index, item))


def gale_shapley():

	bachelorBoys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	girlTaken = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #index refers to girl, value refers to boy so if girlsTaken[5] = 3, it means girl 5 is taken by boy 3
	
	while bachelorBoys:
		boy = bachelorBoys.pop(0)
		boysPreference = boyLikes[boy]
		girl = boysPreference.pop(0)
		

		if girlTaken[girl] < 1:
			#girl is not taken.
			girlTaken[girl] = boy
			print("Boy %s and Girl %s are engaged" % (boy, girl))
		else:
			#The girl he wants is taken
			girlsPreference = girlLikes[girl]
			if girlsPreference.index(girlTaken[girl]) > girlsPreference.index(boy):
				#girl likes new boy
				oldBoy = girlTaken[girl]
				girlTaken[girl] = boy
				print("Girl %s dumped Boy %s for Boy %s" % (girl, oldBoy, boy))
				if boyLikes[oldBoy]:
					#there are still girls on his list
					bachelorBoys.append(oldBoy)
			else:
				#stays with old boyfriend
				if boysPreference:
					bachelorBoys.append(boy)
	return girlTaken

print("\n Pairs: \n")
pairs = gale_shapley()

for index, item in enumerate(pairs):
        print("Girl (%s) is engaged to Boy (%s)" % (index, item))
				