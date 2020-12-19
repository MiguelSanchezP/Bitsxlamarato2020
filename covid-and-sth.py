import matplotlib.pyplot as plt
import numpy as np
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

def look_for_pathologies (patients, condition,plot):
    condition_data = []
    for condition in condition.split(','):
        positive_with_condition = 0
        positive_without_condition = 0
        for patient in patients:
            if patients.split(',')[int(other_condition[1][other_condition[0].index(condition)])] == other_condition[2][other_condition[0].index(condition)]:
                positive_with_condition += 1
            elif patients.split(',')[int(other_condition[1][other_condition[0].index(condition)])] == other_condition[3][other_condition[0].index(condition)]:
                positive_without_condition += 1
        data = [condition, positive_with_condition, positive_without_condition]
        condition_data.append(data)
        if plot:
			plot_data = [positive_with_condition, positive_without_condition]
			plot_labels = ["COVID+other", "Only COVID"]
			plt.pie (plot_data, labels=plot_labels)
			plt.title (condition)
    if plot:
		plt.show()
	return symptoms_data

def find_incompatible_pathologies (patients, condition,plot):
    condition_data = []
    for condition in condition.split(','):
        negative_with_condition = 0
        negative_without_condition = 0
        for patient in patients:
            if patients.split(',')[int(other_condition[1][other_condition[0].index(condition)])] == other_condition[2][other_condition[0].index(condition)]:
                negative_with_condition += 1
            elif patients.split(',')[int(other_condition[1][other_condition[0].index(condition)])] == other_condition[3][other_condition[0].index(condition)]:
                negative_without_condition += 1
        data = [condition, positive_with_condition, positive_without_condition]
        condition_data.append(data)
        if plot:
			plot_data = [positive_with_condition, positive_without_condition]
			plot_labels = ["not COVID", "nothing"]
			plt.pie (plot_data, labels=plot_labels)
			plt.title (condition)
    if plot:
		plt.show()
	return symptoms_data

other_condition = [["vrs","adeno","fluA","fluB","coviruses","bacterial infections", "comorbidies","vaccines"],
["126","127","128","129","137","140","143","190"],
['1','1','1','1','1','1','1','1'],
['2','2','2','2','2','2','2']]
