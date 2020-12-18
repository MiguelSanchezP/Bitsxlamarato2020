f = open ("./Files/COPEDICATClinicSympt_DATA_2020-12-17_1642.csv", 'r')

lines = []
for line in f:
	lines.append(line)

category = input ("Category to find: ")
print (lines[0].split(',').index(category))
