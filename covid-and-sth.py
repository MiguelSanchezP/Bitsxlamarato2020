f = open ("COPEDICATClinicSympt_DATA_2020-12-17_1642.csv", 'r')

data = []
for line in f:
	data.append(line)

patients_COVID_Positive = []
patients_COVID_Negative = []

for value in data:
	if value.split(',')[31] == '1' and (value.split(',')[117] == '1' or value.split(',')[122] == '1' or value.split(',')[107] == '1'):
		patients_COVID_Positive.append(value)
	elif value.split(',')[31] == '1' and ((value.split(',')[117] == '2' or value.split(',')[117] == '') and (value.split(',')[122] == '2' or value.split(',')[122] == '') and (value.split(',')[107] == '2' or value.split(',')[107] == '')):
		patients_COVID_Negative.append(value)

def look_for_pathologies (patients, condition):
    

other_condition = [["vrs","adeno","fluA","fluB","coviruses","bacterial infections", "comorbidies","vaccines"]
["126","127","128","129","137","140","143","190"]
['1','1','1','1','1','1'['cardiopathy___1','hypertension___1','pulmonar_disease___1','asma___1','nephrology___1','hepatic___1','neurologic___1','diabetes___1','tuberculosi___1', 'idp___1','neoplasia___1','kawasaki___1','vih_others___1',int(value.split(',')[143]) => 97]'1']
['2','2','2','2','2','2'['cardiopathy___2','hypertension___2','pulmonar_disease___2','asma___2','nephrology___2','hepatic___2','neurologic___2','diabetes___2','tuberculosi___2', 'idp___2','neoplasia___2','kawasaki___2','vih_others___2',int(value.split(',')[143]) < 97]'2']]