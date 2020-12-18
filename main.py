f = open ("./Files/COPEDICATClinicSympt_DATA_2020-12-17_1642.csv", 'r')

data = []
for line in f:
	data.append(line)

patients_COVID_Positive = []

for value in data:
	if value.split(',')[122] == '1' or value.split(',')[127] == '1':
		patients_COVID_Positive.append(value)
